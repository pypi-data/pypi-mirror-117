import requests

URL = 'http://192.145.238.5/~pasirm5/booru-armor/'


class Load(object):
    def __init__(self, api_key: str = ''):
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}


    def search(self, tags: str, limit: int, pid: int, block: str):
        """Gelbooru search"""
        self.specs['tags'] = tags
        self.specs['limit'] = limit
        self.specs['pid'] = pid
        self.specs['block'] = block

       
        data = requests.get(URL + 'gelbooru', params=self.specs)
        return data.json()

