# cq-intro-python
Calcul Québec training : Introduction to Programming with Python - PYT101

# Content
The content of this workshop is based on [Software Carpentries - Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/)

# Run locally
1. Create a virtual environment
```bash
python -m venv venv-pyt101
```

2. Activate the environment
```bash
source venv-pyt101/bin/activate
```

3. Install [requirements](requirements.txt)
```bash
pip install -r requirements.txt  # or requirements-dev.txt if developping
```

4. Run jupyterlab in your browser
```bash
jupyter lab --ip=127.0.0.1
```

## Development
```bash
pip install -r requirements-dev.txt
```

### 1. Sync markdown to notebooks
Synchronize solutions markdown to their associated notebooks
```bash
jupytext --sync solutions/*.md
```

### 2. Empty notebooks for participants
Empty all solutions notebooks and output in current directory
```bash
python scripts/participant_empty.py solutions/*.ipynb -o .
```
