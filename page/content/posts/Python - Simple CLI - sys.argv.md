---
title: Python - Simple CLI - sys.argv
description: What is `sys.argv` and how to use it for simple command line interface
date: 2025-09-09T07:33:55+02:00
draft: true
tags:
  - python
---
# How to use `sys.argv` in Python

When you write a [[CLI]] (Command Line Interface) applications, you often need to provide some arguments to your program, regardless whether it is a big application like [[ffmpeg]] or  small python script for renaming files in directory.  

In this blog post I'm gonna shortly present you, what is `sys.argv`, when and why to use it and how to use it. 

1. [[#What is `sys.argv`]]
2. [[#When and why to use `sys.argv`]]
3. [[#How to use `sys.argv`]]
4. [[#Advance usage of `sys.argv`]]
5. [[#Final thoughts]]

# What is `sys.argv`

`argv` is  a variable in the `sys` module that is a list containing all the arguments of the executed command, starting with the command itself.

It's exact implementation is written in C, and the behavior can slightly differr depending on the OS where Python is run. 

Let's look at the simplest example:

```python
import sys

print(sys.argv)
```
When run it will print to the console what arguments ware passed:
```bash
$ python3 script.py -d --verbose test.txt -p "with space" -p2=0
['script.py', '-d', '--verbose', 'test.txt', '-p', 'with space', '-p2=0']
```
As you can see, the first argument, is the script's name, and then there is the rest. 
# When and why to use `sys.argv`

Use it for simple argument parsing for your scripts. For everything more complicated use build-in [argparse](https://docs.python.org/3/library/argparse.html) module, or other third party tool like [click](https://pypi.org/project/click/) 

In the example above you can see that `-p "with space"` and `-p2=0` are not treated the same. And this is just an example for one of many reasons why in more sophisticated programs you would like to use specialized argument parser like `argparse`. 

It is easy to parse one argument and couple simple flags, but when it comes to tools with many flags, that can support many standards, types checking, having subparsers or mutually excluded flags - it becomes too cumbersome to work with `argv`. And if you do decide to do that, you will end up in writing your own custom argument parser tool - which for educational purposes is worth doing, but definitely something to avoid for production code. 

# How to use `sys.argv`

Using `sys.argv` is very simple, since it is just a list that contains strings. We can access the first argument by its index e.g. `sys.argv[1]`, second argument `sys.argv[2]` etc. 

Let's say we have simple server to which we want to pass the address and the port on which the server runs.

```bash
$ python3 server.py 0.0.0.0 8000
```

This can be achieved by such code:

```python
import sys

class Server:
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def run(self):
		print(f"Running on: {self.host}:{self.port}")
		input("Press any key to exit.")

if __name__ == "__main__":
	host = sys.argv[1]
	port = sys.argv[2]
	
    server = Server(host, port)
    server.run()
```

This is perfect example of how to use `sys.argv` in you personal scripts and small programs.
You do not need much to start using CLI and making your life easier.

Unfortunately such trivial usage is very limited, what if someone pass only one argument? The program crash with `IndexError` cause `sys.argv[2]` does not exist. What if your program requires the port as integer, but `sys.argv` stores only strings? And what about any basic user experience, like help message to help the users to navigate in your program?

# Advance usage of `sys.argv`

The problem is that such solution is very poor for anyone else than You! If you try to give it to someone else, you will definitely start hearing complaining, about program not working, crashing and missing some basic help features. At this point, you can just switch to specialized argument parser library like `argparse` or `click`. Or you can try to add some basic features by yourself and still utilize `sys.argv`

So first, we need to make some assumptions. The program cannot do everything. It has to work in some boundaries. Requirements and behaviors can change over the time, but at least they need to be defined. So let's make ours.

Our fake server program will have such structure:

```bash
Usage: server [port] [--host] [--help] [--version]
```

First argument is positional, it will be port and it must be provided. We will support `--host` flag that will accept an IPv4 address. Two additional flags, `--help` for printing help and usage information, and `--version` to give users information which version they have installed.

As you will see those requirements is a small cheat from my side, cause I already know beforehand what problems we will encounter, so I already set the requirements in a way to avoid dealing with them.

## Adding help message

Starting easy, we can add simple help message. Because we do not use any library we need to write such help message ourselves. 

```python
from pathlib import Path

__author__ = "Adam Walkiewicz"
__version__ = "0.0.1"


HELP = f"""\
Usage: {Path(__file__).name} [port] [--host] [--help] [--version]

Positional arguments:
    port\t\tRun server on this port, default 8080.

Options:
    --help\t\tPrint this help message.
    --host\t\tRun server on this address, default to 127.0.0.1.
    --version\t\tPrint program version and exit.

Author:
    {__author__}

License:
    MIT 2025 {__author__}
"""
```

For an extra, I also added information about author and version (`__version__` will be also useful later).

Additionally I used `Path` from `pathlib` library to get the currently run program name. Alternatively instead of `Path(__file__).name` we could use `sys.argv[0]`. But as a huge fun of `Path` I decided to sneak it here. 

So, help looks OK, but we need to trigger it somehow.

```python
if __name__ == "__main__":
    if "--help" in sys.argv:
        print(HELP)
        sys.exit(0)
```

With simple [[if-statement]] we check if the `--help` string is in the `sys.argv`, and if it is there we print it and exit.

## Adding version

We literally are going to do the same thing with the `--version` flag:

```python
    if "--version" in sys.argv:
        print(__version__)
        sys.exit(0)
```

Now after having `--help` and `--version` flags, it's time to mention the first problem. Our program does not support short version of flags, like `-h` for help or `-v` for version. obviously we can add it by doing:

```python
if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(HELP)
        sys.exit(0)
	
	if "--version" in sys.argv or "-v" in sys.argv:
        print(__version__)
        sys.exit(0)
```

Nevertheless it is a complication. And spoiler alert - only the first one. 
## Adding host flag

Host flag is a little bit trickier than other 2. Cause here we are not only checking if the flag is among the arguments, but also we need to the value for that flag which is the address. 

```python
    host: str | None = None
    if "--host" in sys.argv:
        host_index = sys.argv.index("--host")
        try:
            host = sys.argv[host_index + 1]
        except IndexError:
            print("Missing host argument", file=sys.stderr)
            sys.exit(2)
```

First we need to define the `host` variable and assign it a default value in case it is not among provided arguments. if it is, we get the `--host` flag index, and it's value that is under `host_index + 1`. It can happen that user provides the flag but forgets to add the address. Then, according to our requirements that we defined, there shouldn't be anything else later, right?

Well, if the users were following our guidelines we wen't here in the first place, and just stop on thee first iteration of out program from [[#How to use `sys.argv`]] section.

Users makes mistakes, for example:

```bash
$ python3 server.py 8000 --host --verssoin 127.0.0.1
```

This will happily pass our argument parsing methods and crash the program later when we try to run server on wrongly spelled `--verssoin`

So let's fix it. First by adding the set of all of the legitimate flags that can be used in our program. And checking if in arguments there is a flag that is not valid.

```python

VALID_FLAGS = {"--help", "-h", "--version", "-v", "--host"}

# <- snip ->
	flags = {flag for flag in sys.argv if flag.startswith("-")}
    invalid_flags = flags - VALID_FLAGS
    if invalid_flags:
        print(f"Following flags are not valid: {invalid_flags}", file=sys.stderr)
        sys.exit(2)
```

But that's not the end of problems. What if the user provides a wrong IPv4 address? fortunately we can validate that with build-in module `ipaddress`:

```python
import ipaddress

# <- snip ->
        try:
            host = sys.argv[host_index + 1]
			ipaddress.IPv4Address(host)
        except IndexError:
            print("Missing host argument", file=sys.stderr)
            sys.exit(2)
        except ipaddress.AddressValueError:
	        print("Provided host '{host}' is not a valid IPv4 address", file=sys.stderr)
            sys.exit(2)
```

So, does it mean that everything should work fine now? Not at all. Still there might be edge cases that we didn't cover. Plus we completely ignore the fact about standard (TODO: check that) where we use equal `=` sign for flag arguments like: `--host=0.0.0.0` . But solving it here would be too much. I will leave it for readers.

## Adding port 

Let's skip ahead same chain of thoughts and immediately add handling for already known situations where user may forgot to provide argument or it will be in a wrong type.

```python
    try:
        port = int(sys.argv[1])
    except IndexError:
        print("Missing port", file=sys.stderr)
        sys.exit(2)
    except ValueError:
        print("Port must be an integer", file=sys.stderr)
        sys.exit(2)
```

Here is my little fraud. In many programs similar to our, `port` could be provided on whatever position in relation to other flags. 

This:

```bash
$ python3 server.py 8000 --host 0.0.0.0
```

Should be treated the same as this:

```bash
$ python3 server.py --host 0.0.0.0 8000
```

In our requirements I deliberately defined that port hast to be the first argument, exactly to not bother myself with this situation.

We can tackle this be removing elements from the `sys.argv` list. But because lists are mutable, modifying int will affect everything that will use it. In our small program it shouldn't be a problem, but it can be considered as a bad practice, and it potentially may affect other parts of code and debugging. 

So let's do it properly by the book, and create a shallow copy of the `sys.argv`, than remove host flag and it's argument from it. That leaves us with list with 2 elements - program name and port.

```python
	arguments = sys.argv[::]  # arguments is a copy of sys.argv
	
	# <- snip ->
        try:
            host = sys.argv[host_index + 1]
            ipaddress.IPv4Address(host)
			arguments.remove(host)
            arguments.remove("--host")

	# <- snip ->
	try:    
        port = int(arguments[1])
```

Now, our program should work more or less correctly, with most of the edge cases covered.
# Final thoughts

Using `sys.argv` is very simple. But there are to sides of the medal in that simplicity. It is very useful for small scripts with little amount of arguments or flags. Quick to use when writing your own personal scripts. Unfortunately once you start to require more fancy features it rapidly becomes cumbersome to use.

Even in my advance example that covers more features we could not fix all the issues. At the end we still not support equal sign `=` for parameter value. And who know what other issues are hidden awaiting to be encountered.

Our simple program supported very limited amount of flags and positional arguments. With each flag or argument more, everything becomes more complicated. More boiler plate code must be added to candle each flag. 

This is the reason why specialized libraries were created. Although it is fun to handle arguments by yourself, it quickly becomes obvious that it is very challenging. That's why I recommend to use argparse or other library that is convenient for you. 

# Whole program (plus extras)

Final version of the code, plus couple extra thing like [[python docstring]]s and type annotations.

```python
import ipaddress
import sys

from pathlib import Path

__author__ = "Adam Walkiewicz"
__version__ = "0.0.1"


HELP = f"""\
Usage: {Path(__file__).name} [port] [--host] [--help] [--version]

Positional arguments:
    port\t\tRun server on this port, default 8080.

Options:
    --help\t\tPrint this help message.
    --host\t\tRun server on this address, default to 127.0.0.1.
    --version\t\tPrint program version and exit.

Author:
    {__author__}

License:
    MIT 2025 {__author__}
"""

VALID_FLAGS = {"--help", "-h", "--version", "-v", "--host"}


class Server:
    """Fake Server class, it does nothing.

    Attributes:
        HOST (str): Host to which server is bind.
        PORT (int): Port on which server runs.
    """

    HOST = "127.0.0.1"
    PORT = 8080

    def __init__(self, host: str | None = None, port: int | None = None) -> None:
        """Initialize Server with host and port.

        Args:
            host: Host to which server is bind, defaults to None.
            port: Port on which server runs, defaults to None.
        """

        self.host = host or Server.HOST
        self.port = port or Server.PORT

    def run(self) -> None:
        """Run the server"""

        print(f"Running on: {self.host}:{self.port}")
        input("Press any key to exit")


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(HELP)
        sys.exit(0)

    if "--version" in sys.argv or "-v" in sys.argv:
        print(__version__)
        sys.exit(0)

    flags = {flag for flag in sys.argv if flag.startswith("-")}
    invalid_flags = flags - VALID_FLAGS
    if invalid_flags:
        print(f"Following flags are not valid: {invalid_flags}", file=sys.stderr)
        sys.exit(2)

    arguments = sys.argv[::]
    host: str | None = None
    if "--host" in sys.argv:
        host_index = sys.argv.index("--host")
        try:
            host = sys.argv[host_index + 1]
            ipaddress.IPv4Address(host)
            arguments.remove(host)
            arguments.remove("--host")
        except IndexError:
            print("Missing host argument", file=sys.stderr)
            sys.exit(2)
        except ipaddress.AddressValueError:
            print("Provided host '{host}' is not a valid IPv4 address", file=sys.stderr)
            sys.exit(2)

    try:
        port = int(arguments[1])
    except IndexError:
        print("Missing port", file=sys.stderr)
        sys.exit(2)
    except ValueError:
        print("Port must be an integer", file=sys.stderr)
        sys.exit(2)

    server = Server(host, port)
    server.run()

```

---

# References:

- Official documentation: https://docs.python.org/3/library/sys.html#sys.argv
- Implementation in C (Python 3.14): https://github.com/python/cpython/blob/3.14/Python/sysmodule.c
- Argparse tutorial: https://realpython.com/command-line-interfaces-python-argparse/
- Click tutorial: https://realpython.com/python-click/
