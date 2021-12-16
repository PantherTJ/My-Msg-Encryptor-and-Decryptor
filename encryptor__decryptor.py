import random 

# class that encodes and decodes the code`
class encoder:
	# alphabets into numbers

	global alphabets
	alphabets = [{'1':'Aa'},{'2':'Bb'},{'3':'Cc'},{'4':'Dd'},{'5':'Ee'},{'6':'Ff'},{'7':'Gg'},	
	{'8':'Hh'},{'9':'Ii'},{'10':'Jj'},{'11':'Kk'},{'12':'Ll'},{'13':'Mm'},{'14':'Nn'},{'15':'Oo'},
	{'16':'Pp'},{'17':'Qq'},{'18':'Rr'},{'19':'Ss'},{'20':'Tt'},{'21':'Uu'},{'22':'Vv'},
	{'23':'Ww'},{'24':'Xx'},{'25':'Yy'},{'26':'Zz'},{'0':'  '}]

	# A kind of semi enocoder, it makes words from leter into number with 1's and 2's at
	# the end that tell the digits of the numbers in sequence and then with a 0 and then 
	# some numbers we say how many indexes to go back to start getting the actual numbers  
	# instead of the 1's and 2's that tell the digit


	def da_encoder(self,msg):
		# the var for numbers from letters
		enc = ''
		# the var for the digits it takes (1's and 2's)
		d_digits =''
		# var for counting the digits and then adding with the d_digits in string form
		d = 0
		# stores the ecryption key
		global enc_key
		enc_key = ''

		#checks what number the letter represents in the msg var
		#msg = input()
		for i in msg:
			for j in range(len(alphabets)):
				letter = list(alphabets[j].items())
				# tells when to stop and start search for the no. of the other letters
				if i in letter[0][1]:
					n = random.randint(1,6)
					
					j = int(j) + n
					if j > 26:
						j = j % 26
					else:
						j = int(j) + n


					enc_key +=  str(n)

					enc+=str(j)
					# the digit counter part
					d = 0

					for l in str(j):
						d+=1
					# d adds to d_digits to represent digits
					d_digits+=str(d)	


					break 

		# prints the semi encoded message, the digits and the other info talked about earlier 
		# all in one line

		# puts the encryption key in the file
		file = open('encryption_key.txt','w')
		key = file.write(enc_key)
		file.close()
		

		#print(f'the endcoded with more info {enc + d_digits + "0" + str(len(d_digits))}')
		return enc + d_digits + "0" + str(len(d_digits))


	def da_decoder(self,encoded_msg,enc_key):
		
		# formatting list has all the things in the encoded msg in a list
		# go_back_num carries info of what index to start at to get 
		# the info of digits or the info of the letters turned into numbers
		# da_digits gives info of how many digits a value contains to represent
		# a letter, we use it divide the encoded msg into smaller numbers which
		# represent the letters
		# da_dg_dg has the no of the digits the da_digits variable has

		formatting_list = [x for x in encoded_msg]
		go_back_num = ''
		da_message = ''
		da_digits = ''
		da_dg_dg = 0

		# gives the go_back_number and the da_dg_dg number value 
		for i in range(len(formatting_list)):
			if '0' in formatting_list[- 1 - i]:
				break
			else: 
				go_back_num += formatting_list[- 1 - i]
				da_dg_dg +=1
		# inverses it 
		go_back_num = go_back_num[::-1]				
		
		# the two while loops below divide the encoded msg into the number
		# representing the letter part and the numbers that divide the 
		# other numbers into numbers that represent certain letters 
		
		# the loop for division of numbers representing letters
		i = 0	
		while (- da_dg_dg - 1 - int(go_back_num) - 1 - i) != -(len(formatting_list)) -1:
			da_message += formatting_list[- da_dg_dg - 1 - int(go_back_num) - 1 - i]	
			i+=1
		# the loop for division of numbers that represent digit value
		i = 0
		while (- da_dg_dg - 1 - int(go_back_num) + i) != (- da_dg_dg - 1):
			da_digits+= formatting_list[- da_dg_dg - 1 - int(go_back_num) + i]
			i+=1 
		
		# the list that contains the message part in a list
		formatting_list1 = [x for x in da_message]
		# the list that contains the digit part in a list
		form_li_dig = [x for x in da_digits]

		#---------------------------
		# its reversed
		formatting_list1.reverse()
		# it will  have the message part divided into numbers divided into
		# letters 
		actual_no_list = []
		# it is used to start at an index and stop at and idex so that
		# the list above can get the value right
		y = 0
		# it will contain the final decoded message
		dec_msg = ''

		# the part that appends the the letter-numbers
		for x in form_li_dig:
			n = ''
			for i in range(y,y+int(x)):
				n += formatting_list1[i]
			actual_no_list.append(n)
			y = y+ int(x)
		
		# the part that adds the decoded msg to a variable
		p = 0
		enc_key_l = [x for x in enc_key]

		for i in actual_no_list:
			i = int(i) - int(enc_key_l[p])
			if i < 0:
				i = 27 - i
			else:
				i = int(i) - int(enc_key_l[p])
			i+=1
			i = str(i)
			for j in range(len(alphabets)):
				letter = list(alphabets[j].items())
				# tells when to stop and start search for the no. of the other letters
				if i in letter[0][0]:
					dec_msg += letter[0][1][1]					
					break 

			p+=1



		#print(f'this is actual_no_list {actual_no_list}')
		# this took more than a week, finally its done :O
		return (dec_msg)

		


# calls the class methods 
"""msg = input()
my_msg = encoder()
print(my_msg.da_decoder(my_msg.da_encoder(msg)))"""