#!/usr/bin/env python
#_*_coding:utf-8_*_

import sys, os
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import checkFasta

def OLP(fastas, **kw):
	if checkFasta.checkFasta(fastas) == False:
		print('Error: for "BINARY" encoding, the input fasta sequences should be with equal length. \n\n')
		return 0

	group1 = {
		'G1': 'NQSDECTKRHYW',
		'G2': 'KHR',
		'G3': 'DE',
		'G4': 'KHRDE',
		'G5': 'AGCTIVLKHFYWM',
		'G6': 'IVL',
		'G7': 'FYWH',
		'G8': 'PNDTCAGSV',
		'G9': 'ASGC',
		'G10': 'P',
	} 
	property = (
	'G1', 'G2', 'G3', 'G4',
	'G5', 'G6', 'G7', 'G8',
	'G9', 'G10')

	encodings = []
	header = ['#OLP']
#	for i in range(1, len(fastas[0][1]) * 20 + 1):
#		header.append('BINARY.F'+str(i))
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], i[1]
		code = [name]
		d=0
		for aa in sequence:
			if aa == '-':
				code = code + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
				continue
			for p in property:
				k=0
				for aa1 in group1[p]:
					if aa1 == aa :
						k=k+1
						#print(k)
				if k>=1:
					d=1
#					print(k)
				else:
					d=0
				code.append(d)
		encodings.append(code)
	return encodings
