from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.CMFCore import permissions    
from Products.Archetypes.public import *
from Products.ATContentTypes.content.file import ATFile, ATFileSchema

try:
    from Products.SmartColorWidget.Widget import SmartColorWidget as ColorWidget
except ImportError:
    ColorWidget = StringWidget

from interfaces import IFlashMovie
from swfHeaderData import analyseContent
from config import SCALE_LIST, PROJECTNAME

schema = ATFileSchema + Schema((

    IntegerField('scale',
                 required = True,
                 searchable = False,
                 default = 100,
                 validators = ('isInt'),
                 vocabulary = SCALE_LIST,
                 widget=SelectionWidget(label = 'Scale',
                                        label_msgid ='label_scale',
                                        description = 'Scale of the flash movie.',
                                        description_msgid ="desc_scale",
                                        i18n_domain='ATFlashMovie'),
                 ),

    StringField('bgcolor',
                 required = True,
                 searchable = False,
                 default = '#FFFFFF',
                 widget=ColorWidget(label = 'Background Color',
                                    label_msgid ='label_bgcolor',
                                    description = 'Select background color of the flash movie.',
                                    description_msgid ="desc_bgcolor",
                                    i18n_domain='ATFlashMovie'),
                ),
    BooleanField('technical_info',
                 searchable = False,
                 default = False,
                 widget= BooleanWidget(label = 'Show technical informations',
                                    label_msgid ='label_technical_info',
                                    description = 'Check to display technical informations about the flash movie.',
                                    description_msgid ="desc_technical_info",
                                    i18n_domain='ATFlashMovie'),
                ),
    
    ))


class ATFlashMovie(ATFile):

    implements(IFlashMovie)

    schema = schema

    portal_type = 'FlashMovie'
    archetype_name = 'FlashMovie'
    assocFileExt   = ('swf',)
    assocMimetypes = ('application/x-shockwave-flash',)
    inlineMimetypes = ('application/x-shockwave-flash',)

    _at_rename_after_creation = True
    
    security = ClassSecurityInfo()

    security.declareProtected(permissions.ModifyPortalContent, 'setFile')
    def setFile(self, value, **kwargs):
        """Saves file and stores flash informations (size, flash version)"""
        ATFile.setFile(self, value, **kwargs)
        data_sample = str(self.getFile())[:1024]
        if len(data_sample):
            tags = analyseContent(data_sample)
            self.width = tags['width']
            self.height = tags['height']
            self.flashversion = tags['flashversion']

registerType(ATFlashMovie, PROJECTNAME)
