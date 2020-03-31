# Logger
Custom Python Logging Tool for simple debugging (outside of print statements).

## How to Use
Three modules are needed when using the Logger:
1. Logger
    - ```from Logger import Logger```
2. SeverityType
    - ```from Logger import SeverityType```
3. A single policy (PrintPolicy, FilePolicy, etc.)
    - ```from Logger.Policy import PrintPolicy```

## Different Policies & Examples
### PrintPolicy
The *PrintPolicy* simply prints the log statement on the Python terminal.

```Python
from Logger import Logger
from Logger import SeverityType
from Logger.Policy import PrintPolicy

logger = Logger(PrintPolicy())
logger.write(SeverityType.DEBUG, "This is a test message!")
```


### FilePolicy
The *FilePolicy* writes the log statements onto a chosen text file.

```Python
from Logger import Logger
from Logger import SeverityType
from Logger.Policy import FilePolicy

logger = Logger(FilePolicy("debug.log"))
logger.write(SeverityType.DEBUG, "This is a test message!")
```

## Custom Policies
To create a custom policy, using the ILogPolicy interface to create a custom class that can then be used with the a Logger object. 