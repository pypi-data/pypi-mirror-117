Build a package:
```
pip install setuptools wheel
python ./setup.py  sdist bdist_wheel
```

Then upload to PyPI:

```
twine upload ./dist/*
```
