#!/usr/bin/env python
#_*_coding:utf-8_*_

import re
from collections import Counter

def AAC(fastas, **kw):
	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
	#AA = 'ARNDCQEGHILKMFPSTWYV'
	encodings = []
	header = ['#']
	for i in AA:
		header.append(i)
	encodings.append(header)
#	print fastas
	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		count = Counter(sequence)
#		print count
		for key in count:
			count[key] = count[key]/float(len(sequence))
#			print count[key]
		code = [name]
#		code = []
		for aa in AA:
			code.append(count[aa])
		encodings.append(code)
#	print encodings
	return encodings