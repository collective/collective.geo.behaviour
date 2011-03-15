from zope.interface import alsoProvides
from zope import schema
from plone.directives import form

# from collective.geo.settings.interfaces import \
#             IGeoCustomFeatureStyle as IGeoCustomFeatureStyleBase
from collective.geo.behaviour import MessageFactory as _


class ICoordinates(form.Schema):
    """Add coordinates to content
    """
    # Openlayers issue
    # - openlayers map doesn't work in hidden tab
    # form.fieldset(
    #         'coordinates',
    #         label=_(u'Coordinates'),
    #         fields=('coordinates',),
    #     )

    form.widget(
        coordinates='collective.z3cform.mapwidget.widget.MapFieldWidget')
    coordinates = schema.Text(
            title=_(u"Coordinates"),
            description=_(u"Modify geographical data for this content"),
            required=False,
        )

alsoProvides(ICoordinates, form.IFormFieldProvider)


# class IGeoCustomFeatureStyle(form.Schema, IGeoCustomFeatureStyleBase):
#     form.fieldset(
#             'geo_custom_styles',
#             label=_(u'Custom Styles'),
#             fields=('use_custom_styles',
#                     'linecolor',
#                     'linewidth',
#                     'polygoncolor',
#                     'marker_image',
#                     'marker_image_size',
#                     'display_properties'),
#         )
# 
#     form.widget(
#             linecolor='collective.z3cform.colorpicker.colorpickeralpha.ColorpickerAlphaFieldWidget',
#             polygoncolor='collective.z3cform.colorpicker.colorpickeralpha.ColorpickerAlphaFieldWidget')
# 
# alsoProvides(IGeoCustomFeatureStyle, form.IFormFieldProvider)

