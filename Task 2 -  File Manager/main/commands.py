import os
from pathlib import Path


def pwd():
    print(os.getcwd())


def cd(path):
    os.chdir(path)


def touch(filename):
    Path(os.path.join(os.getcwd(), filename)).touch()


def cat(path):
    with open(path) as file:
        print(file.read())


def ls():
    print(os.listdir())


def rm(filename):
    os.remove(filename)
