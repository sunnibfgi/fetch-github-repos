
import requests
import sys

try:
    import json
except ImportError:
    import simplejson as json


def github_repos_fetch():
    req = requests.get('https://api.github.com/users/%s/repos' % sys.argv[1])
    if req.status_code == 200:
        data = json.loads(req.content)
    return data


def data_write_to_file():
    obj = {}
    new_user_list = []
    try:
        user_list = github_repos_fetch()
    except UnboundLocalError:
        exit(1)

    if not len(user_list):
        print('data is empty!')
        exit(1)

    for i, item in enumerate(user_list):
        new_user_list.append({
            'id': item['id'],
            'name': item['name'],
            'url': item['html_url'],
            'language': item['language']
        })
    obj['repos_info'] = new_user_list
    obj['count'] = len(user_list)
    json.dump(obj, open('%s.json' % sys.argv[1], 'w'), indent=2)


if __name__ == '__main__':
    data_write_to_file()
