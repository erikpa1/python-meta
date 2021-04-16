from inspect import getframeinfo
from inspect import stack
import traceback

console_end = '\033[0m'
console_red = '\033[91m'
console_blue = '\033[94m'
console_warning = '\u001b[35m'


def __print_format_stack(stackHeight=1, *args, **kwargs):
    caller = getframeinfo(stack()[stackHeight][0])
    print("File \"" + str(caller.filename) + "\", line " + str(caller.lineno) + ": ", *args, **kwargs)


def __print_err(stackHeight, *args, **kwargs):
    print(console_red, end="")
    __print_format_stack(stackHeight, *args, **kwargs)
    print(console_end, end="")


def __print_warn(stackHeight, *args, **kwargs):
    print(console_warning, end="")
    __print_format_stack(stackHeight, *args, **kwargs)
    print(console_end, end="")


def __print_debug(stackHeight, *args, **kwargs):
    print(console_blue, end="")
    __print_format_stack(stackHeight, *args, **kwargs)
    print(console_end, end="")


def __print_info(stackHeight, *args, **kwargs):
    __print_format_stack(stackHeight, *args, **kwargs)


class Logger():

    def __init__(self, function):
        self._function = function

    def __lshift__(self, *args, **kwargs):
        self._function(kwargs.pop("stackHeight", 0) + 3, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        :param stackHeight: height of stack
        """
        self._function(kwargs.pop("stackHeight", 0) + 3, *args, **kwargs)

LogE = Logger(__print_err)
LogW = Logger(__print_warn)
LogD = Logger(__print_debug)
LogI = Logger(__print_info)



