import sys

#Sort the two strings then compare
def sort(s1, s2):
	s1 = sorted(s1)
	s2 = sorted(s2)
	return s1 == s2

def main():
	print sort(sys.argv[1].lower(), sys.argv[2].lower())

main()