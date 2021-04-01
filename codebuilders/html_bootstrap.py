from meta.codebuilders.mxml import *
from meta.guiarchitecture import *


class bsNavItem(NavItem):
    def __init__(self, text = ""):
        super().__init__()
        self._text = text
        self._class = "nav-item"
        self._href = "#"
        self._isActive = False

        self._attributes = {}
        self._attributes["class"] = "nav-item"


    def __str__(self):
        builder = XmlBuilder()

        dict = {
            "class" : "nav-link",
            "href" : self._href
        }

        builder.pair_tag("li", XmlBuilder().pair_tag_nnl("a", self._text, **dict), **self._attributes)

        return builder.result

    def _addition(self):
        return ""

class bsNavDropDownItem(bsNavItem):

    def __init__(self, text = "", items = []):
        super().__init__(text)
        self._attributes["class"] = "nav-item dropdown"
        self._items = items

    def __str__(self):
        builder = XmlBuilder()


        items = XmlBuilder()

        for i in self._items:
            items.pair_tag_nnl("a", i, **{"class": "dropdown-item", "href":"#"}).new_line()


        divBuilder = XmlBuilder()
        divBuilder.pair_tag("div", items, **{"class": "dropdown-menu"})

        aDict = {
            "class" : "nav-link dropdown-toggle",
            "href" : self._href,
            "id": "navbardrop",
            "data-toggle" : "dropdown"
        }

        aBuilder = XmlBuilder()
        aBuilder.pair_tag_nnl("a", self._text, **aDict)


        children = XmlBuilder()
        children.text(aBuilder).new_line()
        children.text(divBuilder).new_line()


        builder.pair_tag("li", children, **self._attributes )


        return builder.result



class bsBrand(Element):
    def __init__(self):
        self._text = ""
        self._logo = ""
        self._href = "#"

    def __str__(self):
        return XmlBuilder().pair_tag("a", self._text, **{"href" : self._href})


class bsNavBar(NavBar):

    def __init__(self):
        super().__init__()
        self.skin = "light"
        self.skin = "dark"
        self.brand = None

    def AddBrand(self, brand: bsBrand):
        self.brand = brand

    def __str__(self):
        builder = XmlBuilder()



        items = ""

        i: NavItem
        for i in self._navItems:
            items += "\n" + str(i) + "\n"

        ul = XmlBuilder()
        ul.pair_tag("ul", items, _class = "navbar-nav")

        builder.pair_tag("nav", ul, _class = "navbar navbar-expand-sm bg-" + self.skin + " navbar-" + self.skin)


        return str(builder)



class bsElement(Element):
    def __init__(self):
        self._tag = "div"



class bsHeader3(bsElement):

    def __init__(self, text):
        super(bsHeader3, self).__init__()
        self._tag = "h3"
        self._text = text

    def __str__(self):
        return str(XmlBuilder().pair_tag_nnl(self._tag, self._text).new_line())


class bsParagraph(bsElement):

    def __init__(self, text):
        super(bsParagraph, self).__init__()
        self._tag = "p"
        self._text = text

    def __str__(self):
        return str(XmlBuilder().pair_tag_nnl(self._tag, self._text).new_line())

class bsBreak(bsElement):

    def __str__(self):
        return "<br>\n"

class bsContainer(Container):
    def __init__(self):
        super().__init__()

    def __str__(self):
        builder = XmlBuilder()

        body = ""
        for i in self._items:
            body += str(i) + "\n"

        builder.pair_tag("div", body, **{"class" : "container"})

        return str(builder)


















