def hammingGeneratorMatrix(r):		#Generator matrix for Hamming codes, given as part of the assignment.
	n = 2**r-1
	
	#construct permutation pi
	pi = []
	for i in range(r):
		pi.append(2**(r-i-1))
	for j in range(1,r):
		for k in range(2**j+1,2**(j+1)):
			pi.append(k)

	#construct rho = pi^(-1)
	rho = []
	for i in range(n):
		rho.append(pi.index(i+1))

	#construct H'
	H = []
	for i in range(r,n):
		H.append(decimalToVector(pi[i],r))

	#construct G'
	GG = [list(i) for i in zip(*H)]
	for i in range(n-r):
		GG.append(decimalToVector(2**(n-r-i-1),n-r))

	#apply rho to get Gtranpose
	G = []
	for i in range(n):
		G.append(GG[rho[i]])

	#transpose    
	G = [list(i) for i in zip(*G)]

	return G
def decimalToVector(n,r): 			#Converts decimal values to vectors, given as part of the assignment.
	v = []
	for s in range(r):
		v.insert(0,n%2)
		n //= 2
	return v    
	
def message(a):						#Converts any vector to a message accepted by a hamming encoder.
	r = 2
	result = []
	binlenght  = str(bin(len(a))[2:])
	while True:
		if ((2**r)-(2*r)-1) < len(a):
			r += 1
		else: 
			break
	hamminglenght = ((2**r)-r-1)
	if len(binlenght) < r:
		diff = r - len(binlenght)
		while diff != 0:
			result.append(int(0))
			diff -= 1
	for i in range(len(binlenght)):
		result.append(int(binlenght[i]))
	for i in a:
		result.append(i)
	while len(result) < hamminglenght:
		result.append(0)
	return result
	
	
def hammingEncoder(m):				#Encodes a message into a Hamming code.
	r = 0
	for temp in range(0,len(m)*100):
		if len(m) == ((2**temp)-temp-1):
			r = temp
			break
	if r == 0:
		return []
	G = hammingGeneratorMatrix(r)
	C = []
	for i in range(len(G[0])):
		summ = 0
		for j in range(len(m)):
				summ += m[j] * G[j][i]
		C.append(summ%2)
	return C


def hammingDecoder(v):				#Decodes a message from a Hamming code.
	r = 0
	for temp in range(1,len(v)*100):
		if len(v)== (2**temp)-1:
			r = temp
			break
	if r == 0:
		return []
	Htranspose = []
	for i in range(1,(2**r)):
		row = []
		num = str(bin(i)[2:])
		while len(num) != r:
			num = "0" + num
		for char in num:
			row.append(int(char))
		Htranspose.append(row)
	vHt = []
	for i in range(len(Htranspose[0])):
		summ = 0
		for j in range(len(v)):
				summ += v[j] * Htranspose[j][i]
		vHt.append(summ%2)
	error = int("".join(str(e) for e in vHt),2)
	if error == 0:
		return v
	else:
		v[error-1]=(v[error-1]+1)%2
		return v


def messageFromCodeword(c):			#Retrieves the message from the codeword.
	r = 0
	for temp in range(1,len(c)*100):
		if len(c)== (2**temp)-1:
			r = temp
			break
	if r == 0:
		return []
	offset = 0
	for i in range(1,r+1):
		j = (2**(i-1))- 1 - offset
		del c[j]
		offset += 1
	return c


def dataFromMessage(m):				#Recovers raw data from a hamming message.
	r = 0
	for temp in range(1,len(m)*100):
		if len(m)== (2**temp)- temp - 1:
			r = temp
			break
	if r == 0:
		return []
	msglenght = []
	for i in range(0,r):
		msglenght.append(m.pop(0))
	lenght = int("".join(str(e) for e in msglenght),2)
	if lenght > len(m):
		return []
	message = []
	for i in range(0,lenght):
		message.append(m.pop(0))
	return message


def repetitionEncoder(m,n):			#Encodes a message using repetition.
	if len(m) != 1:
		return []
	while n != 1:
		m.append(m[0])
		n -= 1
	return m


def repetitionDecoder(v):			#Decodes a message using repetition.
	zero = [0]
	one = [1]
	zeros = []
	ones = []
	while len(v) != 0:
		temp = v.pop(0)
		if temp == 0:
			zeros.append(temp)
		if temp == 1:
			ones.append(temp)
		if temp != 0:
			if temp != 1:
				return []
	if len(zeros) > len(ones):
		return zero
	if len(ones) > len(zeros):
		return one
	if len(ones) == len(zeros):
		return []
