# -*- coding: utf-8 -*-
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from ..testing import CGEO_BEHAVIOUR_INTEGRATION


class TestSetup(unittest.TestCase):

    layer = CGEO_BEHAVIOUR_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def test_install(self):
        self.assertTrue(self.qi.isProductInstalled('collective.geo.behaviour'))

    def test_dependencies(self):
        dependencies = [
            'collective.geo.geographer',
            'collective.geo.mapwidget'
        ]
        for i in dependencies:
            self.assertTrue(self.qi.isProductInstalled(i))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
