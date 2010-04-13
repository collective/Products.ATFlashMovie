from zope.i18nmessageid import MessageFactory

from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory

from config import SKINS_DIR, GLOBALS, PROJECTNAME, ADD_CONTENT_PERMISSION, I18N_DOMAIN

FlashMovieMessageFactory = MessageFactory(I18N_DOMAIN)

registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
    ##Import Types here to register them
    import ATFlashMovie

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)
 
    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)
