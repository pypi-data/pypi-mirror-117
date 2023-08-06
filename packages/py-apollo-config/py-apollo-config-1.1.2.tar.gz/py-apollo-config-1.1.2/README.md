# 携程 Apollo(阿波罗) 配置库

### 说明

这是一个携程 Apollo(阿波罗) 配置获取库，支持环境变量和用户自定义配置。

配置优先级(可通过参数控制)：环境变量 > 阿波罗 > 自定义

### 链接

- [GitHub](https://github.com/ztj1993/py-apollo-config)
- [PyPI](https://pypi.org/project/py-apollo-config)

### 安装

```
pip install py-apollo-config
```

### 依赖

```
pip install config-registry
pip install py-apollo-client
```

### 使用

初始化：

```
import os

from ApolloClient import ApolloClient
from ApolloConfig import ApolloConfig
from ConfigRegistry import ConfigRegistry

os.environ.setdefault('ENV_PREFIX_APOLLO', 'apollo')
os.environ.setdefault('APOLLO_URI', 'http://192.168.68.251:8080')
os.environ.setdefault('APOLLO_APPID', 'equipment-services')

config = ApolloConfig(prefix='{环境变量前缀}')
#config.setting = ConfigRegistry()
#config.apollo = ApolloClient()
config.init()
```

获取配置：

```
config.get('debug', default=False, apollo=False, env=Fals)
```
