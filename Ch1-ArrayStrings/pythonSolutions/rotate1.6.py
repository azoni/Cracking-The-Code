#Rotates image
def rotateMatrix(m):
	size = len(m[0])
	matrix = [[] for y in range(size)] 
	for i in range(size):
		for j in range(size):
			matrix[i].append(m[size-j-1][i])
	return matrix

if __name__ == "__main__":
	matrix = [[1,2,3,4,5],[5,6,7,8,9],[9,10,11,12,13],
	[13,14,15,16,17],[18,19,20,21,22]]

	rotatedMatrix = rotateMatrix(matrix)

	for i in rotatedMatrix:
		print i
