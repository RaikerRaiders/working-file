# from itertools import *

# for i in product('01', repeat=4):
# 	i = list(map(int, i))
# 	x, y, w, z = i[0], i[1], i[2], i[3]
# 	F = (w or x or not (z) or y)*(w or x or not (z) or not (y))*(w or not (x) or not (z) or not (y))
# 	if F == 0:
# 		print(w, y, z, x)

# def convert(n):
# 	st = ''
# 	m = 0
# 	while 7**(m + 1) <= n:
# 		m += 1
# 	for i in range(m, -1, -1):
# 		k = n//(7**i)
# 		n -= k*(7**i)
# 		st += str(k)
# 	return st

# def backt(m):
# 	return sum([int(m[i])*(7**(len(m) - i - 1)) for i in range(len(m))])

# def zadacha(n):
# 	m = convert(n)
# 	if m.count('2') % 2 == 0:
# 		m += '555'
# 	else:
# 		m = '1' + m
# 	return backt(m)

# a = []

# for n in range(1, 4000):
# 	if zadacha(n) < 3799:
# 		a.append(n)


# print(max(a))

# from itertools import *

# k = 0
# for i in product('0123456', repeat=5):
# 	if i[0] != '0':
# 		if i.count('6') == 1:
# 			ch = sum([int(j) if int(j) % 2 == 0 else 0 for j in i])
# 			nech = sum(list(map(int, i))) - ch
# 			if ch < nech:
# 				print(i)
# 				k += 1
# print(k)

# f = open('9.txt')
# sts = f.readlines()
# nums = []
# for i in range(len(sts)):
# 	stn = list(map(int, sts[i].split()))
# 	x = None
# 	if len(set(stn)) == 5:
# 		for ch in stn:
# 			if stn.count(ch) == 3:
# 				x = ch
# 		if x != None:
# 			if x > sum(stn)/7:
# 				nums.append(i + 1)
# print(max(nums))

# a = []

# for i in range(4, 10000):
# 	n = '1' + '9' * i
# 	while ('19' in n) or ('49' in n) or ('999' in n):
# 		if '19' in n:
# 			n = n.replace('19', '9', 1)
# 		if '49' in n:
# 			n = n.replace('49', '91', 1)
# 		if '999' in n:
# 			n = n.replace('999', '4', 1)
# 	a.append(sum(int(i) for i in n))
# print(max(a))


def num(n, m):
	s = ''
	while n > 0:
		s = str(n % m) + s
		n //= m
	return s

# # Задача 1 - 296
# k = []
# for n in range(1, 1000):
# 	if n % 4 == 0:
# 		r = num(n, 4) + num(n, 4)[:2]
# 	else:
# 		r = num(n, 4) + num((n % 4) * 4, 4)
# 	if int(r, 4) > 291:
# 		k.append(int(r, 4))
# print(min(k))

# # Задача 2 - 1991
# k = []
# for n in range(1, 1000):
# 	if n % 3 == 0:
# 		r = '1' + num(n, 12) + 'B'
# 	else:
# 		r = '2' + num(n, 12) + '0'
# 	if int(r, 12) < 1996:
# 		k.append(int(r, 12))
# print(max(k))

# # Задача 3 - 9
# k = []
# for n in range(1, 1000):
# 	if num(n, 16).count('B') % 2 == 0:
# 		r = '1' + num(n, 16)
# 	else:
# 		r = num(n, 16) + '1'
# 	if len(str(int(r, 16))) == 2:
# 		k.append(int(r, 16))
# print(len(k))

# # Задача 4 - 9
# k = set()
# for n in range(100, 1001):
# 	r = bin(n)
# 	m = ''.join(r.split('0'))
# 	k.add(m)
# print(len(k))

# # Задача 5 - 72
# k = []
# for n in range(1, 101):
# 	r = int(bin(n)[2:])
# 	while r % 10 == 0:
# 		r //= 10
# 	m = str(r)[::-1]
# 	if int(m, 2) == 9:
# 		k.append(n)
# print(max(k))

