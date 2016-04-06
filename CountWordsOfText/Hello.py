import os


fileName = "test.txt"
fp = open(fileName)

Content = fp.read();
L = [',','.','!','<','>','(',')']

str = Content;
for item in L:
	str = str.replace(item,'')
str = str.lower()
Words = str.split(' ')


wordic = {}

def Count(Words):
	for item in Words:
		if wordic.get(item) == None:
			wordic[item] = 1
		else:
			wordic[item] = wordic[item]+1

Count(Words)
print(sorted(wordic.items(),key=lambda d:d[1],reverse=True))

fp.close()