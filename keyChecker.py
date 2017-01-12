from msvcrt import getch
while True:
	key = getch()
	keyId = ord(key)
	print key + " is " + str(keyId)