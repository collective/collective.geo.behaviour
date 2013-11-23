
from Acquisition import ImplicitAcquisitionWrapper
from Acquisition import aq_self

from zope.interface import implements
from zope.component import queryAdapter

from collective.geo.geographer.interfaces import IGeoreferenced
from collective.geo.geographer.interfaces import IWriteGeoreferenced

from .interfaces import ICoordinates


class Coordinates(object):
    """Store coordinates with collective.geo.geographer mechanism
    """
    implements(ICoordinates)

    use_custom_styles = 0

    def __init__(self, context):
        # dewrap context when a Dexterity object is added
        if isinstance(context, ImplicitAcquisitionWrapper):
            context = aq_self(context)
        self.context = context

    @property
    def coordinates(self):
        geo_adapter = queryAdapter(self.context, IGeoreferenced)
        if geo_adapter:
            try:
                from shapely.geometry.geo import asShape
            except ImportError:
                from pygeoif.geometry import as_shape as asShape
            try:
                return asShape(IGeoreferenced(self.context).geo).wkt
            except (ValueError, TypeError, NotImplementedError):
                # context is not a valid shape.
                # create a validator?
                pass
        return u''

    @coordinates.setter
    def coordinates(self, value):
        if value:
            try:
                from shapely import wkt
                geom = wkt.loads(value)
            except ImportError:
                from pygeoif.geometry import from_wkt
                geom = from_wkt(value)
            coords = geom.__geo_interface__
            geo = IWriteGeoreferenced(self.context)
            geo.setGeoInterface(coords['type'], coords['coordinates'])

    # TODO: Implement quite simple setter and getter for follow group fields
    #        - use_custom_styles
    #        - marker_image
    #        - map_viewlet_position
    #        - marker_image_size
    #        - map_width
    #        - linecolor
    #        - map_height
    #        - polygoncolor
    #        - display_properties
    #        - linewidth

    @property
    def use_custom_styles(self):
        return self.context.use_custom_styles

    @use_custom_styles.setter
    def use_custom_styles(self, value):
        self.context.use_custom_styles = value

    @property
    def marker_image(self):
        return self.context.marker_image or self.marker_image

    @marker_image.setter
    def marker_image(self, value):
        self.context.marker_image = value

    @property
    def map_viewlet_position(self):
        return self.context.map_viewlet_position or self.map_viewlet_position

    @map_viewlet_position.setter
    def map_viewlet_position(self, value):
        self.context.map_viewlet_position = value

    @property
    def marker_image_size(self):
        return self.context.marker_image_size or self.marker_image_size

    @marker_image_size.setter
    def marker_image_size(self, value):
        self.context.marker_image_size = value

    @property
    def map_width(self):
        return self.context.map_width or None

    @map_width.setter
    def map_width(self, value):
        self.context.map_width = value

    @property
    def linecolor(self):
        return self.context.linecolor or self.linecolor

    @linecolor.setter
    def linecolor(self, value):
        self.context.linecolor = value

    @property
    def map_height(self):
        return self.context.map_height or None

    @map_height.setter
    def map_height(self, value):
        self.context.map_height = value

    @property
    def polygoncolor(self):
        return self.context.polygoncolor or self.polygoncolor

    @polygoncolor.setter
    def polygoncolor(self, value):
        self.context.polygoncolor = value

    @property
    def display_properties(self):
        return self.context.display_properties or self.display_properties

    @display_properties.setter
    def display_properties(self, value):
        self.context.display_properties = value

    @property
    def linewidth(self):
        return self.context.linewidth or self.linewidth

    @linewidth.setter
    def linewidth(self, value):
        self.context.linewidth = value
