# -*- coding: utf-8 -*-
'''
    feedgen.ext.criteo
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce criteo feeds.

    :copyright: 2016, Raspbeguy <raspbeguy@hashtagueule.fr>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

from feedgen.ext.base import BaseExtension

CRITEO_NS = 'http://base.google.com/ns/1.0'


class CriteoExtension(BaseExtension):
    '''FeedGenerator extension for criteo feeds.
    '''

    def __init__(self):
        self.__title = None
        self.__link = None
        self.__description = None

    def title(self, criteo_title=None):
        '''Get or set the hash of the target file.

        :param criteo_title: The target file hash.
        :returns: The target hash file.
        '''
        if criteo_title is not None:
            self.__title = criteo_title
        return self.__title

    def link(self, criteo_link=None):
        '''Get or set the hash of the target file.

        :param criteo_title: The target file hash.
        :returns: The target hash file.
        '''
        if criteo_link is not None:
            self.__link = criteo_link
        return self.__link

    def description(self, criteo_description=None):
        '''Get or set the hash of the target file.

        :param criteo_title: The target file hash.
        :returns: The target hash file.
        '''
        if criteo_description is not None:
            self.__description = criteo_description
        return self.__description

    def extend_ns(self):
        return {'criteo': CRITEO_NS}
