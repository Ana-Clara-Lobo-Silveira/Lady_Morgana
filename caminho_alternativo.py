import os
import sys

def caminho_alternativo(caminho):
    try:
        base = sys._MEIPASS
    except AttributeError:
        base = os.path.abspath(".")

    return os.path.join(base, caminho)
