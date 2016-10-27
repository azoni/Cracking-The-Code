import sys

#split by space, and join %20 in place
def replaceSpace(s):
	return "%20".join(s.split())

#generic use of relace method
def replaceSpace2(s):
	return s.replace(' ', "%20")

#Join command arugment into String
def main():
	w = " ".join(sys.argv[1:])
	print replaceSpace(w)
	print replaceSpace2(w)

main()