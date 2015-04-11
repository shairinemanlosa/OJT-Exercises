def sieve_of_eratosthenes(num):
	list_num = range(2, num + 1)

	for i in list_num:
		if i != "x":
			x = i + 1
			while x <= num:
				if list_num[x - 2] != "x":
					if list_num[x - 2] % i == 0:
						list_num[x - 2] = "x"
				x += 1

	while "x" in list_num:
		list_num.remove("x")

	print list_num


sieve_of_eratosthenes(10)









