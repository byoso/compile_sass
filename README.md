# compile_sass.py


*Easy compile your sass files into css with a single python script in your ~/bin folder*


## requirements:
 libsass

so:

```sh
    pip install libsass
```

## Installation suggested

Simply put this script in you ~/bin folder, so you can call it anywhere in terminal.
Or just use it as you wish.

## Commands

In the directory where you want to compile some sass:

compile a single sass file

```sh
    compile_sass.py [-f | --file] [file name]
```

compile all the sass files in the working directory

```sh
    compile_sass.py [-a | --all | ]
```

watch and compile ONLY if a change occures:
```sh
    compile_sass.py [-w | --watch]
```

exit the watch : ctrl+c

## First use scenario

You want to work on some sass files. Some are already written, they just need to be compile and watched to follow your
modifications.

so first compile all sass:
```sh
    compile_sass.py
```
and then watch the directory
```sh
    compile_sass.py -w
```
