
Folder Routing

# Logging

- logger starts in run.py
- logger can also start in run_estimate.py

logging level and logging or not are parameters. 

- invoke_testers run with loggers, loggers overall for a folder, and loggers for each invoke in folder. 

- different handlers for the same logger
    + can have one handler for console output, another handler for logging to file output
    + [Example](https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters)
- get root logger: logging.getLogger('')