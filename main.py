import random
import secrets
def power(a,n,p):
	res=1;a=a%p
	while n>0:
		if n%2:res=res*a%p;n=n-1
		else:a=a**2%p;n=n//2
	return res%p
def isPrime(n,k=3):
	if n==1 or n==4:return False
	elif n==2 or n==3:return True
	else:
		for i in range(k):
			a=random.randint(2,n-2)
			if power(a,n-1,n)!=1:return False
	return True
	
def __egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = __egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def __modinv(a, m):
    g, x, y = __egcd(a, m)
    if g != 1:
        raise Exception
    else:
        return x % m
	
def geted(phi):
    e = 65537
    d = __modinv(e, phi)
            #e += 1
            #while not isPrime(e):
            #    e += 1
    return (e, d)

def encrypt(message, e, n):
    message = message ** e % n
    return message
    
def decrypt(encrypted, d, n):
    message = encrypted ** d % n
    return message

class Person():
    def __init__(self):
        self.p = 10
        self.q = 10
        while not isPrime(self.p):
            self.p = secrets.randbits(32)
        while not isPrime(self.q):
            self.q = secrets.randbits(32)
        self.n = self.p * self.q
        self.phi = (self.p-1)*(self.q-1)
        self.e, self.d = geted(self.phi)
        
        self.public_key = (self.e, self.n)
        self.private_key = self.d
        
guy = Person()
print('Public: ', guy.public_key, '\nPrivate: ', guy.private_key, sep='')

encrypted = encrypt(12345, guy.e, guy.n)
print(f'Encrypted message: {encrypted}')

decrypted = decrypt(encrypted, guy.d, guy.n)
print(f'Decrypted message: {decrypted}')
