from weakref import proxy, WeakMethod

class PropertyParent():

    def __init__(self):
        self._value = None
        self.onValueChanged = []
        self.onValueChangedWeak = []
        self.name = ""
        self.langName = ""
        self.description = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

        for i in self.onValueChanged:
            i()
        for i in self.onValueChangedWeak:
            i()()

class propFloat(PropertyParent):
    def __init__(self, value: float = 0):
        super().__init__()
        self._value: float = value
        self.minValue = None
        self.maxValue = None
