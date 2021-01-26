#!/usr/bin/env python
#_*_coding:utf-8_*_

import re

def obtainSequenceAllDiAAC(sequence, g_gap):#得到相隔g的二肽的组合
	content = []
	for i in range(len(sequence.strip())-1-g_gap):
		content.append(sequence[i]+sequence[i+1+g_gap])
	return content

def calculateOccurenceFrequencyOfAminoAcid(sequence, g_gap, diAAC):
	occurfrequency = dict()
	sequences = obtainSequenceAllDiAAC(sequence, g_gap)
#alter	
	seqLen = len(sequences)
	for each in diAAC:
		eachCount = sequences.count(each)#计算每一个样本的相隔g的二肽组合中，每个diAAC中二肽的个数
		if eachCount == 0:
			occurfrequency[each] = 0
		else:
			occurfrequency[each] = eachCount/seqLen
	
	return occurfrequency
	
	
def obtainSequenceDiAACALL(sequence, g_gap):#得到相隔0~g的二肽的组合
	content = []
	for m in range(g_gap):
		for i in range(len(sequence.strip())-1-g_gap):
			content.append(sequence[i]+sequence[i+1+g_gap])
	return content

def calculateOccurenceFrequencyOfAminoAcid(sequence, g_gap, diAAC):
	occurfrequency = dict()
	tmpCode = [0] * 400
	sequences = obtainSequenceDiAACALL(sequence, g_gap)
#alter	
	seqLen = len(sequences)
	i12=0
	for each in diAAC:
		eachCount = sequences.count(each)#计算每一个样本的相隔g的二肽组合中，每个diAAC中二肽的个数
		if eachCount == 0:
			tmpCode[i12] = 0
		else:
			tmpCode[i12] = eachCount/seqLen
		i12=i12+1
	return tmpCode

def generateDiaminoAcidComposition(aminoAcid):
	content = []
	for i in aminoAcid:
		for j in aminoAcid:
			content.append(i+j)
	return content



def ASDC(fastas, **kw):
	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
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
		tmpCode=calculateOccurenceFrequencyOfAminoAcid(sequence, 2, diAAC)
		code = code + tmpCode
		encodings.append(code)
#		for j in range(len(sequence) - 2 + 1):
#			tmpCode[AADict[sequence[j]] * 20 + AADict[sequence[j+1]]] = tmpCode[AADict[sequence[j]] * 20 + AADict[sequence[j+1]]] +1
#		if sum(tmpCode) != 0:
#			tmpCode = [i/sum(tmpCode) for i in tmpCode]
#		code = code + tmpCode
#		encodings.append(code)



	return encodings