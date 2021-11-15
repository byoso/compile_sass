#! /usr/bin/env python3.9
# coding: utf-8

import sys
import os
import time
from datetime import datetime
# pip install libsass
import sass


def compile_one(sass_path=None):
    """Compiles the sass file given into a css file using
    the same name"""
    with open(sass_path, "r") as sass_file:
        sass_code = sass_file.read()
    try:
        css_code = sass.compile(string=sass_code)
    except sass.CompileError as ex:
        print(f"{datetime.now()} WIP -  not compilable yet: {sass_path}")
        print(f"{ex}")
        os.system(f"notify-send 'SASS ERROR' '{ex}'")
    else:
        css_path = sass_path[:-4]+"css"

        with open(css_path, "w") as css_file:
            css_file.write(css_code)
        print(f"{datetime.now()} compiled: {css_path}")


def compile_all(directory=None):
    """Compiles all the sass files in the given directory"""
    print(directory)
    sass_files = [
        f for f in os.listdir(directory) if os.path.isfile(
            os.path.join(directory, f)) and f.endswith('.sass')]
    for file in sass_files:
        compile_one(file)


def watch(directory=None, timer=1):
    print(f"watching : {directory}")
    # compile_all(directory)
    eye_on = {}
    for file in os.listdir(directory):
        if os.path.isfile(
                os.path.join(directory, file)) and file.endswith('.sass'):
            eye_on[file] = os.path.getmtime(file)

    while True:
        time.sleep(timer)
        new_sass_files = [
            f for f in os.listdir(directory) if os.path.isfile(
                os.path.join(directory, f)) and f.endswith('.sass')]
        for file in new_sass_files:
            if file not in eye_on:
                compile_one(file)
                eye_on[file] = os.path.getmtime(file)
            elif eye_on[file] != os.path.getmtime(file):
                compile_one(file)
                eye_on[file] = os.path.getmtime(file)


def handler(args):
    if len(args) == 1 or args[1] in ["-a", "--all"]:
        compile_all(os.getcwd())
    if len(args) > 1:
        if args[1] in ["-f", "--file"]:
            if len(args) > 2:
                sass_path = args[2]
                compile_one(sass_path)
            else:
                print("A file path is expected")
        if args[1] in ["-w", "--watch"]:
            watch(os.getcwd())
        if args[1] in ["-h", "--help"]:
            print(
                "Sass compiler\n"
                "\n"
                "synopsis:\n"
                "sass_compiler.py [option 1] [option 2]\n"
                "\n"
                "option 1 :\n"
                "-f, --file, this will compile a sass file into a \n"
                "    css file. You need to enter the sass file path as option 2\n\n"
                "-a, --all, or no option, compile all the sass files in the working directory\n"
                "into css files.\n\n"
                "-w, --watch, if any sass file in the directory is changed,\n"
                "the program will automatically try to compile it\n"
                "(very convenient for dev).\n\n"
                )


if __name__ == "__main__":
    args = sys.argv
    try:
        handler(args)
    except KeyboardInterrupt:
        print("\nend")
