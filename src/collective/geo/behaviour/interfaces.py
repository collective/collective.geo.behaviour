from zope.interface import alsoProvides
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model

from collective.z3cform.colorpicker import colorpickeralpha
from collective.z3cform.mapwidget import WKT
from collective.geo.settings.interfaces import IGeoCustomFeatureStyle
from collective.geo.settings.config import GEO_STYLE_FIELDS
from collective.geo.behaviour import MessageFactory as _


class ICoordinates(model.Schema):
    """Add coordinates and map styles to content
    """

    coordinates = WKT(
        title=_(u"Coordinates"),
        description=_(u"Modify geographical data for this content"),
        required=False,
    )

    model.fieldset(
        'coordinates',
        label=_(u'Coordinates'),
        fields=('coordinates', )
    )


alsoProvides(ICoordinates, IFormFieldProvider)


class IGeoFeatureStyle(model.Schema, IGeoCustomFeatureStyle):

    form.widget(
        linecolor=colorpickeralpha.ColorpickerAlphaFieldWidget,
        polygoncolor=colorpickeralpha.ColorpickerAlphaFieldWidget
    )

    model.fieldset(
        'coordinates',
        label=_(u'Coordinates'),
        fields=GEO_STYLE_FIELDS
    )

alsoProvides(IGeoFeatureStyle, IFormFieldProvider)
