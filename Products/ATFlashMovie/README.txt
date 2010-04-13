Description
===========

This product provides:

* A new content type that stores and displays Adobe Flash movies.
  It autodetects width, height and flash version from swf files.

* A Plone3 portlet to display a Flash movie.

* And a Collage viewlet if this product is installed.


Installation
------------

You can install it via QuickInstaller.


Requirements
------------

Plone 3.0 or later. This version doesn't work with the Plone 2.0,
2.1 and 2.5 series.


Optional Products
-----------------

* SmartColorWidget 1.0.2 or later
  (at this time, use the trunk from SVN: https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/SmartColorWidget/trunk)

* Collage 1.0 or later
  (at this time, use the trunk from SVN: https://svn.plone.org/svn/collective/Collage/trunk)


Integration with Kupu
---------------------

Kupu has some support for embedding Flash objects using ATFlashMovie,
but requires some manual configuration at this time.

1. Install Products.ATFlashMovie from Plone Control Panel.

2. Got to the Resource Types tab in the Kupu configlet.

3. Under the resource ``mediaobject`` add Flash Movie to the selection
   and save.

4. In the action urls table at the bottom of the page, add a new
   entry for the type Flash Movie. The preview may be left blank or be
   the same as the 'normal' image. For 'normal image' you should enter
   ``string:${object_url}/download``. Leave fieldname blank and in the
   'type' field select 'Flash'.

5. Go to the Filter HTML configlet and remove "object" tags filtering
   in "Nasty tags" and "Stripped tags"

Flash movies should now appear in the image drawer and be insertable into
the document.

Using IE the Flash movie will appear in the document and may be edited or
moved as desired. Firefox will not play the movie while you are editing,
so a 'flash placeholder' image is displayed instead: you cannot select it
in Firefox so if you need to delete a Flash movie you will need to include
the image in a slightly larger selection (e.g. spaces before and after)
and delete that.


Credits
=======

* Jean-Charles ROGEZ (jeancharles.rogez@free.fr): Author

* Sergey Volobuev (s_volobuev@phpv.khv.ru): File swfHeaderData.py from CMFFlashMovie

* Christian Schneide (rchristian@daftdog.de): German translation

* Dorneles Tremea (dorneles@tremea.com): Eggification, bugfix 
