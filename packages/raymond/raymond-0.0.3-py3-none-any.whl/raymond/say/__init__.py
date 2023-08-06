class Text:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[39m"
    LIGHT_BLACK_EX = "\033[90m"
    LIGHT_RED_EX = "\033[91m"
    LIGHT_GREEN_EX = "\033[92m"
    LIGHT_YELLOW_EX = "\033[93m"
    LIGHT_BLUE_EX = "\033[94m"
    LIGHT_MAGENTA_EX = "\033[95m"
    LIGHT_CYAN_EX = "\033[96m"
    LIGHT_WHITE_EX = "\033[97m"


class Background:
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    BLUE = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN = "\033[46m"
    WHITE = "\033[47m"
    RESET = "\033[49m"
    LIGHT_BLACK_EX = "\033[100m"
    LIGHT_RED_EX = "\033[101m"
    LIGHT_GREEN_EX = "\033[102m"
    LIGHT_YELLOW_EX = "\033[103m"
    LIGHT_BLUE_EX = "\033[104m"
    LIGHT_MAGENTA_EX = "\033[105m"
    LIGHT_CYAN_EX = "\033[106m"
    LIGHT_WHITE_EX = "\033[107m"


class Style:
    BRIGHT = "\033[1m"
    DIM = "\033[2m"
    NORMAL = "\033[22m"
    RESET_ALL = "\033[0m"


class Raymond:
    """ Utility class to print a welcoming message to std_out

    Available functions are hello and goodbye:

    .. code-block:: python

        from raymond import Raymond
        say = RaymondHello() # or from raymond.time import function_timer
        Raymond().hello()
        Raymond()(":-)")
        Raymond().goodbye()

    """
    def __call__(self, *args, **kwargs):
        """Say custom message!"""
        print(f"{Style.RESET_ALL}{Style.BRIGHT}Message from Raymond {Text.CYAN}'"
              f"{', '.join([str(a) for a in args])} {', '.join([str(k) + ' ' + str(v) for k, v in kwargs.items()])}"
              f"'{Style.RESET_ALL}")
        return self

    def hello(self):
        """Say hello!"""
        print(f"{Style.RESET_ALL}{Style.BRIGHT}Hello from {Text.CYAN}https://raymondt.co.uk!{Style.RESET_ALL}")
        return self

    def goodbye(self):
        """Say goodbye!"""
        print(f"{Style.RESET_ALL}{Style.BRIGHT}Goodbye from {Text.CYAN}https://raymondt.co.uk!{Style.RESET_ALL}")
        return self


def greeting():
    """Completely pointless package to greet a user"""
    Raymond().hello().goodbye()
