#!/usr/bin/env python
#_*_coding:utf-8_*_

import sys, os
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import checkFasta

def BIT20(fastas, **kw):
	if checkFasta.checkFasta(fastas) == False:
		print('Error: for "BIT20" encoding, the input fasta sequences should be with equal length. \n\n')
		return 0

	AA = 'ARNDCQEGHILKMFPSTWYV'
	encodings = []
	header = ['#BIT20']
#	for i in range(1, len(fastas[0][1]) * 20 + 1):
#		header.append('BIT20.F'+str(i))
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], i[1]
		code = [name]
		for aa in sequence:
			if aa == '-':
				code = code + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
				continue
			for aa1 in AA:
				tag = 1 if aa == aa1 else 0
				code.append(tag)
		encodings.append(code)
	return encodings
