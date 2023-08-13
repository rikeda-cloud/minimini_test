import sys
import json
from presentation_layer.minimini_test import Option
sys.path.append("../business_logic_layer")
sys.path.append("../persistence_layer")

class Setting:
    def __init__(self, setting_file):
        with open(setting_file, 'r') as f:
            data = json.load(f)
            self.minishell_prompt = data.get('MINISHELL_PROMPT', 'minishell >> ')
            self.default_shell = data.get('DEFAULT_SHELL', 'bash')
            self.default_shell_path = data.get('DEFAULT_SHELL_PATH', '/bin/bash')
            self.minishell = data.get('MINISHELL', 'minishell')
            self.minishell_path = data.get('MINISHELL_PATH', './minishell')
            self.log_dir = data.get('LOG_DIR', './log/')
            self.log_file_format = data.get('LOG_FILE_FORMAT', '%Y_%m_%d_%H_%M_%S')
            self.command_dir = data.get('COMMAND_DIR', './command/')
            self.default_command_file = data.get('DEFAULT_COMMAND_FILE', './command/default_command.cmd')
            self.extension = data.get("EXTENSION", ".cmd")
            

def main(setting_file):
    setting = Setting(setting_file)
    option = Option(setting)
    option.test_loop()


if __name__ == '__main__':
    main('setting.json')
