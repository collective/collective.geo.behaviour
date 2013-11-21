# -*- coding: utf-8 -*-
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from zope.configuration import xmlconfig
from plone.app.testing import TEST_USER_ID
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.testing import z2


class PloneAppCollectiveGeoBehaviour(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.geo.behaviour
        xmlconfig.file(
            'testing.zcml',
            collective.geo.behaviour,
            context=configurationContext
        )
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geo.behaviour:testing')
        portal.acl_users.userFolderAddUser('admin',
                                           'secret',
                                           ['Manager'],
                                           [])
        login(portal, 'admin')
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory(
            "Folder",
            id="acceptance-test-folder",
            title=u"Test Folder"
        )


CGEO_BEHAVIOUR = PloneAppCollectiveGeoBehaviour()

CGEO_BEHAVIOUR_INTEGRATION = IntegrationTesting(
    bases=(CGEO_BEHAVIOUR, ),
    name="CGEO_BEHAVIOUR_INTEGRATION")

CGEO_BEHAVIOUR_FUNCTIONAL = FunctionalTesting(
    bases=(CGEO_BEHAVIOUR, ),
    name="CGEO_BEHAVIOUR_FUNCTIONAL")

CGEO_BEHAVIOUR_ROBOT = FunctionalTesting(
    bases=(CGEO_BEHAVIOUR, z2.ZSERVER_FIXTURE),
    name="CGEO_BEHAVIOUR_ROBOT")
