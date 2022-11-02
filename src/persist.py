from typing import Any 

class Persist:
    def __init__(self, fname: str ='db.json'):
        self.data: dict[str,list[dict[Any, Any]]]= dict()
        self.fname = fname
            
    def _save(self):
        with open(self.fname, 'w') as fn:
            json.dump(self.data, fn)
    def add(self, key: str, data: dict):
        if self.data.get(key):
            self.data[key].append(data)
        else:
            self.data[key] = [data]
        self._save()
    def get(self, key: str):
        return self.data[key]
    def get_all(self):
        return self.data