# Python

Learn/ing [Python](https://www.python.org)


## Unit tests as documentation

- [Getting Started With Testing in Python – Real Python](https://realpython.com/python-testing/#choosing-a-test-runner)
- To see: [sniffer](https://pypi.org/project/sniffer/0.2.3/)

Run unit tests with the following command line:

```
cd cod/
python -m unittest discover
```

## Setup on Mac OS X Mojave

- Install [PyEnv](https://github.com/pyenv/pyenv) to handle multiple versions of Python:

```
brew update
brew install pyenv
```

- Enable XCode:

```
xcode-select --install
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

- Install wanted version distribution:

```
pyenv install --list
pyenv install 3.7.1
```
