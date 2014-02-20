# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.utils import createContentInContainer
from Products.CMFCore.utils import getToolByName

from ..testing import CGEO_BEHAVIOUR_FUNCTIONAL


class TestBehaviour(unittest.TestCase):

    layer = CGEO_BEHAVIOUR_FUNCTIONAL

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_custom_styles_indexer(self):
        obj = createContentInContainer(
            self.portal,
            'dexterity_content_with_geo_behaviour',
            title=u"Text object",
            use_custom_styles=True,
        )
        obj.reindexObject()
        pc = getToolByName(self.portal, 'portal_catalog')
        brain = pc.search({'UID': obj.UID()})[0]
        styles = brain.collective_geo_styles

        self.assertTrue(isinstance(styles, dict))
        self.assertEqual(styles['use_custom_styles'], True)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBehaviour))
    return suite
