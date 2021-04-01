

class AlphabetArray:

    @staticmethod
    def GetBigLetterOnIndex(index: int):
        #TODO toto este upravit aby to slo aj od -1 a pod a aby to dobre pretekalo
        min = 65
        max = 91
        actualValue = (min + index) % max
        return str(chr(actualValue))

    @staticmethod
    def GetSmallLetterOnIndex(index: int):
        #TODO toto este upravit aby to slo aj od -1 a pod a aby to dobre pretekalo
        min = 97
        max = 122
        actualValue = (min + index) % max
        return str(chr(actualValue))



class StringBuilder:

    def __init__(self):
        self._result = ""
        self.spacing = ""

    def GetResult(self):
        return self._result

    def text(self, *values):
        self._result += self.concat(*values)
        return self

    def new_line(self):
        self._result += "\n"
        return self

    def tab(self, tabLevel = 1):
        self._result += "\t" * tabLevel
        return self

    def concat(self, *values):
        tmp: str = ""
        for value in values:
            tmp += str(value)
        return tmp

