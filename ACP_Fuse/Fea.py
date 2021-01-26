#!/usr/bin/env python
#_*_coding:utf-8_*_

import argparse
import re
from codes import *

if __name__ == '__main__':
	parser = argparse.ArgumentParser(usage="it's usage tip.",
									 description="Generating various numerical representation schemes for protein sequences")
	parser.add_argument("--file", required=True, help="input fasta file")
	parser.add_argument("--type", required=True,
						choices=['AAC', 'GAAC', 'DPC', 'DDE', 'TPC','GAAC','CKSAAP', 'CKSAAGP', 'GDPC', 'GTPC',
								 'AAINDEX','NMBroto', 'Moran', 'Geary','CTDC', 'CTDT', 'CTDD','CTriad', 'KSCTriad',
								 'SOCNumber', 'QSOrder','PAAC', 'APAAC','KNNprotein', 'KNNpeptide',
								 'PSSM', 'SSEC', 'SSEB', 'Disorder', 'DisorderC', 'DisorderB', 
								 'ASA', 'TA', 'ASDC','GGAP','NeedlemanWunsch',
								 'OLP', 'BIT20', 'BIT21', 'IT', 'ZSCALE', 'BLOSUM62', 'EAAC', 'EGAAC', 'KGAAC', 'KGDPC'
								 ],
						help="the encoding type")
	parser.add_argument("--path", dest='filePath',
						help="data file path used for 'PSSM', 'SSEB(C)', 'Disorder(BC)', 'ASA' and 'TA' encodings")
	parser.add_argument("--train", dest='trainFile',
						help="training file in fasta format only used for 'KNNprotein' or 'KNNpeptide' encodings")
	parser.add_argument("--label", dest='labelFile',
						help="sample label file only used for 'KNNprotein' or 'KNNpeptide' encodings")
	parser.add_argument("--order", dest='order',
						choices=['alphabetically', 'polarity', 'sideChainVolume', 'userDefined'],
						help="output order for of Amino Acid Composition (i.e. AAC, EAAC, CKSAAP, DPC, DDE, TPC) descriptors")
	parser.add_argument("--userDefinedOrder", dest='userDefinedOrder',
						help="user defined output order for of Amino Acid Composition (i.e. AAC, EAAC, CKSAAP, DPC, DDE, TPC, GGAP) descriptors")
	parser.add_argument("--out", dest='outFile',
						help="the generated descriptor file")
	parser.add_argument("--GAP", dest='GAP',
						help="the GAP")
	parser.add_argument("--output_type", dest='output_type',
						choices=['csv', 'tsv'],
						help="type of output")
	parser.add_argument("--CutLength", dest='CutLength',
						help="type of output")
	args = parser.parse_args()
	cut = args.CutLength
	print(cut)
	if cut != None:
		fastas = readFasta.readFastacut(args.file,cut)
	else:
		fastas = readFasta.readFasta(args.file)
#		print fastas
	userDefinedOrder = args.userDefinedOrder if args.userDefinedOrder != None else 'ACDEFGHIKLMNPQRSTVWY'
	userDefinedOrder = re.sub('[^ACDEFGHIKLMNPQRSTVWY]', '', userDefinedOrder)
	if len(userDefinedOrder) != 20:
		userDefinedOrder = 'ACDEFGHIKLMNPQRSTVWY'
	myAAorder = {
		'alphabetically': 'ACDEFGHIKLMNPQRSTVWY',
		'polarity': 'DENKRQHSGTAPYVMCWIFL',
		'sideChainVolume': 'GASDPCTNEVHQILMKRFYW',
		'userDefined': userDefinedOrder
	}
	myOrder = myAAorder[args.order] if args.order != None else 'ACDEFGHIKLMNPQRSTVWY'
	kw = {'path': args.filePath, 'train': args.trainFile, 'label': args.labelFile, 'order': myOrder, 
	'GAP': args.GAP}
	userDefinedoutputtype=args.output_type
	myFun = args.type + '.' + args.type + '(fastas, **kw)'
#	print( kw)
	print('Descriptor type: ' + args.type)
	encodings = eval(myFun)
#	print(encodings)
	outFile = args.outFile if args.outFile != None else 'encoding.tsv'
	if userDefinedoutputtype == "tsv":
		saveCode.savetsv(encodings, outFile)
	else:
		saveCode.savecsv(encodings, outFile)
