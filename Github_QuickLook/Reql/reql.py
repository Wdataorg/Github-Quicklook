import json
import requests


def reql(owner, repo):
    reql_url = 'https://api.github.com/repos/{}/{}'.format(owner, repo)
    response = requests.get(reql_url)
    json_response = json.loads(response.content)
    if len(json_response) == 2:
        return
    
    else:
        return json_response
