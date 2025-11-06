import time
import sys

def show_loading_bar(duration=3):
    """Display a loading bar during PDF compilation"""
    bar_length = 40
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        filled = '=' * i
        empty = ' ' * (bar_length - i)
        arrow = '>' if i < bar_length else '='
        sys.stdout.write(f'\r[{filled}{arrow}{empty}] {percent:.0f}%')
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    sys.stdout.write('\n')
