
from logging import *

import weakref



class Null():
    """ Null objects always and reliably "do nothing." """

    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self
    def __repr__(self): return "Null()"
    def __nonzero__(self): return 0
    def __bool__ (self): return False

    def __getattr__(self, name): return self
    def __setattr__(self, name, value): return self
    def __delattr__(self, name): return self

    def __eq__(self, other):
        if other is None:
            return True
        return False


class Functor():
    """
    Functor is object which is possible to put to as Ella Delegate
    Advantage of functor is creating inheritance between functions and
    hide guiData
    """
    def __init__(self, _self, variableName):
        setattr(_self, variableName, self)
        self.__self__ = weakref.proxy(_self)
        self.__name__ = variableName

    def __call__(self, *args, **kwargs):
        LogError_FunctionAndLine("Unimplemented functionality")

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



class Command():
    def Do(self):
        pass

    def Undo(self):
        pass


class CommandHistory():
    def __init__(self):
        self._commands = []
        self._actualCommand = -1

    def RegisterCommand(self, command: Command):
        self._commands.append(command)

    def ClearCommnads(self):
        self._commands.clear()

    def GetCommands(self):
        return self._commands

    def GoBack(self):
        pass

    def GoForward(self):
        pass

class MultiObjectHandler():
    def __init__(self):
        self._objects = []

    def __getattr__(self, item):
        values = []
        for i in self._objects:
            values.append(getattr(i, item, None))
        return values

    def __setattr__(self, key, value):
        for i in self._objects:
            setattr(i, key, value)

    def __call__(self, *args, **kwargs):
        for i in self._objects:
            i(i, *args, **kwargs)

