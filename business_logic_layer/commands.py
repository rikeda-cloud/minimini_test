import os
import subprocess
from persistence_layer.log import Log
from presentation_layer.color import Color


BASH = 'bash'
BASH_PATH = '/bin/bash'
MINISHELL = 'minishell'
MINISHELL_PATH = './minishell'
DEFAULT_COMMAND_PATH = './default_command.txt'


def diff(data1, data2):
    return 'OK' if data1 == data2 else 'KO'


def exec_command_line(command_line: str, shell_path: str):
    proc = subprocess.run(
                shell_path,
                input=command_line,
                encoding='UTF-8',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
    )
    return proc


def json_sirialize(command_line, proc1, proc2):
    nest_result = {}
    result_dict = {}
    result_dict['diff_exit_status'] = diff(proc1.returncode, proc2.returncode)
    result_dict['diff_stdout'] = diff(proc1.stdout, proc2.stdout)
    result_dict['diff_stderr'] = diff(proc1.stderr, proc2.stderr)
    result_dict['exit_status'] = {BASH: proc1.returncode, MINISHELL: proc2.returncode}
    result_dict['stdout'] = {BASH: proc1.stdout, MINISHELL: proc2.stdout}
    result_dict['stderr'] = {BASH: proc1.stderr, MINISHELL: proc2.stderr}
    nest_result[command_line] = result_dict
    return nest_result


def choice_label_and_status():
    labels = ['diff_exit_status', 'diff_stdout', 'diff_stderr']
    [Color.print(f'[{idx + 1}] {label}', Color.BLUE) for idx, label in enumerate(labels)]
    select_idx = -1
    while True:
        try:
            select_idx = int(input('検索したい項目のインデックスを選択してください: '))
            if 0 < select_idx <= len(labels):
                break
            else:
                Color.print('無効な値が入力されました', Color.RED)
        except ValueError:
            select_idx = -1
            Color.print('無効な値が入力されました', Color.RED)
    select_status = input('KOまたはOKを入力(不正な入力の場合、KOが選択されます)').upper()
    select_status = 'OK' if select_status == 'OK' else 'KO'
    return labels[select_idx - 1], select_status


class Command:
    def __init__(self, minishell_prompt):
        self.log = Log()
        self.minishell_prompt = minishell_prompt

    def __exec_command_bash_minishell(self, command_line: str):
        bash_proc = exec_command_line(command_line, BASH_PATH)
        minishell_proc = exec_command_line(command_line, MINISHELL_PATH)
        minishell_proc.stdout = minishell_proc.stdout.strip(self.minishell_prompt)
        minishell_proc.stdout = minishell_proc.stdout.lstrip(command_line)
        minishell_proc.stdout = minishell_proc.stdout.lstrip('\n')
        result = json_sirialize(command_line, bash_proc, minishell_proc)
        self.log.add(result)
        return result

    def search(self):
        label, status = choice_label_and_status()
        result = self.log.search(label, status)
        return result

    def exec(self):
        command_line = input('実行したいコマンドを入力してください: ')
        result = self.__exec_command_bash_minishell(command_line)
        return result

    def exec_all(self):
        results_list = []
        text_file_path = input('コマンドファイルのパスを入力してください\n指定したファイルが開けない場合、デフォルトファイルが使用されます: ')
        if not os.path.isfile(text_file_path):
            text_file_path = DEFAULT_COMMAND_PATH
        with open(text_file_path, 'r') as f:
            for command in f.readlines():
                command = command.rstrip('\n')
                result = self.__exec_command_bash_minishell(command)
                results_list.append(result)
        return results_list

    def show(self):
        result = self.log.load()
        return result

    def clear(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)


def main():
    pass


if __name__ == '__main__':
    main()
