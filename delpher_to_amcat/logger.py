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
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# create file handler
fh = logging.FileHandler('delpher_to_amcat.log')
fh.setLevel(logging.INFO)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.WARN)

# display time and thread name in log entries
formatter = logging.Formatter('%(asctime)s: %(threadName)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

log.addHandler(ch)
log.addHandler(fh)
