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

```python
>>> import barfoo
>>> barfoo.version()
 '0.0.1-alpha'
>>> barfoo.Factory()
 <barfoo.__init__.Factory at 0x7fbdae14eda0>
>>> barfoo.Factory()
 <barfoo.__init__.Factory at 0x7fbdae14eda0>
```

## Known issues

- Following the [PackageHierarchy](https://github.com/cython/cython/wiki/PackageHierarchy) the directory Factory should contain a "\_\_init\_\_.py" file, but then the module imported doen't have the Factory object.

- Separate the _singleton_ file in a submodule, lets say _utils_, it is unknown how later the import must be made.
