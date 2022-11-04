# ! /usr/bin/env python
# _*_ coding: utf-8 _*_
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ALBERTGAMUS")
print("""
port aramaya hoşgeldiniz.
1)hızlı tarama
2)servis ve versiyon bilgisi
3)işletim sistemi bilgisi

""")
islem=input("işlem numarasını giriniz: ")

if(islem=="1"):
	hedefip=input("hedef ip giriniz: ")
	os.system("nmap " + hedefip)
	
elif(islem=="2"):
	hedefip=input("hedef ip giriniz: ")
	os.system("nmap -sS -sV" + hedefip)
	
elif(islem=="3"):
	hedefip=input("hedef ip giriniz: ")
	os.system("nmap -O" + hedefip)
else:
	print("hatali giriş program kapatılıyor")	
	
		
	
	
		
