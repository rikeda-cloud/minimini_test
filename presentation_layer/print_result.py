import re
from presentation_layer.color import Color


class PrintResult:
    def __init__(self):
        self.accept_exec = [
                'diff_exit_status',
                'diff_stdout',
                'diff_stderr'
        ]
        self.accept_default = [
                'diff_exit_status',
                'diff_stdout',
                'diff_stderr',
                'exit_status',
                'stdout',
                'stderr'
        ]
        self.accept_anlysis = [
                'total_stdout_faild',
                'total_stderr_faild',
                'total_exit_status_faild'
        ]

    def print_data(self, command, data, accept):
        Color.print(f'~~~ {command} ~~~', Color.PURPLE)
        for key, value in data.items():
            if key in accept:
                if re.match('total', key) and value != 0:
                    Color.print_reverce(f'{key} -> {value}', Color.RED)
                elif value == 'KO':
                    Color.print_reverce(f'{key} -> {value}', Color.RED)
                elif value == 'OK':
                    Color.print(f'{key} -> {value}', Color.GREEN)
                else:
                    Color.print(f'{key} -> {value}', Color.CYAN)

    def exec(self, result):
        for command, data in result.items():
            self.print_data(command, data, self.accept_exec)

    def all(self, results):
        for result in results:
            for command, data in result.items():
                self.print_data(command, data, self.accept_exec)

    def search(self, results):
        for result in results:
            for command, data in result.items():
                self.print_data(command, data, self.accept_default)

    def show(self, results):
        for command, result in results.items():
            self.print_data(command, result, self.accept_default)

    def anlysis(self, after_anlysis):
        self.print_data('anlysis', after_anlysis, self.accept_anlysis)

    def create(self, file):
        if file:
            print(f'{file}が作成されました')

    def clear(self, result):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
