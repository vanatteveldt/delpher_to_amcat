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
ppn = '832675288'
ocr_base_url = 'http://kranten.delpher.nl/nl/async/resolverproxy?'
query_template = 'http://kranten.delpher.nl/nl/api/results/coll/{collection}/query//facets%5Btype%5D/{record_type}/cql/%28date+_gte_+{from_date}%29/cql/%28date+_lte_+{until_date}%29/cql/%28ppn+any+%28%22{ppn}%22%29%29/maxperpage/{items_per_page}/sortfield/date/page/'
