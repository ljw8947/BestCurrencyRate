import json
from flask import jsonify
class TC:
    va=1
    vb=2
    vc=3

t=TC()
t={'a':1,'b':2,'c':3,'d':[5,6,7,8]}
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(':')))