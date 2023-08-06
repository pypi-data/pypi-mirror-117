#  Django_Logging_Headers
This package is based on The Django logging feature, with patched support for logging request header data
该包基于django日志功能，通过打补丁的方式支持记录请求头数据
## Install
```
pip install django-logging-headers
```

## Use
In app entry file:
```
import django_logging_headers as logging

logger.info("success", request=self.request, keys=["HTTP_EAGLEEYE_TRACEID"])
```