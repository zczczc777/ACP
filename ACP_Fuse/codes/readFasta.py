#!/usr/bin/env python
#_*_coding:utf-8_*_

import re, os, sys

def readFasta(file):
	if os.path.exists(file) == False:
		print('Error: "' + file + '" does not exist.')
		sys.exit(1)

	with open(file) as f:
		records = f.read()

	if re.search('>', records) == None:
		print('The input file seems not in fasta format.')
		sys.exit(1)

	records = records.split('>')[1:]
	myFasta = []
	for fasta in records:
		array = fasta.split('\n')
		name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())
		myFasta.append([name, sequence])
	return myFasta


def readFastacut(file,cut):
	cutarg=re.findall(r'[A-Z]+|[0-9]+', cut.upper())
	cutnum=int(cutarg[1])
	if os.path.exists(file) == False:
		print('Error: "' + file + '" does not exist.')
		sys.exit(1)

	with open(file) as f:
		records = f.read()

	if re.search('>', records) == None:
		print('The input file seems not in fasta format.')
		sys.exit(1)
	if cutnum < 1:
		print('Error: "' + file + '"Cutting length is out of range .')
		sys.exit(1)

	records = records.split('>')[1:]
	myFasta = []
	for fasta in records:
		array = fasta.split('\n')
		name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())
		if cutnum>len(sequence):
			sequence=sequence+sequence+sequence+sequence
		if cutarg[0]=="NT":
			sequence=sequence[0:cutnum]
		if cutarg[0]=="CT":
			sequence=sequence[len(sequence)-cutnum:len(sequence)]
		if cutarg[0]=="NTCT":
			sequence=sequence[0:cutnum]+sequence[len(sequence)-cutnum:len(sequence)]
#		print(sequence)
		myFasta.append([name, sequence])
	return myFasta