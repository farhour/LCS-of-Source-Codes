import sys
import glob

path = 'input/sample/*.txt'

countOfArgs = len(sys.argv)
pathToFiles = list()
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
