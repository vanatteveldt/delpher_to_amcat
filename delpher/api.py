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
from delpher import request
from settings.delpher import *
from delpher_to_amcat.logger import log


class DelpherAPI:
    """Provide access to search result pages from the public API of kranten.delpher.nl

    Documentation of the API is available at http://kranten.delpher.nl/nl/api

    Attributes:
        from_date: Start of period to search in. Format: %d-%m-%Y
        until_date: End of period to search in. Format: %d-%m-%Y
        collection: Identifier of the collection to retrieve documents for. Default: ddd
            (see http://kranten.delpher.nl/nl/api/explain/coll/list/)
        record_type: Document type . Default: artikel
        ppn: Identifier of the paper to search in. Default: 832675288 (De Telegraaf)
    """
    page = 0
    records_processed = 0
    number_of_records = None

    def __init__(self, ppn, from_date, until_date, collection='ddd', record_type='artikel'):

        self.ppn = ppn
        items_per_page = 100
        self.query = query_template.format(**locals())

        log.info('Start transferring articles. Collection: {collection}; Record type: {record_type}; '
                 'PPN: {ppn}; From: {from_date}; Until: {until_date}.'.format(**locals()))

    def result_pages(self):
        """Get iterator over result pages."""
        while self.number_of_records is None or self.records_processed < self.number_of_records:

            self.page += 1
            articles = self.list_next_articles()

            self.records_processed += len(articles)

            yield articles

    def results(self):
        """Get iterator over results."""
        for article in (result_page for result_page in self.result_pages()):
            yield article

    def results_url(self):
        """Generate URL to retrieve next page of search results.
        """
        return self.query + str(self.page)

    def list_next_articles(self):
        """Retrieve next page of search results
        """
        url = self.results_url()

        try:
            response = request.get(url)
        except:
            log.exception('Could not get results for url {url}'.format(**locals()))
            return []

        self.number_of_records = response['numberOfRecords']
        log.info('Page {self.page} of article list retrieved. '
                 '{self.records_processed} of {self.number_of_records} articles processed.'.format(**locals()))

        return response['records']

    @staticmethod
    def ocr_url(identifier):
        """Generate URL to get OCR data from
        """
        identifier_parts = identifier.split('?')
        if len(identifier_parts) > 1:
            return ocr_base_url + identifier_parts[1]
        else:
            log.error('Could not generate OCR link for identifier ' + identifier)
            return ''

    @staticmethod
    def article_ocr(identifier):
        """Retrieve ocr full text for article with identifier
        """
        url = DelpherAPI.ocr_url(identifier)
        try:
            response = request.get(url)
        except:
            log.exception('Could not get OCR data for url {url}.'.format(**locals()))
            return '<failed to load>'

        if response is None:
            log.error('Did not get OCR data for url {url}.'.format(**locals()))
            return '<failed to load>'
        else:
            # Each paragraph is one item in the list
            return "\n\n".join([response[key] for key in sorted(response.keys()) if key != 'title'])
