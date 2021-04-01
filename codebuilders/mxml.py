
from meta.string import StringBuilder as sb

class XmlBuilder():

    def __init__(self):
        self.result = ""

    def __str__(self):
        return self.result

    def text(self, *content):
        self.result += sb().concat(*content)
        return self

    def pair_tag(self, tag, *args, **kwargs):
        self.result += "\n<" + tag + self.getattributes(**kwargs) + ">\n"
        self.result += sb().concat(*args)
        self.result += "\n</" + tag + ">\n"
        return self

    def pair_tag_nnl(self, tag, *content, **kwargs):
        self.result += "<" + tag + self.getattributes(**kwargs) + ">"
        self.result += sb().concat(*content)
        self.result += "</" + tag + ">"
        return self



    def start_tag(self, tag, **attributes):
        self.result += "<" + tag + self.getattributes(**attributes) + ">"
        return self

    def end_tag(self, tag):
        self.result += "</" + tag + ">"
        return self

    def solo_tag(self, content, **attributes):
        self.result += "<" + content + self.getattributes(**attributes) + ">"
        return self


    def new_line(self):
        self.result += "\n"
        return self

    def getattributes(self, **kwargs):
        result = " "
        if len(kwargs) == 0:
            result = ""

        for key, value in kwargs.items():
            if key == "_class":
                result += "class" + "="
            else:
                result += key + "="

            result += "\"" + str(value) + "\" "

        return result
