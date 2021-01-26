#!/usr/bin/env python
#_*_coding:utf-8_*_

import re
import math
from collections import Counter
import sys, os
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import checkFasta
def IT(fastas, **kw):
	if checkFasta.checkFasta(fastas) == False:
		print('Error: for "BINARY" encoding, the input fasta sequences should be with equal length. \n\n')
		return 0
	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
	#AA = 'ARNDCQEGHILKMFPSTWYV'
	encodings = []
	header = ['#IT']
#	for i in AA:
#		header.append(i)
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		count = Counter(sequence)
		count1 = Counter(sequence)
		for key in count:
			count[key] = count[key]
			count1[key] = count[key]/len(sequence)
		code = [name]
		temp_SE =0.0
		temp_RSE =0.0
		for aa in AA:
			if count[aa] != 0:
				temp_SE =temp_SE-count1[key] * math.log( count1[key]) / math.log(2)
				temp_RSE = temp_RSE + count1[key] * (math.log(count1[key] * (len(sequence) - 1) / 2) / math.log(2));
		code.append(temp_SE)
		code.append(temp_RSE)
		code.append(temp_SE - temp_RSE )
#		for aa in AA:
#			code.append(count[aa])
		encodings.append(code)

	return encodings