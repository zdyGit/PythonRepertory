import string
import random


def actication_code(key,length=20):
	head = hex(key)[2:]
	head = head+"HW"
	chars = string.ascii_letters+string.digits
	l = length-len(head)
	tail = ''.join([random.choice(chars) for i in range(l)])
	return head+tail
