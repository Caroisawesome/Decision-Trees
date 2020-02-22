PY = python
PIP = pip

install:
	$(PIP) install numpy
	$(PIP) install scipy

all: 
	$(PY) "main.py" 0 0 
	$(PY) "main.py" 0 1 
	$(PY) "main.py" 0 2 
	$(PY) "main.py" 1 0 
	$(PY) "main.py" 1 1 
	$(PY) "main.py" 1 2 
	$(PY) "main.py" 2 0 
	$(PY) "main.py" 2 1 
	$(PY) "main.py" 2 2 


