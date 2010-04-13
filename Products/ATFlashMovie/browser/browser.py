from Products.Five import BrowserView
try:
    from Products.Collage.browser.views import BaseView
    class CollageStandardView(BaseView):
        title = u'Standard'

    class CollagePortletView(BaseView):
        title = u'Portlet'

except ImportError:
    pass
    

class flashMovieView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
    

    def getDisplayHeight(self):
        """Returns height in pixels for selected scale"""
        if self.context.height:
            return int(self.context.height * (self.context.getScale() / 100.0))
        else:
            return None
    
    def getDisplayWidth(self):
        """Returns width in pixels for selected scale"""
        if self.context.width:
            return int(self.context.width * (self.context.getScale() / 100.0))
        else:
            return None
