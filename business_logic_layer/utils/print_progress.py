import sys
from presentation_layer.color import Color


def get_color_by_percentage(percentage: int):
    if percentage < 10:
        color = Color.YELLOW
    elif percentage < 30:
        color = Color.CYAN
    elif percentage < 50:
        color = Color.BLUE
    elif percentage < 90:
        color = Color.GREEN
    else:
        color = Color.RED
    return color

def print_progress(dividend: int, divisor: int):
    progress = (dividend + 1)/divisor
    bar_length = 100
    progress_bar = '=' * int(bar_length * progress)
    spaces = ' ' * (bar_length - len(progress_bar))
    percentage = int(progress * 100)
    color = get_color_by_percentage(percentage)
    sys.stdout.write(f'\rProgress: [{color}{progress_bar}>{spaces}{Color.END}] {int(progress * 100)}%')
    sys.stdout.flush()
