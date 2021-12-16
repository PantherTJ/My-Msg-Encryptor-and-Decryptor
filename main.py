from encryptor__decryptor import encoder
my_msg = encoder()

print('-----------------------------')
print('Please type your message here')
print('-----------------------------')
print('You can also type your encrypted message to be decrypted')
print('-----------------------------')
print('type "x" for encryption type "y" for decryption')

while True:
	da_decs = input()

	if da_decs == 'x':
		print("pls type your msg to be encoded")
		da_msg = input()
		print(f'the encoded msg is -- {my_msg.da_encoder(da_msg)}')
		print('-------------------------------------------------')
		break
	
	elif da_decs == 'y':
		print("pls type your encrypted msg to be decoded")
		da_msg = input()
		print(" pls type your encryption key")
		da_code = input()
		print(f'the results of decoding are -- {my_msg.da_decoder(da_msg,da_code)} ')
		break 
	
	elif  da_decs != 'x' or da_decs != 'y':
		print('type correctly')

	print('type "x" for encryption type "y" for decryption')

print('---------------------------------')
print('press any key to exit')
x =  input()

