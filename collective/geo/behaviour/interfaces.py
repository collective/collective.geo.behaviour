from zope import schema
from zope.interface import alsoProvides
from plone.directives import form

from collective.z3cform.colorpicker import colorpickeralpha
from collective.z3cform.mapwidget.widget import MapFieldWidget
from collective.geo.settings.interfaces import IGeoCustomFeatureStyle
from collective.geo.settings.config import GEO_STYLE_FIELDS
from collective.geo.behaviour import MessageFactory as _


class ICoordinates(form.Schema, IGeoCustomFeatureStyle):
    """Add coordinates and map styles to content
    """

    coordinates = schema.Text(
        title=_(u"Coordinates"),
        description=_(u"Modify geographical data for this content"),
        required=False,
    )

    form.widget(
        coordinates=MapFieldWidget,
        linecolor=colorpickeralpha.ColorpickerAlphaFieldWidget,
        polygoncolor=colorpickeralpha.ColorpickerAlphaFieldWidget
    )

    form.fieldset(
        'coordinates',
        label=_(u'Coordinates'),
        fields=('coordinates', )
    )

    form.fieldset(
        'geo_custom_styles',
        label=_(u'Custom map styles'),
        fields=GEO_STYLE_FIELDS
    )

alsoProvides(ICoordinates, form.IFormFieldProvider)
