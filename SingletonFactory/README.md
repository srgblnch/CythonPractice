# SingletonFactory

This code will provide an singleton object.

```
SingletonFactory
 |-- setup.py
 |-- barfoo
     |-- __init__.py
     |-- factory.pyx
     |-- singleton.pyx
     |-- version.pyx
     |-- subm
         |-- __init__.py
         |-- bar.pyx
         |-- foo.pyx
```

To build the extension:

```bash
$ python3 setup.py build
$ python3 setup.py install
```

(It works also with python2.7) To install in a different directory, but in the pythonpath append at the end of the install command: "--prefix _path_".

## version 0.0.3:

```python
>>> import barfoo
>>> barfoo.version()
 '0.0.3'
>>> barfoo.Factory()
 <barfoo.factory.Factory at 0x(...)>
>>> barfoo.Factory()
 <barfoo.factory.Factory at 0x(...)>
```

Important to see that the memory reference point the same position, that means it is returning the same object.

Then use this factory to build the submodule objects:

```python
>>> barfoo.Factory().getBar()
<barfoo.subm.bar.Bar at 0x(...)>
>>> barfoo.Factory().getFoo()
<barfoo.subm.bar.Foo at 0x(...)>
```

Each time giving you a fresh (different) *Bar* and *Foo* object. By the way one can access those objects directly using the submodule.

```python
>>> import barfoo.subm
>>> barfoo.subm.Bar().bar
 'bar'
barfoo.subm.Foo().foo
 'foo'
```
