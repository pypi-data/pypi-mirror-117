# Compylex

Compylex is a package that allows you to compile code using a python script.<br> Compylex accepts the code , language and user inputs and returns the output.<br> Compylex uses the preinstalled compilers from your machine and runs them against the inputs given to it.

# Testing:

To test compylex run the following code:

```python
    from compylex.compiler import Compile
    code = "print('Hello World!')"
    lang = "PYTHON"
    inp = ""
    run_id = 0
    CompilerObject = Compile(code, lang, inp, run_id)
    print(code.get_status())
    print(code.get_output())

```

- code - (String) The code to compile.
- lang - (String) [All caps] The programming language (PYTHON/C/C++).
- inp - (String) The inputs that need to passed to the compiler.
- run_id - (int) An identification number for the compile task.
- get_status() - Returns the compilation status ( 1 : Success and 0 : Error).
- get_output() - Returns the compilation output.

# Contributing to Compylex

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
