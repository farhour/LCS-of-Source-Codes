import sys
import glob
from tokenizer import tokenize
import GSuffixTree
import math
import csv
import json

path = 'input/sample/*.txt'

countOfArgs = len(sys.argv)
pathToFiles = list()
listForGST = list()
if countOfArgs > 1:
    for i in range(1, countOfArgs):
        pathToFiles.append(sys.argv[i])
else:
    files = glob.glob(path)
    for file in files:
        pathToFiles.append(file)
for pathToFile in pathToFiles:
    with open(pathToFile, 'r') as content_file:
        content = content_file.read()
    listForGST.append(tokenize(content))
gst = GSuffixTree.STree(listForGST)
lcsList = gst.lcs()
lcsCount = list()
for lcs in lcsList:
    lcsCount.append(len(gst.find_all(lcs)))
tokensCount = len(lcsList[0])
result = list()
for i in range(len(lcsList)):
    score = math.log(lcsCount[i], 2) * math.log(tokensCount, 2)
    result.append([score, tokensCount, lcsCount[i], ' '.join(lcsList[i])])
with open('output/result.csv', 'w') as myFile:
    wr = csv.writer(myFile)
    wr.writerows(result)
with open('output/result.json', 'w') as myFile:
    json = json.dumps(result)
    myFile.write(json)
