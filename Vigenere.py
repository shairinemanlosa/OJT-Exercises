import cProfile

class Vigenere_Cipher:
	def __init__(self):
		self.alphabet = "abcdefghijklmnopqrstuvwxyz1234567890 "
		self.list_alphabet = []
		self.size = 0
		

	def mix_alphabet(self):
		keyword = "excalibur"
		new_keyword = ""
		temp_key = []

		for i in self.alphabet:
			if i not in keyword:
				new_keyword += i
		new_keyword = keyword + new_keyword

		for i in xrange(0, len(new_keyword), 5):
			temp_key.append(new_keyword[i:i+5])
		
		for j in xrange(len(temp_key[0])):
			for i in xrange(len(temp_key)):
				if i < len(temp_key) and j < len(temp_key[i]):
					self.list_alphabet.append(temp_key[i][j])
		return self.list_alphabet

	def generate_table(self, alphabet):
		temp = []
		for i in alphabet:
			temp.append(alphabet[alphabet.index(i):] + alphabet[:alphabet.index(i)])

		return temp

	def encrypt(self, text, password):
		index = 0
		table = self.generate_table(self.mix_alphabet())
		encrypted_text = ""

		for i in xrange(0, len(text)):
			if text[i] not in self.alphabet:
				print "Invalid"
				return
			else:
				if index == len(password):
					index = 0
				text_index = text[i]
				pass_index = password[index]
				t_index = self.alphabet.index(text_index)
				p_index = self.alphabet.index(pass_index)
				encrypted_text += table[t_index][p_index]
				index += 1
		print encrypted_text

	def decrypt(self, text, password):
		index = 0
		decrypted_text = ""
		table = self.generate_table(self.mix_alphabet())
		for i in xrange(0, len(text)):
			if text[i] not in self.alphabet:
				print "Invalid"
				return 
			else:
				if index == len(password):
					index = 0
				text_index = text[i]
				pass_index = password[index]
				p_index = self.alphabet.index(pass_index)
				t_index = self.alphabet.index(text_index)
				find_text = table[p_index]
				result = find_text.index(text_index)
				decrypted_text += self.alphabet[result] 
				index += 1
		print decrypted_text



password = Vigenere_Cipher()
message = "now is the time for all good men to come to the aid of their fellow man"
encrypted_message = "uer9opefrx72xatejd27fn700yd076sr0vyc5e6sgw o9nwieoney7mzbsojej2 yc7gviq"
key = "excalibur"

cProfile.run("encrypted = password.encrypt(message, key)")
cProfile.run("decrypted = password.decrypt(encrypted_message, key)")

print encrypted
print decrypted