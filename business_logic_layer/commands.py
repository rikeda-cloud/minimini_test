import os
import re
import time
import subprocess
from persistence_layer.log import Log
from presentation_layer.color import Color
from business_logic_layer.utils.json_sirialize import json_sirialize
from business_logic_layer.utils.diff import diff
from business_logic_layer.utils.choice_label_and_status import choice_label_and_status
from business_logic_layer.utils.anlysis_result import anlysis_result
from business_logic_layer.utils.input_file_name import input_want_to_create_file_name
from business_logic_layer.utils.input_file_name import input_exec_command_file_name


class Command:
    def __init__(self, setting):
        self.log = Log(setting)
        self.setting = setting

    def __exec_command(self, command: str, shell_path: str):
        proc = subprocess.run(
                    shell_path,
                    input=command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding='UTF-8'
        )
        return proc

    def __exec_command_shell(self, command: str):
        shell_proc = self.__exec_command(command, self.setting.default_shell)
        minishell_proc = self.__exec_command(command, self.setting.minishell_path)
        minishell_proc.stdout = re.sub(r'^.*\n', '', minishell_proc.stdout)
        result = json_sirialize(command, shell_proc, minishell_proc, self.setting)
        self.log.add(result)
        return result

    def exec(self):
        command = input('実行したいコマンドを入力してください: ')
        result = self.__exec_command_shell(command)
        return result

    def all(self):
        command_file_path = input_exec_command_file_name(self.setting)
        start_time = time.perf_counter()
        with open(command_file_path, 'r') as f:
            result_list = [self.__exec_command_shell(cmd.rstrip('\n')) for cmd in f.readlines()]
        end_time = time.perf_counter()
        print(f'Execution time = {end_time - start_time}')
        return result_list

    def show(self):
        result = self.log.load()
        return result

    def search(self):
        label, status = choice_label_and_status()
        result = self.log.search(label, status)
        return result

    def anlysis(self):
        result = self.log.load()
        result = anlysis_result(result)
        return result

    def create(self):
        file_name = input_want_to_create_file_name(self.setting)
        result = self.log.load()
        command_list = [command for command in result.keys()]
        with open(self.setting.command_dir + file_name, 'w') as f:
            f.writelines('\n'.join(command_list))
        return file_name

    def clear(self):
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)
