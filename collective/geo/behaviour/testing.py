# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.publisher.browser import TestRequest as baseRequest
from z3c.form.interfaces import IFormLayer

from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.geo.behaviour


CGEO_BEHAVIOUR = PloneWithPackageLayer(
    zcml_package=collective.geo.behaviour,
    zcml_filename='configure.zcml',
    gs_profile_id='collective.geo.behaviour:default',
    name="CGEO_BEHAVIOUR")

CGEO_BEHAVIOUR_INTEGRATION = IntegrationTesting(
    bases=(CGEO_BEHAVIOUR, ),
    name="CGEO_BEHAVIOUR_INTEGRATION")

CGEO_BEHAVIOUR_FUNCTIONAL = FunctionalTesting(
    bases=(CGEO_BEHAVIOUR, ),
    name="CGEO_BEHAVIOUR_FUNCTIONAL")
