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

```python
>>> import Factory
>>> Factory.Factory()
<Factory.__init__.Factory at 0x7fbdae14eda0>
>>> Factory.Factory()
<Factory.__init__.Factory at 0x7fbdae14eda0>
```
