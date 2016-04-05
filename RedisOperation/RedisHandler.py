from CreateActivationCode import actication_code
import redis

db = redis.StrictRedis(host="127.0.0.1",port=6379,db=3)

L = [actication_code(i,8) for i in range(200)]

def getID(code):
 	strid = code.split('HW')[0]
 	return int(strid,16)

def SaveToRedis(L):
 	for item in L:
 		key = getID(item)
 		value = item
 		db.set(key,value)

SaveToRedis(L)

print(db.get(50).decode())

