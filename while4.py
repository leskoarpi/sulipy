'''4. Feladat
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!'''
szöveg = input('szöveg:')
szam = input("hanyszor?")
szam = int(szam)
i = 0
while i < szam:
  print(szöveg)
  i = i + 1