# # Задача 6 - 102
# for n in range(1, 128):
# 	r = bin(n)[2:]
# 	s = '0'*(8 - len(r)) + r
# 	s = s.replace('0', 'a').replace('1', '0').replace('a', '1')
# 	if int(s, 2) == 153:
# 		print(n)

# import sys
# from math import *

# sys.setrecursionlimit(15000)

# # Задача 1 - 240757875872
# def f(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return (3 * n + 5) * f(n - 1)
# print(f(2073)/f(2070))

# # Задача 2 - 792
# def f(n):
# 	if n >= 2222:
# 		return n
# 	else:
# 		return n ** 3 + f(n + 2)
# print(f(4) - f(10))

# # Задача 3 - 6139
# def f(n):
# 	if n < 3:
# 		return 1
# 	elif n % 2 == 0:
# 		return f(n - 1) + n - 1
# 	else:
# 		return f(n - 2) + 2 * n - 2
# print(f(2048) - f(2045))

# # Задача 4 - 8896
# def f(n):
# 	if n < 10:
# 		return n - 1
# 	elif n % 2 == 0:
# 		return 3*n - 1 + f(n - 3)
# 	else:
# 		return 5*n + 2 + f(n - 4)
# print(f(4445) - f(4444))

# # Задача 5 - 4092529
# def f(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * f(n - 1)
# print((f(2024) - f(2023))/f(2022))

# # Задача 6 - 1019592
# def f(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return 2 * n * f(n - 1)
# # print((f(2024)/16 - f(2023))/f(2022))
# print(2023*504)
# # не работает, посчитал вручную

# # Задача 7 - 2446
# def f(n):
# 	if n > 10000:
# 		return n - 10000
# 	else:
# 		return f(n + 1) + f(n + 2)
# # print(f(12345) * (f(10) - f(12))/f(11) + f(10101))
# print(2345 + 101)
# # не работает, посчитал вручную

# # Задача 8 - 1
# def f(n):
# 	if n >= 2010:
# 		return n
# 	else:
# 		return f(n + 1) + f(n + 2) + f(n + 3)
# print((f(2000) - 2*(f(2002) + f(2003)))/f(2004))

# # Задача 9 - 8750
# def f(n):
# 	if n >= 5000:
# 		return factorial(n)
# 	else:
# 		return 2*f(n + 1)/(n + 1)
# # print(1000*f(7)/f(4))
# print(1000*7*6*5/24)
# # не работает, посчитал вручную

# # Задача 10 - 1683
# def f(n):
# 	if n >= 10000:
# 		return n
# 	elif n % 3 == 0:
# 		return n + f(n/3)
# 	else:
# 		return 2*n + f(n + 3)
# print(f(999) - f(46))

# # Задача 11 - 1024
# def f(n):
# 	if n == 1:
# 		return 2
# 	else:
# 		return 2 * f(n - 1)
# print(f(1900)/2**1890)

# # Задача 12 - 8174947
# def f(n):
# 	if n < 3:
# 		return n
# 	else:
# 		return n - 1 + f(n - 1)
# print(f(4044))

# # Задача 13 - 102697
# def f(n):
# 	if n == 1:
# 		return 2
# 	else:
# 		return f(n - 1) + 5*n**2
# print(f(39))

# # Задача 14 - 4122
# def f(n):
# 	if n == 1:
# 		return 1
# 	elif n % 2 == 0:
# 		return n + f(n - 1)
# 	else:
# 		return 2*f(n - 2)
# print(f(26))

# # Задача 15 - 180224
# def f(n):
# 	if n <= 10:
# 		return n
# 	elif n <= 36:
# 		return n//4 + f(n - 10)
# 	else:
# 		return 2*f(n - 5)
# print(f(100))

# # Задача 16 - 12
# def f(n):
# 	if n < 3:
# 		return n
# 	elif n % 2 == 0:
# 		return int((n + f(n - 2))/5)
# 	else:
# 		return int((2*n + f(n - 1) + f(n - 2))/4)
# print(f(50))

