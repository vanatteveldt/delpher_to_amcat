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
from delpher_to_amcat.transfer import DelpherToAmcat


if __name__ == '__main__':
    # thread1 = DelpherToAmcat(from_date='01-01-1945', until_date='31-12-1954')
    thread1 = DelpherToAmcat(from_date='01-01-1945', until_date='03-01-1945')
    thread1.start()
    '''
    thread2 = DelpherToAmcat(from_date='01-01-1955', until_date='31-12-1964')
    thread2.start()
    thread3 = DelpherToAmcat(from_date='01-01-1965', until_date='31-12-1974')
    thread3.start()
    thread4 = DelpherToAmcat(from_date='01-01-1975', until_date='31-12-1984')
    thread4.start()
    thread5 = DelpherToAmcat(from_date='01-01-1985', until_date='31-12-1994')
    thread5.start()
    thread6 = DelpherToAmcat(from_date='01-01-1995', until_date='31-12-1995')
    thread6.start()
    '''
