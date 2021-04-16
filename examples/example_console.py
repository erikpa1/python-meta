from logging import *

LogE << "Test - error log"
LogD << "Test - debug log"
LogW << "Test - warning log"
LogI << "Test - info log"


def StackLog():
    LogE("Stack height test", stackHeight=1)

StackLog()



