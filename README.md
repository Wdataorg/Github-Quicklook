# Github-Quicklook
![https://img.shields.io/github/issues/Wdataorg/Github-Quicklook](https://img.shields.io/github/issues/Wdataorg/Github-Quicklook)
![https://img.shields.io/github/forks/Wdataorg/Github-Quicklook](https://img.shields.io/github/forks/Wdataorg/Github-Quicklook)
![https://img.shields.io/github/stars/Wdataorg/Github-Quicklook](https://img.shields.io/github/stars/Wdataorg/Github-Quicklook)
![https://img.shields.io/github/license/Wdataorg/Github-Quicklook](https://img.shields.io/github/license/Wdataorg/Github-Quicklook)
![https://www.murphysec.com/platform3/v3/badge/1612817586031460352.svg?t=1](https://www.murphysec.com/platform3/v3/badge/1612817586031460352.svg?t=1)

- [简单介绍](#简单介绍)
- [使用方法](#使用方法)
- [官方网站](#官方网站)
- [API接口的使用方法](#API接口的使用方法)

## 简单介绍
使用`api.github.com`作为接口，快速查看Github星星数等信息
`api.github.com`是Github的api接口

## 使用方法

下载后会有一个`Github信息快速查看器.exe`的文件，这就是软件，双击打开后，输入仓库的拥有者，以及仓库名，即可查看相关信息

## 官方网站

Github-Quicklook官方网站:[https://Wdataorg/Github-Quicklook](https://Wdataorg/Github-Quicklook)

## API接口的使用方法

我们将使用Python代码实现

### 解析

> 以下属于进阶内容，讲解的是本项目的实现方法

```python
from requests import get # 导入请求函数
response = get('https://api.github.com/repos/{UserName}/{RepoName}') # 向API接口请求
print(response.content) 
```

以`Wdataorg/Github-Quicklook`为例，输出是这样

```
PS D:\Github-Quicklook> & C:/Users/S.X.Y/AppData/Local/Programs/Python/Python38-32/python.exe d:/Github-Quicklook/test/test.py
b'{"id":536071343,"node_id":"R_kgDOH_PMrw","name":"Github-Quicklook","full_name":"Wdataorg/Github-Quicklook","private":false,"owner":{"login":"Wdataorg","id":107593423,"node_id":"O_kgDOBmm-zw","avatar_url":"https://avatars.githubusercontent.com/u/107593423?v=4","gravatar_id":"","url":"https://api.github.com/users/Wdataorg","html_url":"https://github.com/Wdataorg","followers_url":"https://api.github.com/users/
......(太多了)
```

他的格式是json, 没法直接使用，还得**转换**成`dict`

以下是转化的代码
```python
json_data = response.content
import json # 导入Json类
dict_data = json.loads(json_data) # 转化成Dict类型
print(type(dict_data)) # 打印类型
```

输出是`<class 'dict'>`，得到了`Dict`类型的数据，我们就可以直接分析了！

但我们要了解网页返回的`json`类型中的一些数据

```
eg.                     类型
"size":11671            显示仓库大小
"forks_count":0         显示仓库fork数量
"stargazers_count": 1   显示仓库Star数量
"watchers_count": 1     显示仓库Watch数量
```
了解了这些信息，我们就可以补全查询仓库信息的代码

```python
print('星星数量\tWatch数量\tFork数量\t仓库大小')
print('{}\t{}\t{}\t{}'.format(dict_data['stargazers_count'], dict_data["watchers_count"], dict_data["forks_count"],dict_data["size"])) # 打印信息
```

完整代码如下：

```python
from requests import get # 导入请求函数
response = get('https://api.github.com/repos/Wdataorg/Github-Quicklook') # 向API接口请求
json_data = response.content
import json
dict_data = json.loads(json_data)
print('星星数量\tWatch数量\tFork数量\t仓库大小')
print('{}\t{}\t{}\t{}'.format(dict_data['stargazers_count'], dict_data["watchers_count"], dict_data["forks_count"],dict_data["size"])) # 打印信息
```

输出如下：

```
PS D:\Github-Quicklook> & C:/Users/S.X.Y/AppData/Local/Programs/Python/Python38-32/python.exe d:/Github-Quicklook/test/test.py
星星数量        Watch数量       Fork数量        仓库大小
1              1              0               11671
```
