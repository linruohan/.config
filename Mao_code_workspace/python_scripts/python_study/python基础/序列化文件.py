import pickle,json
d=dict(name='xiaohan',s=123,score=100)

# print(pickle.dumps(d))
with open("dump.txt",'wb') as f:
    pickle.dump(d,f)

with open("dump.txt",'rb') as f:
    b=pickle.load(f)
    # print(b)

# print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))
class Student(object):
    """docstring for ."""
    def __init__(self, name,age,score):
        super(object, self).__init__()
        self.name = name
        self.age = age
        self.score = score

def student_json(s):
    return {
    'name':s.name,
    'age':s.age,
    'score':s.score,
    }
def student_json_2(d):
    return Student(d['name'],d['age'],d['score'])
s=Student('Bob','12','65')
#序列化
print(json.dumps(s,default=student_json))
#反序列化
print(json.loads(json_str, object_hook=student_json_2))
