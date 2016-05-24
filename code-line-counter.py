import os
import sys
from sys import stdout

rootdir = sys.argv[1]
extDic = {}

def countLines(fPath):
	count = 0
	with open(fPath) as f:
		for i, l in enumerate(f):
			pass
			count = i
	return count + 1

def outTab(text):
	padSize = 10
	padChar = " "
	if len(str(text)) >= 10:
		stdout.write(text)
	else:
		pad = ""
		for p in xrange(padSize - len(str(text))):
			pad += padChar
		stdout.write(str(text) + pad)

for root, subdirs, files in os.walk(rootdir):
	for file in files:
		fPath = root + "\\" + file;
		fName, fExt = os.path.splitext(fPath)
		if fExt in extDic.keys():
			extDic[fExt] += countLines(fPath)
		else:
			extDic[fExt] = countLines(fPath)

outTab('FILE TYPE')
stdout.write(' | ')
outTab('LINE COUNT')
stdout.write('\n')
total = 0
for ext, lCount in extDic.iteritems():
	outTab(ext)
	stdout.write(' | ')
	outTab(lCount)
	stdout.write('\n')
	total += lCount
outTab('TOTAL')
stdout.write(' | ')
outTab(total)
stdout.write('\n')