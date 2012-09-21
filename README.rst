Introduction
============

This package provides the ability to assign geographical information to
Dexterity-based (``plone.app.dexterity``) content types within Plone and does
so using ``collective.geo.geographer`` and ``collective.z3cform.mapwidget``.  

By applying the behaviour from this package to a Dexterity content type, a
`Coordinates` field becomes available when creating or editing said content.
This allows a user to either look-up coordinates for a place or feature via
geo-coding, draw a geographical feature (such as a point, line or polygon) on a
map, or enter details manually in Well-Known Text (WKT) format.

When stored, this geographical information can be used by the rest of the 
``collective.geo`` set of packages.  For instance, the coordinates can be
displayed on maps against Collections or Folders using ``collective.geo.kml``.

Installation
------------

Add this package into your Plone buildout like so::
    
    [instance]
    recipe = plone.recipe.zope2instance
    ...
    eggs +=
        collective.geo.behaviour

The package provides an auto-entry point so specifying its name under
``zcml`` isn't necessary.

About the behaviour
-------------------

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

Once your type configuration has the behaviour applied, then content objects of
said type will be marked as georeferenceable for ``collective.geo.geographer``.
This is achieved through the marker interface
``collective.geo.geographer.interfaces.IGeoreferenceable``.

Through the web
^^^^^^^^^^^^^^^^

If you are configuring your Dexterity-based type through the web-based
interface, then proceed to edit your content type in the `Dexterity Content
Types` control panel. Under the `Behaviours` tab you will find the
``collective.geo Maps`` behaviour -- select this and save your content type.

Upon adding or editing an object of your content type, you will see the new
field accordingly.

Generic Setup (file system)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you've created a file-system Dexterity type configuration, you need to
specify the relevant interface as a behaviour::
    
    collective.geo.behaviour.interfaces.ICoordinates

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
        </property>
        ...
    </object>
