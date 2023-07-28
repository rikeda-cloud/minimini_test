from presentation_layer.color import Color

def choice_label_and_status():
    labels = ['diff_exit_status', 'diff_stdout', 'diff_stderr']
    for idx, label in enumerate(labels):
        Color.print(f'[{idx + 1}] {label}', Color.BLUE)
    while True:
        try:
            select_idx = int(input('検索したい項目のインデックスを選択してください: '))
            if 0 < select_idx <= len(labels):
                break
            else:
                Color.print('無効な値が入力されました', Color.RED)
        except ValueError:
            Color.print('無効な値が入力されました', Color.RED)
    select_status = input('KOまたはOKを入力(不正な入力の場合、KOが選択されます)').upper()
    select_status = 'OK' if select_status == 'OK' else 'KO'
    return labels[select_idx - 1], select_status
