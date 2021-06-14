import xml.etree.ElementTree as et

from logging import *

import gui_arch


class Skins(gui_arch.Skins):
    dark = "dark"
    white = "white"


class FontSkin(gui_arch.FontSkin):
    dark = "dark"
    white = "white"


class NavItem(gui_arch.NavItem):
    def __init__(self, text=""):
        super().__init__()
        self._text = text
        self._class = "nav-item"
        self._href = "#"
        self._isActive = False

        self._attributes = {}
        self._attributes["class"] = "nav-item"

    def FillTree(self, tree: et.Element):
        dict = {
            "class": "nav-link",
            "href": self._href
        }

        if self._isActive:
            self._attributes["class"] = "nav-item active"

        liElement = et.SubElement(tree, "li", self._attributes)

        aElement = et.SubElement(liElement, "a", dict)
        aElement.text = self._text


class NavDropDownItem(NavItem):

    def __init__(self, text="", items=[]):
        super().__init__(text)
        self._attributes["class"] = "nav-item dropdown"
        self._items = items

    def FillTree(self, tree: et.Element):
        liElement = et.SubElement(tree, "li", self._attributes)

        aDict = {
            "class": "nav-link dropdown-toggle",
            "href": self._href,
            "id": "navbardrop",
            "data-toggle": "dropdown"
        }

        activeElement = et.SubElement(liElement, "a", aDict)
        activeElement.text = self._text
        divElement = et.SubElement(liElement, "div", {"class": "dropdown-menu"})

        for i in self._items:
            aElement = et.SubElement(divElement, "a", {"class": "dropdown-item", "href": "#"})


class Brand(gui_arch.Element):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._attributes = {}
        self._attributes["class"] = "navbar-brand"
        self._attributes["href"] = "#"

    def FillTree(self, tree: et.Element):
        a = et.SubElement(tree, "a", self._attributes)
        a.text = self._text


class NavBar(gui_arch.NavBar):

    def __init__(self):
        super().__init__()
        # self.skin = "light"
        self.navbar_skin = "dark"
        self.bg_skin = "dark"
        self.brand = None

    def SetSkin(self, skinName: str):
        self.bg_skin = skinName
        self.navbar_skin = skinName

    def AddBrand(self, brand: Brand):
        self.brand = brand

    def FillTree(self, tree: et.Element):
        if self.type == gui_arch.NavBarTypes.STANDARD:
            self._FillStandardType(tree)
        elif self.type == gui_arch.NavBarTypes.COLLAPSE:
            LogE << "Unimplemented" + "https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_navbar_collapse"
        else:
            LogE << "Totally unimplemented"

    def _FillStandardType(self, tree: et.Element):
        nav = et.SubElement(tree, "nav",
                            {"class": "navbar navbar-expand-sm bg-" + self.bg_skin + " navbar-" + self.navbar_skin})

        ul = et.SubElement(nav, "ul", {"class": "navbar-nav"})
        i: NavItem
        for i in self._navItems:
            i.FillTree(ul)


class Element(gui_arch.Element):
    def __init__(self):
        self._tag = "div"


class Header1(gui_arch.Element):

    def __init__(self, text):
        super().__init__()
        self._tag = "h1"
        self._text = text

    def FillTree(self, tree: et.Element):
        et.SubElement(tree, self._tag).text = self._text

class Header2(gui_arch.Element):

    def __init__(self, text):
        super().__init__()
        self._tag = "h2"
        self._text = text

    def FillTree(self, tree: et.Element):
        et.SubElement(tree, self._tag).text = self._text

class Header3(gui_arch.Element):

    def __init__(self, text):
        super().__init__()
        self._tag = "h3"
        self._text = text

    def FillTree(self, tree: et.Element):
        et.SubElement(tree, self._tag).text = self._text

class Paragraph(gui_arch.Element):

    def __init__(self, text):
        super().__init__()
        self._tag = "p"
        self._text = text

    def FillTree(self, tree: et.Element):
        et.SubElement(tree, self._tag).text = self._text



class Container(gui_arch.Container):
    def __init__(self):
        super().__init__()
        self._attributes = {}
        self._attributes["class"] = "container"
        self.fluidEnabled = False
        self.borderEnabled = False
        self.topPadding = 0
        self.fontSkin = None


    def FillTree(self, tree: et.Element):
        self._Bake()
        div = et.SubElement(tree, "div", self._attributes)

        i: Element
        for i in self._items:
            i.FillTree(div)

    def _Bake(self):
        base = "container"

        if self.fluidEnabled:
            base += "-fluid"

        if self.borderEnabled:
            base += " border"

        if self.skin:
            base += " bg-" + self.skin

        if self.fontSkin:
            base += " text-" + self.fontSkin

        base += " pt-" + str(self.topPadding)

        self._attributes["class"] = base

class TableView(Container):

    def __init__(self):
        super().__init__()
        self._attr = {}
        self._attr["class"] = "table table-striped"
        self.hoverEnabled = False
        self.isBorderLess = False

        #TODO farby jednotlivych columnov https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_table_contextual&stacked=h
        #TODO skin headru https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_table_head&stacked=h
        #TODO small table https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_table_sm&stacked=h
        #TODO responsible https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_table_responsive

    def FillTree(self, tree: et.Element):

        div = et.SubElement(tree, "table", self._attributes)

        thead = et.SubElement(div, "thead", {})
        tr = et.SubElement(thead, "tr", {})

        items = ["Name", "Surname", "Age"]

        for i in items:
            et.SubElement(tr, "th", {}).text = i

        tbody = et.SubElement(div, "tbody", {})

        items = [
            ["Erik", "Palencik", "21"],
            ["Peter", "Maly", "45"],
            ["Lukas", "Treti", "33"]
            ]

        for i in items:
            tr = et.SubElement(tbody, "tr", {})

            for j in i:
                et.SubElement(tr, "td", {}).text = j
