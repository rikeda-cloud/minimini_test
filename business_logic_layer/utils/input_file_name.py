import os


def input_want_to_create_file_name(setting):
    while True:
        file_name = input(f'作成したい{setting.extension}ファイル名を入力してください: ')
        if not file_name.endswith(setting.extension):
            print(f'ファイルの拡張子は{setting.extension}のみ使用できます')
        elif os.path.isfile(file_name):
            print("そのファイルはすでに存在します")
        else:
            break
    return file_name

def get_file_in_dir(cmd_dir):
    file_list = []
    file_or_dir_list = [file_or_dir for file_or_dir in os.listdir(cmd_dir)]
    for file_or_dir in file_or_dir_list:
        if os.path.isfile(cmd_dir + file_or_dir):
            file_list.append(file_or_dir)
        else:
            [file_list.append(file_or_dir + '/' + file) for file in os.listdir(cmd_dir + file_or_dir)]
    return file_list

def input_exec_command_file_name(setting):
    [print(f'{file}') for file in get_file_in_dir(setting.command_dir)]
    prompt = 'コマンドファイルのパスを入力してください\n指定したファイルが開けない場合、デフォルトファイルが使用されます: '
    command_file_path = setting.command_dir + input(prompt)
    if not os.path.isfile(command_file_path):
        command_file_path = setting.default_command_file
    return command_file_path
