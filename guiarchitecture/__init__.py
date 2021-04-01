

class Application():
    pass


class Element():
    pass


class NavItem(Element):
    pass

class NavDropItem(Element):
    pass


class NavBar(Element):

    def __init__(self):
        super().__init__()
        self._navItems: [NavItem] = []

    def AddNavItem(self, item: NavItem):
        self._navItems.append(item)

class Container(Element):
    def __init__(self):
        self._items = []

    def AddItem(self, item):
        self._items.append(item)
        return item