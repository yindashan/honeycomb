# -*- coding:utf-8 -*-
##################################
# Vigenere 是一种多码加密法
# author vearne
# ***注意***:
# 1) 字母表中必须要包含明文中出现的字母
# 2) 密钥不能为空
# 3) 字母表中的字母不应当重复
##################################
class Vigenere(object):
    def __init__(self, table='0123456789', key='apple'):
        # 字母表
        self.table = table
        # 密钥
        self.key = key
        
    def genNum(self, curr):
        if curr + 1 >= len(self.key):
            return 0
        else:
            return curr + 1
            
    def dict(self, chr, move):
        index = self.table.index(chr)
        return self.table[(index + move) % len(self.table)]
     
    def encrypt(self, cleartext):
        # i 指向明文, j 指向密钥
        j = 0
        ll = []
        for i in range(len(cleartext)):
            move = ord(self.key[j]) % len(self.table)
#            print 'move', move
            new_chr = self.dict(cleartext[i], move)
            ll.append(new_chr)
            j = self.genNum(j)
        return ''.join(ll)
            
    def decrypt(self, ciphertext):
        # i 指向密文, j 指向密钥
        j = 0
        ll = []
        for i in range(len(ciphertext)):
            move = ord(self.key[j]) % len(self.table)
            move = move * (-1)
            new_chr = self.dict(ciphertext[i], move)
            ll.append(new_chr)
            j = self.genNum(j)
        return ''.join(ll)
        
if __name__ == '__main__':
    v = Vigenere(table='0152893647', key='apple')
    cleartext = '0000106861'
    print cleartext
    ciphertext = v.encrypt(cleartext)
    print ciphertext
    print '----------------------------------'
    cleartext = v.decrypt(ciphertext)
    print cleartext

