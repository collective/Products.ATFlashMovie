from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from Products.ATFlashMovie import FlashMovieMessageFactory as _


class IFlashMoviePortlet(IPortletDataProvider):
    """A portlet which shows a Flash Movie"""

    uid = schema.Choice(title=_(u"label_portlet_selection"),
                        description=_(u"help_portlet_selection"),
                        default=u"",
                        required=True,
                        vocabulary="flashmovie.portlet.flashselection")



class SourcesVocabulary(object):
    """Provides vocabulary to IFlashMoviePortlet.uid through ZCML"""

    implements(IVocabularyFactory)

    def __call__(self, context):

        context = getattr(context, 'context', context)
        portal_catalog = getToolByName(context, 'portal_catalog')

        voc = []

        brains = portal_catalog(portal_type='FlashMovie')
        for brain in brains: # Brains
            o = brain.getObject()
            path = '/'.join(o.getPhysicalPath())
            title = "%s (%s)" % (brain.Title, path)
            voc.append(SimpleTerm(o.UID(), title=title))
        return SimpleVocabulary(voc)

SourcesVocabularyFactory = SourcesVocabulary()


class Assignment(base.Assignment):
    implements(IFlashMoviePortlet)

    def __init__(self, uid=''):
        self.uid = uid

    @property
    def title(self):
        return  _(u'heading_portlet')
    
    
class Renderer(base.Renderer):

    render = ZopeTwoPageTemplateFile('portlet.pt')

    def getContext(self):
        """ Returns the target Object for portlet """
        
        context = aq_inner(self.context)
        cat = getToolByName(context, 'portal_catalog')
        r = cat(UID=self.data.uid)
        if r:
            return r[0].getObject()
        
        return None
        
        
class AddForm(base.AddForm):
    form_fields = form.Fields(IFlashMoviePortlet)
    label = _(u"add_portlet")
    description = _(u"desc_portlet")

    def create(self, data):
        return Assignment(uid=data.get('uid', ''))


class EditForm(base.EditForm):
    form_fields = form.Fields(IFlashMoviePortlet)
    label = _(u"edit_portlet")
    description = _(u"desc_portlet")
