# Simple Python Logger

SimplePyLogger is a very simple logging library for Python.

Its main functionalities are based on the Python logging library with some tweaks.

Currently, it is based on the Singleton pattern. So, only one logger instance can be created.

# Install

First, update `pip` by running `python -m pip install --upgrade pip`. Then, run `python -m pip install SimplePyLogger`.

# (Very short) Tutorial

First create a `Logger` instance:

```python
from PyLogger import Logger
logger = Logger() # using current work directory
logger = Logger(path_to_log_file) # or using custom path
```

Then log whatever you want to:

```
logger.info("Some info")
logger.warning("Some warning")
logger.error("Some error")
```

It currently accepts prefix, end and sep kwargs for logging.
