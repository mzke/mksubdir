import os
import sys
from mksubdir import MkSubDir

VERSAO = "0.1"


def print_help():
    print(f"mksubdir {VERSAO}")
    print("Use: mksubdir [pasta_base] [pasta_nova]")
    print("Exemplo: mksubdir C:\\Temp \\RH\\Sefip")


if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print_help()
        exit(1)

    try:
        arg2 = sys.argv[2]
    except IndexError:
        arg2 = None

    mksubdir = MkSubDir(arg1, arg2)
    mksubdir.execute()




