import sys

#Recursive solution
def recursive(s):
	if s != "":
		return s[-1:] + recursive(s[:-1])
	else:
		return ""

#General solution
def reverse(s):
	return s[::-1]

def main():
	w = sys.argv[1]
	print recursive(w)
	print reverse(w)

main()