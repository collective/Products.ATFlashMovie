from zope.interface import Interface, Attribute


class IFlashMovie(Interface):
    """ A simple type for managing Adobe Flash files """

    width = Attribute('Width of flash movie')
    height = Attribute('Height of flash movie')
    flashversion = Attribute('Version of flash movie')
