from requests import get # 导入请求函数
response = get('https://api.github.com/repos/Wdataorg/Github-Quicklook') # 向API接口请求
json_data = response.content
import json
dict_data = json.loads(json_data)
print('星星数量\tWatch数量\tFork数量\t仓库大小')
print('{}\t{}\t{}\t{}'.format(dict_data['stargazers_count'], dict_data["watchers_count"], dict_data["forks_count"],dict_data["size"])) # 打印信息