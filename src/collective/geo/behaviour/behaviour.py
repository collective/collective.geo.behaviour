
from Acquisition import ImplicitAcquisitionWrapper
from Acquisition import aq_self

from zope.interface import implementer
from zope.component import queryAdapter

from collective.geo.geographer.interfaces import IGeoreferenced
from collective.geo.geographer.interfaces import IWriteGeoreferenced
from shapely import wkt
from shapely.geometry import shape
from .interfaces import ICoordinates


@implementer(ICoordinates)
class Coordinates(object):
    """Store coordinates with collective.geo.geographer mechanism
    """

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
                return shape(IGeoreferenced(self.context).geo).wkt
            except (ValueError, TypeError, NotImplementedError):
                # context is not a valid shape.
                # create a validator?
                pass
        return u''

    @coordinates.setter
    def coordinates(self, value):
        if value:
            try:
                geom = wkt.loads(value)
            except Exception:
                return
            coords = geom.__geo_interface__
            geo = IWriteGeoreferenced(self.context)
            geo.setGeoInterface(coords['type'], coords['coordinates'])
