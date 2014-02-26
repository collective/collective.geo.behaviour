Introduction
============

This package provides the ability to assign geographical information to
Dexterity-based (``plone.app.dexterity``) content types within Plone and does
so using `collective.geo.geographer`_ and `collective.geo.mapwidget`_.

By applying the behaviour *Collective Geo Maps* to a Dexterity content type, a
`Coordinates` field becomes available when creating or editing said content.

This allows a user to either look-up coordinates for a place or feature via
geo-coding, draw a geographical feature (such as a point, line or polygon) on a
map, or enter details manually in Well-Known Text (`WKT`_) format.

Collective.geo.behaviour also provides *Collective Geo Styles* behaviour.
By this behaviour it is possible to customize the style of the features
that will be displayed on the map for each content type.

Geographical information can be used by the rest of the ``collective.geo``
set of packages.  For instance, the coordinates can be displayed on maps against Collections or Folders using `collective.geo.kml`_.


Found a bug? Please, use the `issue tracker`_.

.. contents:: Table of contents


Installation
============

This addon can be installed has any other addons, please follow official
documentation_.


About the Maps behaviour
------------------------

The behaviour adds a ``coordinates`` field to the content type and uses a
``collective.z3cform.mapwidget`` widget in order to allow the user to
manipulate the geographic information.

The behaviour effectively acts as a proxy to load and save the data into the
relevant location by querying for an
``collective.geo.geographer.interfaces.IGeoreferenced`` adapter and
``collective.geo.geographer.interfaces.IWriteGeoreferenced`` respectively for
the given context.

This means that changes made upon as edits to the content object and changes
made in the `Coordinates` tab are both modifying exactly the same data.

Usage
-----

Once your type configuration has the *Collective Geo Maps* behaviour applied, then content objects of said type will be marked as georeferenceable for ``collective.geo.geographer``.
This is achieved through the marker interface
``collective.geo.geographer.interfaces.IGeoreferenceable``.


Through the web
^^^^^^^^^^^^^^^^

If you are configuring your Dexterity-based type through the web-based
interface, then proceed to edit your content type in the `Dexterity Content
Types` control panel. Under the `Behaviours` tab you will find the
``Collective Geo Maps`` behaviour -- select this and save your content type.

In the same way you could choose *Collective Geo Styles* in order to assing
the other behaviour.

Upon adding or editing an object of your content type, you will see the new
field accordingly.


Generic Setup (file system)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you've created a file-system Dexterity type configuration, you need to
specify the relevant interfaces as a behaviour::

    collective.geo.behaviour.interfaces.ICoordinates
    collective.geo.behaviour.interfaces.IGeoFeatureStyle

and import or re-import your type configuration.  As an example, a type
configuration at ``${product_dir}/profiles/default/types/my.datatype.xml``
would look like this::

    <?xml version="1.0"?>
    <object name="my.datatype"
       meta_type="Dexterity FTI"
       i18n:domain="tdh.metadata" xmlns:i18n="http://xml.zope.org/namespaces/i18n">
        ...
        <property name="behaviors">
          <element value="collective.geo.behaviour.interfaces.ICoordinates" />
          <element value="collective.geo.behaviour.interfaces.IGeoFeatureStyle" />
        </property>
        ...
    </object>

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
.. _issue tracker: https://github.com/collective/collective.geo.bundle/issues
.. _Plone: http://plone.org
.. _collective.geo.mapwidget: http://pypi.python.org/pypi/collective.geo.mapwidget
.. _collective.geo.geographer: http://pypi.python.org/pypi/collective.geo.geographer
.. _collective.geo.kml: http://pypi.python.org/pypi/collective.geo.kml
.. _WKT: http://en.wikipedia.org/wiki/Well-known_text
