path = 'data'

try:
    data = eval(open(path,'r').read())
except:
    open(path,'w').write('{}')
    data = eval(open(path,'r').read())

def AddData(key,value):
    data[key] = value
    file = open('data','w')
    file.write(str(data))
    file.close()

def GetData(key):
    if not key in data:
        return False
    return data[key]

def RemoveData(key):
    if not key in data:
        return False
    data.pop(key)
    file = open('data','w')
    file.write(str(data))
    file.close()

def GetAllData():
    return data

