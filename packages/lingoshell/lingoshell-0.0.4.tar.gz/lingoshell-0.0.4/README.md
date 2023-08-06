# LingoShell

LingoShell is a programming language that allows you to write in different human languages

- Website: <https://lingoshell.com>
- Pypi: <https://pypi.org/project/lingoshell/0.0.1/>

## Supported Human Languages

- English
- Mandarin (Traditional)

## Usage/Examples

Hello World Program

```
PRINT("HELLO WORLD)
```

Switching human languages with the LANG variable

```
# Hello World in different human languages
VAR LANG = "en"
PRINT("Hello")

VAR LANG = "zh"
打印("你好")
```

## Demo

Feel free to try LingoShell with the Repl it [here](https://github.com/gavinkhung/lingoshell-lang)

## Contributing

Contributions are always welcome!

If you want to submit a new human language, check out the form [here](https://forms.gle/Bc5qEJAQFjGFPkQS7)

## Acknowledgements

- [Make YOUR OWN Programming Language](https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD)

## Building Package

```bash
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
