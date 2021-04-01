
from meta.codebuilders.mxml import *
from meta.codebuilders.html_constants import *



class HtmlRequirment():
    def __init__(self):
        self.tag = ""
        self.rel = "stylesheet"
        self.href = ""

class HtmlHeader():
    def __init__(self):
        self._title = ""
        self._requirments = []

    def __str__(self):
        return self.ToString()

    def AddBootstrapRequirment(self):
        self.AddRequirment(HtmlConstants.link, HtmlConstants.stylesheet, Libraries.boostrap_css_4_5_2)
        self.AddRequirment(HtmlConstants.script, HtmlConstants.stylesheet, Libraries.boostrap_js_4_5_2)

    def AddRequirment(self,tag: str, rel: str, href: str):
        tmp = HtmlRequirment()
        tmp.tag = tag
        tmp.rel = rel
        tmp.href = href
        self._requirments.append(tmp)

    def ToString(self):
        builder = XmlBuilder()
        builder.start_tag("head").new_line()

        builder.solo_tag("meta", charset="utf-8")
        builder.pair_tag_nnl("title", self._title) .new_line()


        i: HtmlRequirment
        for i in self._requirments:
            builder.pair_tag(i.tag, rel=i.rel, href=i.href)


        builder.new_line()
        builder.end_tag("head").new_line()

        return builder.result

    def __str__(self):
        return self.ToString()

class HtmlBody():
    def __init__(self):
        self._nodes = []

    def __str__(self):
        return self.ToString()

    def AddNode(self, node):
        self._nodes.append(node)
        return node

    def ToString(self):
        builder = XmlBuilder()
        builder.start_tag("body").new_line()

        for i in self._nodes:
            builder.text(str(i)).new_line()

        builder.new_line()


        builder.end_tag("body")

        return builder.result

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
        builder = XmlBuilder()
        builder.solo_tag("!DOCTYPE html").new_line()
        builder.start_tag("html", lang=self._htmlLang).new_line()

        builder.text(str(self._head)).new_line()
        builder.text(str(self._body)).new_line()
        builder.end_tag("html").new_line()


        return builder.result




    pass