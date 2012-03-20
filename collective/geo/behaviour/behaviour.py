from shapely import wkt
from shapely.geometry.geo import asShape

from rwproperty import getproperty, setproperty

from zope.interface import implements
from zope.component import queryAdapter

from collective.geo.geographer.interfaces import IGeoreferenced
from collective.geo.geographer.interfaces import IWriteGeoreferenced
# from interfaces import IGeoCustomFeatureStyle
from interfaces import ICoordinates


class Coordinates(object):
    """Store coordinates with collective.geo.geographer mechanism
    """
    implements(ICoordinates)

    def __init__(self, context):
        self.context = context

    @getproperty
    def coordinates(self):
        geo_adapter = queryAdapter(self.context, IGeoreferenced)
        if geo_adapter:
            try:
                return asShape(IGeoreferenced(self.context).geo).wkt
            except ValueError:
                # context is not a valid shape.
                # create a validator?
                pass
        return u''

    @setproperty
    def coordinates(self, value):
        if not value:
            return
        coords = wkt.loads(value).__geo_interface__
        geo = IWriteGeoreferenced(self.context)
        geo.setGeoInterface(coords['type'], coords['coordinates'])



# class GeoCustomFeatureStyle(object):
#     implements(IGeoCustomFeatureStyle)
#
#     def __init__(self, context):
#         self.context = context
#
#     use_custom_styles = True
#     linecolor = u'ff00003c'
#     linewidth = 2.0
#     polygoncolor = u'ff00003c'
#     marker_image = u'string:${portal_url}/img/marker.png',
#     marker_image_size = 0.7
#     display_properties =  ['Title', 'Description']
