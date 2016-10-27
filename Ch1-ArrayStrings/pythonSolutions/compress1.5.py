import sys

#Appends to an array after counting matches
def compress(w):
	arr = []
	i = 0;
	while i < len(w):
		count = 1
		arr.append(w[i])
		while w[i] == w[(count + i) % len(w)]:
			count += 1
		i += count
		arr.append(str(count))
	w = ''.join(arr)
	return w

#Runs the main method!
if __name__ == '__main__':
	w = sys.argv[1]
	print compress(w)