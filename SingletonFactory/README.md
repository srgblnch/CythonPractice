# SingletonFactory

This code will provide an singleton object.

```
SingletonFactory
 |-- setup.py
 |-- barfoo
     |-- [__init__.py]
     |-- [__init__.pyx]
     |-- factory.pyx
     |-- singleton.pyx
     |-- version.pyx
     |-- subm
         |-- [__init__.py]
         |-- [__init__.pyx]
         |-- bar.pyx
         |-- foo.pyx
```

To build the extension:

```bash
$ python3 setup.py build
$ python3 setup.py install
```

To install in a different directory, but in the pythonpath append at the end of the install command: "--prefix _path_".

## version 0.0.1:

```python
>>> import barfoo
>>> barfoo.version()
 '0.0.1-alpha'
>>> barfoo.Factory()
 <barfoo.__init__.Factory at 0x7fbdae14eda0>
>>> barfoo.Factory()
 <barfoo.__init__.Factory at 0x7fbdae14eda0>
```

But due to then, there are issues to solve when the factory likes to load a submodule to build object from them.

## The issues:

### Multiple cythonize files

Using the tag [multiplecythonize](https://github.com/srgblnch/CythonPractice/tree/multiplecythonize/SingletonFactory) one get the exception:

```python
>>> import barfoo
(...)
ImportError: dynamic module does not define init function (PyInit_barfoo)
```

### Submodule import

With a \_\_init\_\_.pyx file (tag [nosubmodule](https://github.com/srgblnch/CythonPractice/tree/nosubmodule/SingletonFactory)) that does an include of those multiple files, then it can be imported, but not the submodule.

### \_\_init\_\_.py files

When those directories with sources have "\_\_init\_\_.py files, then the import of the module points to the installed ".py" file and not the ".so".

