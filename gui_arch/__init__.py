

class Application():
    pass


class Element():

    def __init__(self):
        self.skin = None

    def SetSkin(self, skinName: str):
        pass


class NavItem(Element):
    def __init__(self):
        self._isActive = False

    def SetActive(self, status = True):
        self._isActive = status


class NavDropItem(Element):
    pass


class NavBarTypes():
    class STANDARD: pass
    class COLLAPSE: pass


class NavBar(Element):

    def __init__(self):
        super().__init__()
        self.type: NavBarTypes = NavBarTypes.STANDARD
        self._navItems: [NavItem] = []

    def AddNavItem(self, item: NavItem) -> NavItem:
        self._navItems.append(item)
        return item

    def SetType(self, type: NavBarTypes):
        self.type = type

class Container(Element):
    def __init__(self):
        super().__init__()
        self._items = []

    def AddItem(self, item):
        self._items.append(item)
        return item