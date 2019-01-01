# Python

Learn/ing [Python](https://www.python.org)


## Machine Learning

The main motivation to (re)learn Python now (according to other important topics I have to learn to
 too) is the fact that it is widely used for Machine Learning (that I am learning too).
 
I think one of the reasons for that, one of the strength of Python is the collections: see below. 


## Table of content

- [Setup](./doc/setup.md)
- Collections:
  - [List](./cod/test_collection_1_list.py) and [Lists with OOP](./cod/test_collection_2_list_oop.py)
  - [Set](./cod/test_collection_3_set.py)
  - [Dictionary](./cod/test_collection_4_dict.py)
  - [Tuple](./cod/test_collection_5_tuple.py)


## Unit tests as documentation

> I decided to provide tutorial of the language as unit tests that can be executed. 

- [Getting Started With Testing in Python – Real Python](https://realpython.com/python-testing/#choosing-a-test-runner)
- To see: [sniffer](https://pypi.org/project/sniffer/0.2.3/)

Run unit tests with the following command line:

```
cd cod/
python -m unittest discover
```

As continuous running:

- https://stackoverflow.com/questions/15166532/how-to-automatically-run-tests-when-theres-any-change-in-my-project-django

```
npm install -g nodemon
nodemon --ext py --exec "python -m unittest discover"
```

