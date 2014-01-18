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
import requests


def get(url):
    """Make an HTTP request to the given URI.

    Returns the deserialized json if successful, and raises an exception otherwise

    Args:
        url: String of URI

    Returns:
        JSON requested from given URI

    Raises:
        Exception: If returned status code doesn't equal 200
        Exception: If returned body has no JSON representation
    """
    expected_status = 200

    r = requests.get(url)

    if r.status_code != expected_status:
        raise Exception(
            "Request {url!r} returned code {r.status_code}, expected {expected_status}:\n{r.text}".format(
                **locals()))

    try:
        return r.json()
    except:
        raise Exception("Cannot decode json; text={r.text!r}".format(**locals()))
