import shutil


def print_centralizado(s):
    print(s.center(shutil.get_terminal_size().columns))