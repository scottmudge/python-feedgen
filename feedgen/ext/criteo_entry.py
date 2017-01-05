# -*- coding: utf-8 -*-
'''
    feedgen.ext.criteo
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce criteo feeds.

    :copyright: 2016, Raspbeguy <raspbeguy@hashtagueule.fr>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

from lxml import etree
from feedgen.ext.base import BaseEntryExtension

CRITEO_NS = 'http://base.google.com/ns/1.0'


class CriteoEntryExtension(BaseEntryExtension):
    '''FeedEntry extention for criteo feeds
    '''
    def __init__(self):
        self.__criteo_id = None
        self.__criteo_title = None
        self.__criteo_description = None
        self.__criteo_google_product_category = None

    def extend_rss(self, entry):
        '''Add additional fields to an RSS item.

        :param feed: The RSS item XML element to use.
        '''
        if self.__criteo_id:
            id = etree.SubElement(entry, '{%s}id' % CRITEO_NS)
            id.text = self.__criteo_id

        if self.__criteo_title:
            title = etree.SubElement(entry, '{%s}title' % CRITEO_NS)
            title.text = self.__criteo_title

        if self.__criteo_description:
            description = etree.SubElement(entry,
                                           '{%s}description' % CRITEO_NS)
            description.text = self.__criteo_description

        if self.__criteo_google_product_category:
            google_product_category = etree.SubElement(
                    entry, '{%s}google_product_category' % CRITEO_NS)
            google_product_category.text = \
                self.__criteo_google_product_category

    def id(self, criteo_id=None):
        '''Get or set the number od id

        :param criteo_title: The id number.
        :returns: The id number.
        '''
        if criteo_id is not None:
            self.__criteo_id = criteo_id
        return self.__criteo_id

    def title(self, criteo_title=None):
        '''Get or set the hash of the target file.

        :param criteo_title: The target file hash.
        :returns: The target hash file.
        '''
        if criteo_title is not None:
            self.__criteo_title = criteo_title
        return self.__criteo_title

    def description(self, criteo_description=None):
        '''Get or set the size of the target file.

        :param criteo_description: The target file size.
        :returns: The target file size.
        '''
        if criteo_description is not None:
            self.__criteo_description = criteo_description
        return self.__criteo_description

    def google_product_category(self, criteo_google_product_category=None):
        '''Get or set the size of the target file.

        :param criteo_google_product_category: The target file size.
        :returns: The target file size.
        '''
        if criteo_google_product_category is not None:
            self.__criteo_google_product_category = \
                criteo_google_product_category
        return self.__criteo_google_product_category
