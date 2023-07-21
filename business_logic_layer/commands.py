import os
import subprocess
from persistence_layer.log import Log
from presentation_layer.color import Color


BASH = 'bash'
BASH_PATH = '/bin/bash'
MINISHELL = 'minishell'
MINISHELL_PATH = './minishell'
DEFAULT_COMMAND_DIR = './command/'
DEFAULT_COMMAND_PATH = DEFAULT_COMMAND_DIR + 'default_command.cmd'
EXTENSION = '.cmd'


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
    p1_retcode, p2_retcode = proc1.returncode, proc2.returncode
    result_dict['exit_status'] = {BASH: p1_retcode, MINISHELL: p2_retcode}
    result_dict['stdout'] = {BASH: proc1.stdout, MINISHELL: proc2.stdout}
    result_dict['stderr'] = {BASH: proc1.stderr, MINISHELL: proc2.stderr}
    nest_result[command_line] = result_dict
    return nest_result


def anlysis_result(results: dict[str, str]):
    after_anlysis_result = {
            'total_exit_status_faild': 0,
            'total_stdout_faild': 0,
            'total_stderr_faild': 0
    }
    for result in results.values():
        if result['diff_exit_status'] == 'KO':
            after_anlysis_result['total_exit_status_faild'] += 1
        if result['diff_stdout'] == 'KO':
            after_anlysis_result['total_stdout_faild'] += 1
        if result['diff_stderr'] == 'KO':
            after_anlysis_result['total_stderr_faild'] += 1
    return after_anlysis_result


def choice_label_and_status():
    labels = ['diff_exit_status', 'diff_stdout', 'diff_stderr']
    for idx, label in enumerate(labels):
        Color.print(f'[{idx + 1}] {label}', Color.BLUE)
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

def input_file_name():
    while True:
        file_name = input(f'作成したい{EXTENSION}ファイル名を入力してください: ')
        if not file_name.endswith(EXTENSION):
            print(f'ファイルの拡張子は{EXTENSION}のみ使用できます')
        elif os.path.isfile(file_name):
            print("そのファイルはすでに存在します")
        else:
            break
    return file_name


class Command:
    def __init__(self, minishell_prompt):
        self.log = Log()
        self.minishell_prompt = minishell_prompt

    def __exec_command_bash_minishell(self, command_line: str):
        bash_proc = exec_command_line(command_line, BASH_PATH)
        minishell_proc = exec_command_line(command_line, MINISHELL_PATH)
        minishell_stdout = minishell_proc.stdout
        minishell_stdout = minishell_stdout.strip(self.minishell_prompt)
        minishell_stdout = minishell_stdout.lstrip(command_line)
        minishell_stdout = minishell_stdout.lstrip('\n')
        minishell_proc.stdout = minishell_stdout
        result = json_sirialize(command_line, bash_proc, minishell_proc)
        self.log.add(result)
        return result

    def exec(self):
        command_line = input('実行したいコマンドを入力してください: ')
        result = self.__exec_command_bash_minishell(command_line)
        return result

    def all(self):
        results_list = []
        prompt = 'コマンドファイルのパスを入力してください\n指定したファイルが開けない場合、デフォルトファイルが使用されます: '
        command_file_path = input(prompt)
        if not os.path.isfile(command_file_path):
            command_file_path = DEFAULT_COMMAND_PATH
        with open(command_file_path, 'r') as f:
            for command in f.readlines():
                command = command.rstrip('\n')
                result = self.__exec_command_bash_minishell(command)
                results_list.append(result)
        return results_list

    def show(self):
        result = self.log.load()
        return result

    def search(self):
        label, status = choice_label_and_status()
        result = self.log.search(label, status)
        return result

    def anlysis(self):
        results = self.log.load()
        results = anlysis_result(results)
        return results

    def create(self):
        file_name = input_file_name()
        results = self.log.load()
        command_list = [command for command in results.keys()]
        with open(DEFAULT_COMMAND_DIR + file_name, 'w') as f:
            f.writelines('\n'.join(command_list))
        return file_name

    def clear(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)


def main():
    pass


if __name__ == '__main__':
    main()
