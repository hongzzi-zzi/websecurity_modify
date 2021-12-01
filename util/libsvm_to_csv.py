import sys
def libsvm_to_csv(libsvmFile):
	sys.stdout = open('result.csv', 'w')
	f = open(libsvmFile, 'r')

	lines = f.readlines()
	for line in lines:	
		minus_list = [-1]*3639

		l = line.split(' #')[0]
		l = l.split(' ')
		file_name = line.split(' #')[1].strip('\n')
		
		for i in range(len(l)):
			if i != 0:
				key = int(l[i].split(':')[0])
				val = float(l[i].split(':')[1])
				minus_list[key-1]=val
		if int(l[0]) == 1:
			mb = 'M'
		else:
			mb = 'B'
		
		result_string=str(minus_list).strip('[]')+', '+file_name

		print(result_string)

	sys.stdout.close()