import sys

def isUnique(s):
    charsTable = set()
    for c in s:
        if c in charsTable:
            return False
        charsTable.add(c)
    return True

def noBuffer(s):
    sortedStr = sorted(s)
    for i in range(len(sortedStr) - 1):
        if sortedStr[i] == sortedStr[i+1]:
           return False
    return True

def main():
    w = sys.argv[1]
    print('User Input: {}: {}'.format(w, isUnique(w)))
    print('User Input: {}: {}'.format(w, noBuffer(w)))

main()