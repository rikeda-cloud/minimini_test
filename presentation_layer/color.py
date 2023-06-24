class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    YELLOW = '\033[33m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'
    END = '\033[0m'

    @classmethod
    def print(self, string, color, end='\n'):
        print(color + string + Color.END, end=end)

    @classmethod
    def print_underline(self, string, color, end='\n'):
        print(self.UNDERLINE + color + string + Color.END, end=end)

    @classmethod
    def print_reverce(self, string, color, end='\n'):
        print(self.REVERCE + color + string + Color.END, end=end)


def main():
    Color.print('abc', Color.RED, end='')
    Color.print_underline('abc', Color.RED, end='')
    Color.print_reverce('abc', Color.RED, end='')


if __name__ == '__main__':
    main()
