import os
import subprocess
from persistence_layer.log import Log
from presentation_layer.color import Color
from business_logic_layer.utils.json_sirialize import json_sirialize
from business_logic_layer.utils.diff import diff
from business_logic_layer.utils.choice_label_and_status import choice_label_and_status
from business_logic_layer.utils.anlysis_result import anlysis_result
from business_logic_layer.utils.input_file_name import input_want_to_create_file_name
from business_logic_layer.utils.input_file_name import input_exec_command_file_name


BASH = 'bash'
BASH_PATH = '/bin/bash'
MINISHELL = 'minishell'
MINISHELL_PATH = './minishell'
DEFAULT_COMMAND_DIR = './command/'
DEFAULT_COMMAND_PATH = DEFAULT_COMMAND_DIR + 'default_command.cmd'
EXTENSION = '.cmd'


class Command:
    def __init__(self, minishell_prompt):
        self.log = Log()
        self.minishell_prompt = minishell_prompt

    def __exec_command_line(self, command_line: str, shell_path: str):
        proc = subprocess.run(
                    shell_path,
                    input=command_line,
                    encoding='UTF-8',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
        )
        return proc

    def __exec_command_bash_minishell(self, command_line: str):
        bash_proc = self.__exec_command_line(command_line, BASH_PATH)
        minishell_proc = self.__exec_command_line(command_line, MINISHELL_PATH)
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
        command_file_path = input_exec_command_file_name()
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
        file_name = input_want_to_create_file_name()
        results = self.log.load()
        command_list = [command for command in results.keys()]
        with open(DEFAULT_COMMAND_DIR + file_name, 'w') as f:
            f.writelines('\n'.join(command_list))
        return file_name

    def clear(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)
