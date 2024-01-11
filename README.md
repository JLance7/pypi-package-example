# Pypi package example
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Development
```bash
pip install -e .
```
*import/test code*

## Testing
```bash
python -m unittest
```

## Deployment
```bash
python setup.py sdist or python setup.py bdist_wheel
twine upload dist/*
```