"""
 Additionnal setup
"""

from Products.CMFCore.utils import getToolByName


def setupMimetypesRegistry(context):
    """
    Setup MimetypesRegistry with new icon.
    """

    site = context.getSite()
    mtr = getToolByName(site, 'mimetypes_registry')
    
    mtr.manage_editMimeType('application/x-shockwave-flash', 'Shockwave Flash file', 'application/x-shockwave-flash', ('swf', 'swfl'), 'video.png', binary=True, globs='*.swf')

    return 'Shockwave Flash mimetypes updated in MimetypesRegistry.'
