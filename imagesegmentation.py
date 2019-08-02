import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('turbine-blade.jpg',0)
#plt.hist(image.ravel(),256,[0,256])
#plt.show()
k,l = image.shape
m = k+2
n = l+2
kernel = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
matrix = [[0 for i in range(n)] for j in range(m)]
result = [[0 for i in range(l)] for j in range(k)]
for i in range(k):
    for j in range(l):
        matrix[i+1][j+1] = image[i][j]
matrix = np.asarray(matrix)
       
#cv2.imshow('padded img',matrix)
#cv2.waitKey(0)
T = 1100
count = 0

for i in range(k):
	for j in range(l):
		sum = matrix[i][j]*kernel[0][0] + matrix[i][j+1]*kernel[0][1] + (matrix[i][j+2]*kernel[0][2]) + (matrix[i+1][j] * kernel[1][0]) + (matrix[i+1][j+1] * kernel[1][1]) + (matrix[i+1][j+2]* kernel[1][2]) + (matrix[i+2][j] * kernel[2][0]) + (matrix[i+2][j+1] * kernel[2][1]) + (matrix[i+2][j+2] * kernel[2][2]) 
		#result[i][j] = np.absolute(sum)      	
		
		if(np.absolute(sum)>T or np.absolute(sum)== T):
			result[i][j] = np.absolute(sum)
		sum =0

#print(result)        	
result = np.asarray(result)

for i in range(k):
	for j in range(l):
		if(result[i][j]>0):
			print(i,j)
cv2.imwrite('porosity.jpg',result)		


