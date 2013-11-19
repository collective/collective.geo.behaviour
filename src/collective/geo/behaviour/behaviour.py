
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
