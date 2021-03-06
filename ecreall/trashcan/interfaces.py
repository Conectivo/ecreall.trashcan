from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ITrashed(Interface):
    pass


class ITrashcanLayer(IDefaultBrowserLayer):
    """Layer when user is in trashcan
    """

class ILayer(Interface):
    """Layer when ecreall.trashcan is installed
    """