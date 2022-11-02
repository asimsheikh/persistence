# Persistence

A library to create and store objects in python.

An example of using the library 

```python
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

rand = User(first_name='Rand', last_name='Al Thor', age=24)
matt = User(first_name='Matt', last_name='Cauthon', age=23)

db = Persist()

db.add(key='users', data=rand.dict())
db.get(key='users')

assert db.get(key='users') == [rand.dict()]

db.add(key='users', data=matt.dict())

assert db.get_all() == {'users': [rand.dict(), matt.dict()] }
```
