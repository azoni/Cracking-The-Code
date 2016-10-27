import sys

#Solution using a Set.
def isUnique(s):
    charsTable = set()
    for c in s:
        if c in charsTable:
            return False
        charsTable.add(c)
    return True

#No Buffers
def noBuffer(s):
    sortedStr = sorted(s)
    for i in range(len(sortedStr) - 1):
        if sortedStr[i] == sortedStr[i+1]:
           return False
    return True

#Histagram style
def histagram(s):
    strLen = len(s)
    if strLen > 128:
        return False
    charArr = [0] * 128
    for i in range(strLen):
        val = ord(s[i])
        if charArr[val] > 0:
            return False
        charArr[val] += 1
    return True

def main():
    w = sys.argv[1]
    print('User Input: {}: {}'.format(w, isUnique(w)))
    print('User Input: {}: {}'.format(w, noBuffer(w)))
    print('User Input: {}: {}'.format(w, histagram(w)))
    
main()