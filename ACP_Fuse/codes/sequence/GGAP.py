#!/usr/bin/env python
#_*_coding:utf-8_*_

import re, sys, os
from collections import Counter
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import readFasta
import saveCode
import checkFasta

USAGE = """
USAGE:
	python GGAP.py input.fasta <g_gap> <output>

	input.fasta:      the input protein sequence file in fasta format.
	g_gap:   the sliding window, integer, defaule: 5
	output:           the encoding file, default: 'encodings.tsv'
"""


def obtainSequenceAllDiAAC(sequence, g_gap):#得到相隔g的二肽的组合
	content = []
	for i in range(len(sequence.strip())-1-g_gap):
		content.append(sequence[i]+sequence[i+1+g_gap])
	return content

def calculateOccurenceFrequencyOfAminoAcid(sequence, g_gap, diAAC):
	occurfrequency = dict()
	tmpCode = [0] * 400
	sequences = obtainSequenceAllDiAAC(sequence, g_gap)
#alter	
	seqLen = len(sequences)
	i12=0
	for each in diAAC:
		eachCount = sequences.count(each)#计算每一个样本的相隔g的二肽组合中，每个diAAC中二肽的个数
		if eachCount == 0:
			occurfrequency[each] = 0
			tmpCode[i12] = 0
		else:
			occurfrequency[each] = eachCount/seqLen
			tmpCode[i12] = eachCount/seqLen
		i12=i12+1
	
	return tmpCode


def generateDiaminoAcidComposition(aminoAcid):
	content = []
	for i in aminoAcid:
		for j in aminoAcid:
			content.append(i+j)
	return content



def GGAP(fastas, **kw):
	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
	g_gap1= kw['GAP'] 
	g_gap= int(g_gap1)
	encodings = []
	diPeptides = [aa1 + aa2 for aa1 in AA for aa2 in AA]
	header = ['#'] + diPeptides
	encodings.append(header)

	AADict = {}
	for i in range(len(AA)):
		AADict[AA[i]] = i

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		code = [name]
		tmpCode = [0] * 400
		diAAC=generateDiaminoAcidComposition(AA)
		tmpCode=calculateOccurenceFrequencyOfAminoAcid(sequence, g_gap, diAAC)
		code = code + tmpCode
		encodings.append(code)
	return encodings
	
if __name__ == '__main__':

	if len(sys.argv) == 1:
		print(USAGE)
		sys.exit(1)
	fastas = readFasta.readFasta(sys.argv[1])
	g_gap = int(sys.argv[2]) if len(sys.argv) >= 0 else 1
	output = sys.argv[3] if len(sys.argv) >= 4 else 'encoding.tsv'

	if len(sys.argv) >= 5:
		if sys.argv[4] in myAAorder:
			kw['order'] = myAAorder[sys.argv[4]]
		else:
			tmpOrder = re.sub('[^ACDEFGHIKLMNPQRSTVWY]', '', sys.argv[4])
			kw['order'] = tmpOrder if len(tmpOrder) == 20 else 'ACDEFGHIKLMNPQRSTVWY'

	encodings = EAAC(fastas, g_gap, **kw)
	saveCode.savetsv(encodings, output)