# # Задача 17 - 32804
# k = []
# def f(n):
# 	if n < 2:
# 		return 1
# 	elif n % 3 == 0:
# 		return f(n / 3) - 1
# 	else:
# 		return f(n - 1) + 7
# # for i in range(1, 1000000):
# # 	if f(i) == 111:
# # 		k.append(i)
# # print(min(k))

# # Задача 18 - 120
# k = 0
# def f(n):
# 	if n == 0:
# 		return 0
# 	elif n % 2 == 0:
# 		return f(n / 2)
# 	else:
# 		return 1 + f(n - 1)
# for n in range(1, 1001):
# 	if f(n) == 3:
# 		k += 1
# print(k)

# # Задача 19 - 10229
# def f(n):
# 	if n < 3:
# 		return 1
# 	elif n % 2 != 0:
# 		return f(n - 1) + n
# 	else:
# 		return f(n - 3) + 2*n
# print(f(2048) - f(2041))

# # Задача 20 - 12114
# def f(n):
# 	if n < 3:
# 		return 3
# 	else:
# 		return 2*n + 5 + f(n - 2)
# print(f(3027) - f(3023))

# # Задача 21 - 21
# def f(n):
# 	if n >= 10000:
# 		return n
# 	elif n % 2 == 0:
# 		return f(n + 2) - 3
# 	else:
# 		return f(n + 2) + 1
# print(f(94) - f(80))

# # Задача 22 - 346
# def f(n):
# 	if n > 3000:
# 		return 1
# 	elif n % 2 == 0:
# 		return f(n + 1) - n + 1
# 	else:
# 		return f(n + 2) - 2*n + 2
# print(2*(f(39) - f(34)))

# # Задача 23 - 
# def f(n):
# 	if n < 3:
# 		return n
# 	elif n % 2 != 0:
# 		return f(n - 1) + f(n - 2) + 1
# 	else:
# 		return sum([f(i) for i in range(1, n)])
# # print(f(38))
# # не считается, вручную впадлу считать, сами считайте, код верный

# # Задача 24 - 
# def f(n):
# 	if n <= 2:
# 		return 1
# 	elif n % 2 != 0:
# 		return f(n - 1) - n
# 	else:
# 		return f(n - 2) + g(n - 1) + 2

# def g(n):
# 	if n <= 0:
# 		return 2
# 	elif n % 2 != 0:
# 		return f(n - 1) - 2*g(n - 1)
# 	else:
# 		return 2*f(n - 2) - 2*g(n - 1)
# # print(f(96))
# # не считается, вручную впадлу считать, сами считайте, код верный

# # Задача 25 - 81
# k = []
# def f(n):
# 	if n <= 1:
# 		return 1
# 	elif n % 3 == 0:
# 		return n + f(n/3)
# 	else:
# 		return n + f(n + 3)
# # for n in range(1, 1000):
# # 	try:
# # 		if f(n) > 100:
# # 			k.append(n)
# # 	except RecursionError:
# # 		k.append(10000)
# # print(min(k))

# # Задача 26 - 216
# k = 0
# def f(n):
# 	if n < 3:
# 		return n + 1
# 	elif n % 2 == 0:
# 		return f(n - 2) + n - 2
# 	else:
# 		return f(n + 2) + n + 2
# # for n in range(2, 10001, 2):
# # 	try:
# # 		if len(str(f(n))) == 5:
# # 			k += 1
# # 	except RecursionError:
# # 		continue
# print(k)

# # Задача 27 - 2462
# def f(n):
# 	if n >= 3210:
# 		return 1
# 	else:
# 		return f(n + 3) + 7
# def g(n):
# 	if n < 10:
# 		return n
# 	else:
# 		return g(n - 3) + 5
# print(f(15) - g(3000))

# # Задача 28 - 123
# def f(n):
# 	if n >= 10000:
# 		return n
# 	elif n % 6 == 0:
# 		return n/6 + f(n/6 + 2)
# 	else:
# 		return n + f(n + 2)
# print(f(264) - f(7))

