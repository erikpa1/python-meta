


class PythonType:
    def __init__(self, keyWord: str, value: str, leftSurrounding = "", rightSurrounding = ""):
        self.keyWord = keyWord
        self.value = value
        self.surroundings_l = leftSurrounding
        self.surroundings_r = rightSurrounding

    def GetFormatedValue(self):
        result = self.surroundings_l + str(self.value) + self.surroundings_r
        return result

    def GetFormatedKeyWord(self):
        if self.keyWord == "":
            return ""
        else:
            return ": " + self.keyWord

    """
    Pri doplnani niecoho do konstruktora netreba zabudnut na toto
    """
    def __call__(self, defaultValue = ""):
        copy = PythonType(self.keyWord, defaultValue, self.surroundings_l, self.surroundings_r)
        return copy


class PythonTypes:
    String = PythonType("str", "", "\"", "\"")
    Int = PythonType("int", 0)
    Float = PythonType("float", 0)
    Bool = PythonType("bool", False)
    Array = PythonType("{}", {}, "{", "}")

class PythonAttribute():
    def __init__(self, attributeName, attributeType: PythonType = None):
        self.attrName = attributeName
        self.attrType = attributeType

class PythonMethod():
    def __init__(self, methodName, parameters = [], returnType: PythonType = None):
        self.name = methodName
        self.parameters = parameters,
        self.returnType = returnType

class PythonClass():
    def __init__(self, className: str):
        self.name = className

        self._attributes = {}
        self._subClasses = {}
        self._methods = {}


    def AddSubClass(self, subclassaName):
        tmp =  PythonClass(subclassaName)
        self._subClasses[subclassaName] = tmp
        return tmp

    def AddMethod(self, methodName, parameters = [], returnType: PythonType = None):
        self._methods[methodName] = PythonMethod(methodName, parameters, returnType)

    def AddAttribute(self, attributeName, attributeType = None):
        self._attributes[attributeName] = PythonAttribute(attributeName, attributeType)


class SimplePythonClassGenerator():

    def __init__(self, className, indendantion = 0):
        self._class = PythonClass(className)
        self.indendantion = indendantion
        self._builder = StringBuilder()


    def AttributesIndent(self):
        return self.indendantion + 1

    def RootClass(self):
        return self._class

    def Compile(self):

        builder = self._builder
        builder.tab(self.indendantion).text("class ", self._class.name, ":").new_line()

        root = self._class

        key: PythonClass
        for key, claz in self._class._subClasses.items():
            subGenerator = SimplePythonClassGenerator(key, self.AttributesIndent())
            subGenerator._class = claz
            subGenerator.Compile()
            builder.text(subGenerator.ToString())
            builder.new_line()

        j: PythonAttribute
        for name, attribute in self._class._attributes.items():
            builder.tab(self.AttributesIndent())
            builder.text(name, attribute.attrType.GetFormatedKeyWord(), " = ", attribute.attrType.GetFormatedValue())
            builder.new_line()

        k: PythonMethod
        for k in self._class._methods.values():
            builder.tab(self.AttributesIndent())
            builder.text(k.name, k.returnType)
            builder.new_line()

        builder.tab(self.AttributesIndent()).text("pass").new_line()


    def ToString(self):
        return self._builder.GetResult()

