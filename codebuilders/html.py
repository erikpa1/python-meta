import xml.etree.ElementTree as et
from xml.dom import minidom

from meta.codebuilders.mxml import *
from meta.codebuilders.html_constants import *




class HtmlHeader():
    def __init__(self):
        self._title = ""
        self._requirments = []
        self._metas = []
        self._metas.append({"charset": "utf-8"})

    def SetTitle(self, title: str):
        self._title = title

    def AddBootstrapRequirment(self):
        self._metas.append({"name": "viewport", "content": "width=device-width, initial-scale=1"})

        data = {}
        data["rel"] = HtmlConstants.stylesheet
        data["href"] = Libraries.boostrap_css_4_5_2
        self.AddRequirment(HtmlConstants.link, data)

        data = {}
        data["src"] = Libraries.boostrap_js_4_5_2
        self.AddRequirment(HtmlConstants.script, data, " ")

        data = {}
        data["src"] = Libraries.jquery_3_5_1
        self.AddRequirment(HtmlConstants.script, data, " ")

        data = {}
        data["src"] = Libraries.popper_1_16_0
        self.AddRequirment(HtmlConstants.script, data, " ")


    def AddRequirment(self, tag, data: {}, body = ""):
        self._requirments.append((tag, data, body))



    def FillTree(self, tree: et.Element):
        headElement = et.SubElement(tree, "head")

        titleElement = et.SubElement(headElement, "title")
        titleElement.text = self._title

        i: {}
        for i in self._metas:
            et.SubElement(headElement, "meta", i)

        for i in self._requirments:
            dependency = et.SubElement(headElement, i[0], i[1])
            dependency.text = i[2]





class HtmlBody():
    def __init__(self):
        self._nodes = []

    def AddNode(self, node):
        self._nodes.append(node)
        return node

    def FillTree(self, tree: et.Element):
        bodyElement = et.SubElement(tree, "body")

        for i in self._nodes:
            i.FillTree(bodyElement)


class HtmlDocument():

    def __init__(self):
        self._htmlLang = "en"
        self._head = HtmlHeader()
        self._body = HtmlBody()

    @property
    def head(self) -> HtmlHeader:
        return self._head

    @property
    def body(self) -> HtmlBody:
        return self._body

    def __str__(self):
        return self.ToString()


    def ToString(self):

        htmlTags = {"lang" : self._htmlLang}

        root: et.Element = et.Element("html", htmlTags)

        self._head.FillTree(root)
        self._body.FillTree(root)

        result = "<!DOCTYPE html>\n"
        treeResult = et.tostring(root)
        treeResult =  minidom.parseString(treeResult).toprettyxml(indent=" " * 4)

        result += treeResult.replace('b\'', '')


        return result



    pass