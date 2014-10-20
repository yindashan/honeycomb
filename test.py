from vigen import Vigenere
def decorate(num, limit):
    num = str(num)
    cleartext = num
    for i in range(limit - len(num)):
        #cleartext = '0' + cleartext
        cleartext =  cleartext + '0'
    v = Vigenere(table='0152893647', key='Studyhardandmakeprogresseveryday')
    return 'GD' + v.encrypt(cleartext)

for i in range(10000):
	#print '################################'
	#print cleartext
	ciphertext = decorate(i, 10)
	print ciphertext
	#print '----------------------------------'
	#print cleartext
	


#for i in range(1000000):
#	cleartext = str(i)
#	#print '################################'
#	#print cleartext
#	ciphertext = v.encrypt(cleartext)
#	print ciphertext
#	#print '----------------------------------'
#	cleartext = v.decrypt(ciphertext)
#	#print cleartext
#	
