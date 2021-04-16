from designpatterns import *

class A():
    def __init__(self):
        self.someBehaviour = Null

    def DoA(self):
        self.someBehaviour.DoSomething()

    def DoB(self):
        self.someBehaviour.DoSomethingElse()

    def DoC(self):
        self.someBehaviour.DoSameThingAsSomething()


class Human():
    def __init__(self):
        self.posX = 0

    def SetPosX(self, value):
        self.posX = value

    def PrintPosition(self):
        LogD("My position is: ", self.posX)

class MoveForwardCommand(Command):

    def __init__(self, who: Human, speed: float):
        self.who = who
        self.speed = speed

    def Do(self):
        self.who.SetPosX(self.who.posX + 1)
        return self

    def Undo(self):
        self.who.SetPosX(self.who.posX - 1)
        return self

human = Human()

move = MoveForwardCommand(human, 1)

history = CommandsHistory()

history.RegisterCommand(move.Do())
history.RegisterCommand(move.Do())

history.GoBack()
history.GoBack()

history = CommandsHistory()

history.RegisterCommand(move)
history.RegisterCommand(move)

history.GoForward()
history.GoForward()

history.GoBack()
history.GoBack()



