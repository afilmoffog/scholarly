"""scholarly.py"""
import requests
from ._navigator import Navigator

_AUTHSEARCH = '/citations?hl=en&view_op=search_authors&mauthors={0}'
_KEYWORDSEARCH = '/citations?hl=en&view_op=search_authors&mauthors=label:{0}'
_PUBSEARCH = '/scholar?hl=en&q={0}'


class _Scholarly(object):
    """docstring for scholarly"""
    def __init__(self):
        self.__nav = Navigator()

    def use_proxy(self, http: str, https: str):
        self.__nav._use_proxy(http, https)

    def search_pubs(self, query):
        """Search by query and returns a generator of Publication objects

        :Example::
        >>> search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
        >>> print(next(search_query))
        {
            'bib':{
                    'abstract':'Humans can judge from vision alone whether an object is '
                                'physically stable or not. Such judgments allow observers '
                                'to predict the physical behavior of objects, and hence '
                                'to guide their motor actions. We investigated the visual '
                                'estimation of physical stability of 3-D objects (shown '
                                'in stereoscopically viewed rendered scenes) and how it '
                                'relates to visual estimates of their center of mass '
                                '(COM). In Experiment 1, observers viewed an object near '
                                'the edge of a table and adjusted its tilt to the '
                                'perceived critical angle, ie, the tilt angle at which '
                                'the object …',
                    'author': 'SA Cholewiak and RW Fleming and M Singh',
                    'eprint': 'https://jov.arvojournals.org/article.aspx?articleID=2213254',
                    'title': 'Perception of physical stability and center of mass of 3-D '
                          'objects',
                    'url': 'https://jov.arvojournals.org/article.aspx?articleID=2213254',
                    'venue': 'Journal of vision',
                    'year': ' 2015'
            },
            'citedby': 19,
            'filled': False,
            'id_scholarcitedby': '15736880631888070187',
            'source': 'scholar',
            'url_scholarbib': 'https://scholar.googleusercontent.com/scholar.bib?q=info:K8ZpoI6hZNoJ:scholar.google.com/&output=citation&scisdr=CgXsOAkeGAA:AAGBfm0AAAAAXsLLJNxa7vzefAEwz6a3tLCEoMsli6vj&scisig=AAGBfm0AAAAAXsLLJNK0I3FleN-7_r_TxUF8m5JDa9W5&scisf=4&ct=citation&cd=0&hl=en'
        }
        """
        url = _PUBSEARCH.format(requests.utils.quote(query))
        return self.__nav.search_publications(url)

    def search_single_pub(self, pub_title: str, filled: bool = False):
        """Search by scholar query and return a single Publication object"""
        url = _PUBSEARCH.format(requests.utils.quote(pub_title))
        return self.__nav.search_publication(url, filled)

    def search_author(self, name):
        """Search by author name and return a generator of Author objects

        :Example::
        >>> search_query = scholarly.search_author('Marty Banks, Berkeley')
        >>> print(next(search_query))
        {
            'affiliation': 'Professor of Vision Science, UC Berkeley',
            'citedby': 20160,
            'email': '@berkeley.edu',
            'filled': False,
            'id': 'Smr99uEAAAAJ',
            'interests': ['vision science', 'psychology', 'human factors', 'neuroscience'],
            'name': 'Martin Banks',
            'url_picture': 'https://scholar.google.com/citations?view_op=medium_photo&user=Smr99uEAAAAJ'
        }
        """
        url = _AUTHSEARCH.format(requests.utils.quote(name))
        return self.__nav.search_authors(url)

    def search_keyword(self, keyword):
        """Search by keyword and return a generator of Author objects

        :Example::
        >>> search_query = scholarly.search_keyword('Haptics')
        >>> print(next(search_query))
        {
            'affiliation': 'Postdoctoral research assistant, University of Bremen',
            'citedby': 55943,
            'email': '@collision-detection.com',
            'filled': False,
            'id': 'lHrs3Y4AAAAJ',
            'interests': ['Computer Graphics',
                       'Collision Detection',
                       'Haptics',
                       'Geometric Data Structures'],
            'name': 'Rene Weller',
            'url_picture': 'https://scholar.google.com/citations?view_op=medium_photo&user=lHrs3Y4AAAAJ'
        }
        """
        url = _KEYWORDSEARCH.format(requests.utils.quote(keyword))
        return self.__nav.search_authors(url)

    def search_pubs_custom_url(self, url):
        """Search by custom URL and return a generator of Publication objects
        URL should be of the form '/scholar?q=...'"""
        return self.__nav.search_publications(url)

    def search_author_custom_url(self, url):
        """Search by custom URL and return a generator of Author objects
        URL should be of the form '/citation?q=...'"""
        return self.__nav.search_authors(url)
