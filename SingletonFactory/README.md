# SingletonFactory

This code will provide an singleton object.

```
SingletonFactory
 |-- setup.py
 |-- Factory
     |-- __init__.pyx
     |-- factory.pyx
     |-- singleton.pyx
     |-- version.pyx
```

To build the extension:

```bash
$ python3 setup.py build
```

```python
>>> import Factory
>>> Factory.version()
 '0.0.1-alpha'
>>> Factory.Factory()
 <Factory.__init__.Factory at 0x7fbdae14eda0>
>>> Factory.Factory()
 <Factory.__init__.Factory at 0x7fbdae14eda0>
```

## Known issues

- Following the [PackageHierarchy](https://github.com/cython/cython/wiki/PackageHierarchy) the directory Factory should contain a "__init__.py" file, but then the module imported doen't have the Factory object.

- Separate the _singleton_ file in a submodule, lets say _utils_, it is unknown how later the import must be made.
