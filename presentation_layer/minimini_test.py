from presentation_layer.color import Color
from presentation_layer.print_result import PrintResult
from business_logic_layer.commands import Command


class Option:
    def __init__(self, setting):
        self.command = Command(setting)
        self.print_result = PrintResult()
        self.command_dict = {
            'exec': {
                'description': '入力したコマンドを一つずつ実行',
                'method': self.command.exec,
                'print': self.print_result.exec
            },
            'all': {
                'description': 'テキストファイル内の全てのコマンドを実行',
                'method': self.command.all,
                'print': self.print_result.all
            },
            'show': {
                'description': '全ての実行結果を一覧',
                'method': self.command.show,
                'print': self.print_result.show
            },
            'search': {
                'description': '特定の実行結果となったコマンドを検索',
                'method': self.command.search,
                'print': self.print_result.search
            },
            'anlysis': {
                'description': 'KO/コマンド数を表示',
                'method': self.command.anlysis,
                'print': self.print_result.anlysis
            },
            'create': {
                'description': '実行結果から' + setting.extension + 'ファイルを作成',
                'method': self.command.create,
                'print': self.print_result.create
            },
            'clear': {
                'description': 'ウィンドウのクリア',
                'method': self.command.clear,
                'print': self.print_result.clear
            },
            'exit': {'description': '終了'},
        }

    def __check_choice(self, choice: str):
        for command in self.command_dict.keys():
            if choice == command:
                return True
        return False

    def __print_commands(self):
        max_len = max([len(command) for command in self.command_dict.keys()])
        for key, value in self.command_dict.items():
            Color.print(f" {key:<{max_len + 1}}: {value['description']}",
                        Color.BLUE)

    def __choice_command(self) -> str:
        choice = ''
        exist_flag = False
        while True:
            self.__print_commands()
            choice = input(' コマンドを選択してください: ').lower().strip()
            exist_flag = self.__check_choice(choice)
            if exist_flag:
                break
            else:
                Color.print('無効な値が入力されました', Color.RED)
        return choice

    def test_loop(self):
        self.command.clear()
        while True:
            choice = self.__choice_command()
            if choice == 'exit':
                break
            result = self.command_dict[choice]['method']()
            self.command_dict[choice]['print'](result)
