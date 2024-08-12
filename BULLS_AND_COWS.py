import random
import os
from time import sleep
def terms():
	try:
		os.system('cls')
		term=int(input("HOW MANY COWS YOU WANT TO GUESS? : "))
		os.system('cls')
		return term
	except:
		os.system('cls')
		print("INVALID NUMBER")
		sleep(1)
		os.system('cls')
		return terms()
terms=terms()
def chan():
	try:
		cha=int(input("IN HOW MANY CHANCE YOU WANT TO GUESS? : "))
		os.system('cls')
		return cha
	except:
		os.system('cls')
		print('INVALID NUMBER')
		sleep(1)
		os.system('cls')
		return chan()
chan=chan()
def bc():
	x=[]
	for i in range(0,terms):
		n=random.randint(0,9)
		x.append(str(n))
	if len(set(x))==terms:
		a="".join(x)
		a=int(a)
		if len(str(a))!=terms:
			return bc()
		return x
	else:
		bc()
a=bc()
def bullsandcows(a,chan,terms):
	m=0
	while m!=chan:
		try:
			num=int(input('ENTER A NON REPETITIVE NUMBER: '))
			num=str(num)
			b=[]
			for i in num:
				b.append(i)			
				
			if len(set(b))==terms and len(b)==terms:
				c=[]
				for i in range(0,terms):
					if a[i]==b[i]:
						c.append("COW")
				d=set(a)&set(b)
				if len(c)==terms:
					print("""
	YOU GUESSED IT RIGHT!""")
					break
				elif len(d)>=len(c):
					k=len(d)-len(c)
					e=[]
					for i in range(k):
						e.append("BULL")
				if len(d)==0 and len(c)==0:
					print("NO BULLS , NO COWS")
					m+=1
				else:
					f=c+e
					print(f)
					m+=1
			else:
				print('INVALID NUMBER')
		except:
			print("INVALID NUMBER")
	return m


yo=bullsandcows(a,chan,terms)
if yo==chan:
	print("""
	BETTER LUCK NEXT TIME !!!""")
 
 
 
 
 