# # Задача 29 - 9
# def f(n):
# 	if n == 1:
# 		return 2
# 	else:
# 		return f(n - 1) * (3**(n % 5))/(3**(n % 7))
# # print(f(1025)/f(1030))
# # не работает, вручную посчитал

# # Задача 30 - 1065509
# def f(n):
# 	if n < 2:
# 		return n
# 	else:
# 		return f(n // 2) * 10 + n % 2
# for n in range(1, 10000000):
# 	if f(n) == 100000100001000100101:
# 		print(n)
# 		break

# # Задача  - 
# def f(n):
# 	if n :
# 		return 
# 	elif n :
# 		return 
# 	else:
# 		return 
# print()

from itertools import *

# print('d c b a')
# for i in product('01', repeat=4):
# 	a, b, c, d = int(i[0]), int(i[1]), int(i[2]), int(i[3])
# 	if ((not a) or b) and ((not b) or (not c)) and (c or d) == 1:
# 		print(d, c, b, a)

# k = []

# def num(n):
# 	s = ''
# 	while n > 0:
# 		s = str(n % 3) + s
# 		n //= 3
# 	return s

# for n in range(1, 1000):
# 	if n % 2 == 0:
# 		m = '2' + num(n) + num(int(num(n)[-1]) * 2)
# 	else:
# 		m = num(int(num(n)[0]) * 2) + num(n) + '2'
# 	if int(m, 3) > 100:
# 		k.append(int(m, 3))
# print(min(k))

from math import *

# k = []

# for x in range(21):
# 	for y in range(21):
# 		if (9*21**8 + 4*21**7 + 3*21**6 + 6*21**5 + 9*21**4 + 7*21**3 + x*21**2 + 2*21 + 1 - 2*21**5 - y*21**4 - 9*21**3 - 2*21**2 - 5*21 - 3) % 20 == 0:
# 			k.append(x - y)
# print((9*21**8 + 4*21**7 + 3*21**6 + 6*21**5 + 9*21**4 + 7*21**3 + 20*21**2 + 2*21 + 1 - 2*21**5 - 0*21**4 - 9*21**3 - 2*21**2 - 5*21 - 3)/20)

import sys

sys.setrecursionlimit(15000)

# def f(n):
# 	if n < 7:
# 		return 7
# 	elif n % 3 == 0:
# 		return 3 + f(n - 1)
# 	else:
# 		return 5 - f(n - 1)
# print(f(3015))

# nums = list(map(int, list(open('17-3.txt'))))

# k = []
# c = 0
# for num in nums:
# 	if len(str(num)) == 2 and num % ((num // 10) + (num % 10)) == 0:
# 		k.append(num)
# minim = min(k)
# for i in range(len(nums) - 1):
# 	if nums[i] % minim == 0 or nums[i + 1] % minim == 0:
# 		c += 1
# print(c)

# def f(n):
# 	if n == 49:
# 		return 1
# 	elif n >= 50:
# 		return 0
# 	elif n == 13:
# 		return 0
# 	return f(n + 2) + f(3*n) + f(n**2)
# print(f(3))

# for x, y, z in product('0123456789', repeat=3):
# 	num = int('12' + x + '345' + y + '67089' + z)
# 	if num % 206 == 0:
# 		print(num, num // 206)

# ----------------------------------------------
# Задание 26

f = open('26.txt')
n = f.readline()
seats = f.readlines()
for i in range(len(seats)):
	seats[i] = list(map(int, seats[i].split()))
sts = []
for i in range(1, 1000):
	sits = [seat[1] for seat in seats if seat[0] == i]
	for j in range(1, 996):
		if set(sits).intersection(set([j, j + 1, j + 2, j + 3, j + 4])) == set():
			if (j - 1) in sits or (j + 5) in sits:
				if max(sits) > j + 4:
					sts.append([i, j])
maxrow = sorted(sts)[::-1][0][0]
minsit = min([s[1] for s in sts if s[0] == maxrow])
print(maxrow, minsit)
# ----------------------------------------------

