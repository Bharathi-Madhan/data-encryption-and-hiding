import random
import time
import steganography as s

#Euclid's algorithm for determining the greatest common divisor
def gcd(a, b):
    while not b == 0:
        a, b = b, a % b
    return a

#Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def multiplicative_inverse(e, phi):
    for i in range(phi):
        if ((e*i)%phi) == 1:
            return i

#Tests to see if a number is prime.
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

#Given two prime numbers, generate a new keypair.
def generate_keypair(p, q):
    # validate input
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = (p-1) * (q-1)

    # choose an integer e such that e and phi(n) are co-prime
    e = random.randrange(1, phi)

    # use Euclid's Algorithm to verify that e and phi(n) are co-prime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # return public and private keypair
    # public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

#Encrypt a given message using the public key provided.
def encrypt(pk, plaintext):
    # unpack the key into it's components
    
    key, n = pk
    # convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [
        (ord(char) ** key) % n \
            for char in plaintext]
    # return the array of bytes
    
    
    return cipher

#Decrypt an cipher using the private key provided.
def decrypt(pk, ciphertext):
    # unpack the key into its components
    key, n = pk
    #ciphertext = ciphertext[:-1]
    # generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [
        chr((ord(char)) ** key % n) \
        for char in ciphertext]
    # return the array of bytes as a string
    return ''. join(plain)

#def print_seprator() -> None:
#    print('*'*75)

#def print_welcome() -> None:
#    print_seprator()
#    print('RSA Keypair Generator & Encrypter/Decrypter')
#    print_seprator()

#Run the RSA key generator

#print_welcome()
'''
list=[11,13,17,19,23,29]
n1=random.choice(list);
list.remove(n1)
n2=random.choice(list);
'''
def main1(temp1,temp2):
    start= time.time()
    public, private = generate_keypair(19,13)
    #print('Public  key', public)
    print('Private key', private)

    #convert the temp2 contents into a string message
    #def encrypt_rsa(p,q,r,file):
    with open(temp2,'r') as file1:
        message = file1.read()

    #message = input('\nEnter a message to encrypt with your private key: \n')
    encrypted_msg = encrypt(public,message)
    #print(encrypted_msg)
    #print(type(encrypted_msg))
    #print_seprator()

    #name=input("Enter the name of the cover image file(with extension):")
    #global newimg
    #print('Encrypted message:',''.join(map(lambda x: str(x),encrypted_msg)))
    #print(encrypted_msg)
    end= time.time()
    newimg, time2 =s.steganography_encode(encrypted_msg,temp1)
    etime= end- start
    etime= etime+ time2
    #data=s.steganography_decode(newimg)
    #print(data)
    #print('Decrypted message:',decrypt(public, data))
    #print_seprator()
    #print()
    #newimg=s.steganography_encode(encrypted_msg,'books.png')
    #data=s.steganography_decode(newimg)
    #print("Retrived data:\n")
    return etime
def main2(temp3,key1,key2):
    #public, private = generate_keypair(19,13)
    private=key1,key2
    data=s.steganography_decode(temp3)
    decrypted_msg=decrypt(private,data)
    file=open('new.txt','w')
    file.write(decrypted_msg)
    file.close()