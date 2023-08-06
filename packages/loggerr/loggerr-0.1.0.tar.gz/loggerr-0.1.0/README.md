# loggerr [![](https://img.shields.io/pypi/v/loggerr?style=flat-square)](https://pypi.org/project/loggerr/) [![](https://img.shields.io/static/v1?label=github&message=loggerr&labelColor=black&color=3572a5&style=flat-square&logo=github)](https://github.com/fiverr/loggerr) [![](https://circleci.com/gh/fiverr/loggerr.svg?style=svg)](https://circleci.com/gh/fiverr/loggerr)

```py
from loggerr import Loggerr

logger = Loggerr("warn")
logger.info("Something going as expected", { "host": socket.gethostname() }) # ignored
logger.error("Something must have gone terribly wrong") # sent
```
