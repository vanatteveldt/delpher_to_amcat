###########################################################################
#          (C) Vrije Universiteit, Amsterdam (the Netherlands)            #
#                                                                         #
# This file is part of AmCAT - The Amsterdam Content Analysis Toolkit     #
#                                                                         #
# AmCAT is free software: you can redistribute it and/or modify it under  #
# the terms of the GNU Lesser General Public License as published by the  #
# Free Software Foundation, either version 3 of the License, or (at your  #
# option) any later version.                                              #
#                                                                         #
# AmCAT is distributed in the hope that it will be useful, but WITHOUT    #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or   #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public     #
# License for more details.                                               #
#                                                                         #
# You should have received a copy of the GNU Lesser General Public        #
# License along with AmCAT.  If not, see <http://www.gnu.org/licenses/>.  #
###########################################################################
from datetime import datetime
import threading
import json

from delpher_to_amcat.logger import log
from settings import amcat, delpher
from amcat.api import AmcatAPI
from delpher.api import DelpherAPI


class DelpherToAmcat(threading.Thread):

    set_id = None

    def __init__(self, from_date, until_date):
        threading.Thread.__init__(self)

        self.delpher_api = DelpherAPI(delpher.ppn, from_date, until_date)
        self.amcat_api = self.setup_amcat(from_date, until_date)

    def run(self):
        """Start the transfer process of articles from kranten.delpher.nl to amcat.vu.nl
        """
        for result_page in self.delpher_api.result_pages():

            articles = [DelpherToAmcat.convert_article(article) for article in result_page]
            self.upload_to_amcat(articles)

        log.info('Done. Processed all articles in set {self.set_id}.'.format(**locals()))

    def setup_amcat(self, from_date, until_date):
        """Create Amcat API object and save configuration data for later use.
        """
        amcat_api = AmcatAPI(amcat.host, amcat.username, amcat.password)

        log.info('Setup Amcat API with host {0}, username {1}. Use project {2}'.format(amcat.host, amcat.username,
                                                                                       amcat.project))

        now = datetime.now().replace(microsecond=0)
        set_name = amcat.set_name_template.format(**locals())

        try:
            aset = amcat_api.create_set(project=amcat.project, name=set_name, provenance=amcat.data_provenance)
        except:
            log.exception('Could not create article set')
            raise

        log.info('Created article set in Amcat. ID: {0}'.format(aset['id']))

        self.set_id = aset['id']

        return amcat_api

    @staticmethod
    def convert_article(article):
        """Convert article from KB format to AMCAT format.

        Unused keys in AMCAT format are: section, byline, length, externalid, author, addressee, uuid

        Args:
            article: representation of one article as retrieved from Delpher API. Predicate: Identifier and date are
            always set.

        Returns:
            An article in Amcat's representation. Postcondition: date, headline, text, and medium are always set.
        """
        ocr = DelpherAPI.article_ocr(article['identifier'])
        page = article.get('page', '')

        return {
            'date': datetime.strptime(article['date'], '%Y/%m/%d %H:%M:%S').isoformat(),
            'headline': article.get('title', '%(ocr).30s...' % {'ocr': ocr}),  # headline must not be empty
            'medium': article.get('papertitle', 'ppn: {0}'.format(delpher.ppn)),
            'text': ocr if len(ocr) > 0 else '<no text>',
            'pagenr': int(page) if page.isdigit() else '',
            'url': article.get('metadataKey', ''),
            'metastring': json.dumps(article)  # Just store all available information for potential later use.
        }

    def upload_to_amcat(self, articles):
        """Create articles in Amcat using AmcatAPI

        Args:
            articles: List of articles in Amcat's format
        """
        try:
            self.amcat_api.create_articles(project=amcat.project, articleset=self.set_id, json_data=articles)
        except:
            log.exception('Could not upload articles to amcat. url: {amcat.project}; set: {self.set_id}; '
                          'data: {articles}'.format(**locals()))
