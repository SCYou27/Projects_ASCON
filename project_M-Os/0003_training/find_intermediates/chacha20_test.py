import chacha20
key = '0'*80
nonce = '0'*16
print(chacha20.ChaCha20(key+nonce))

key = '0'*57+'1'+'0'*22
nonce = '0'*16
print(chacha20.ChaCha20(key+nonce))

key = '0'*80
nonce = '0'*9+'1'+'0'*6
print(chacha20.ChaCha20(key+nonce))

key = '0'*80
nonce = '0'*7+'1'+'0'*8
print(chacha20.ChaCha20(key+nonce))

A = '0000000000000000000000000000000000000000000000000000000000000001'
print(len(A))
