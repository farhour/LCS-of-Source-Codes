import sys
import glob
from tokenizer import tokenize
import GSuffixTree

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
print(lcsList)
print(lcsCount)

