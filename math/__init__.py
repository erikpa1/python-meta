

class AutoIncrementer():
    def __init__(self, startValue = 0, incrementStep: int = 1):
        self._value = startValue
        self._incrementStep = incrementStep

    def __call__(self):
        tmp = self._value
        self._value += self._incrementStep
        return tmp

class AutoDecrementer():
    def __init__(self, startValue = 0, incrementStep: int = 1):
        self._value = startValue
        self._incrementStep = incrementStep

    def __call__(self):
        tmp = self._value
        self._value -= self._incrementStep
        return tmp
