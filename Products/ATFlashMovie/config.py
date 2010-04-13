from Products.CMFCore import permissions    
from Products.Archetypes.public import IntDisplayList

ADD_CONTENT_PERMISSION = permissions.AddPortalContent
PROJECTNAME = "ATFlashMovie"
SKINS_DIR = 'skins'
I18N_DOMAIN = 'ATFlashMovie'

GLOBALS = globals()

SCALE_LIST = IntDisplayList(
    ((200, '200%'),
     (150, '150%'),
     (100, '100%'),
     (75, '75%'),
     (50, '50%'),
     (25, '25%'),
     ))

VIEWLETS = [
    ('viewlet_flash', 'Flash',
     'string:here/viewlet_flash/macros/portlet',
     '', 'View', 'PT:FlashMovie', 1),
    ]
