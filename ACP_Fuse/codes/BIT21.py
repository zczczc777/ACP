#!/usr/bin/env python
#_*_coding:utf-8_*_

import sys, os
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import checkFasta

def BIT21(fastas, **kw):
	if checkFasta.checkFasta(fastas) == False:
		print('Error: for "BINARY" encoding, the input fasta sequences should be with equal length. \n\n')
		return 0

	group1 = {
		'G1': 'ACFGHILMNPQSTVWY',
		'G2': 'DE',
		'G3': 'KR',
		'G4': 'CFILMVW',
		'G5': 'AGHPSTY',
		'G6': 'DEKNQR',
		'G7': 'ACDGPST',
		'G8': 'EILNQV',
		'G9': 'FHKMRWY',
		'G10': 'CFILMVWY',
		'G11': 'AGPST',
		'G12': 'DEHKNQR',
		'G13': 'ADGST',
		'G14': 'CEILNPQV',
		'G15': 'GASDT',
		'G16': 'DGNPS',
		'G17': 'AEHKLMQR',
		'G18': 'CFITVWY',
		'G19': 'ACFGILVW',
		'G20': 'HMPSTY',
		'G21': 'DEKNRQ'
	}
	property = (
	'G1', 'G2', 'G3', 'G4',
	'G5', 'G6', 'G7', 'G8',
	'G9', 'G10','G11', 'G12', 'G13', 'G14',
	'G15', 'G16', 'G17', 'G18',
	'G19', 'G20' , 'G21')

	encodings = []
	header = ['#BIT21']
#	for i in range(1, len(fastas[0][1]) * 20 + 1):
#		header.append('BINARY.F'+str(i))
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], i[1]
		code = [name]
		d=0
		for aa in sequence:
			if aa == '-':
				code = code + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
