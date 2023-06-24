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

    def print_data(self, command, data, accept):
        Color.print(f'~~~ {command} ~~~', Color.PURPLE)
        for key, value in data.items():
            if key in accept:
                if value == 'KO':
                    Color.print_reverce(f'{key} -> {value}', Color.RED)
                elif value == 'OK':
                    Color.print(f'{key} -> {value}', Color.GREEN)
                else:
                    Color.print(f'{key} -> {value}', Color.CYAN)

                    

    def search(self, results):
        for result in results:
            for command, data in result.items():
                self.print_data(command, data, self.accept_default)

    def exec(self, result):
        for command, data in result.items():
            self.print_data(command, data, self.accept_exec)

    def exec_all(self, results):
        for result in results:
            for command, data in result.items():
                self.print_data(command, data, self.accept_exec)

    def show(self, results):
        for command, result in results.items():
            if isinstance(result, dict):
                self.print_data(command, result, self.accept_default)
            else:
                Color.print_reverce(f'{command} {result}', Color.WHITE)

    def clear(self, result):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
