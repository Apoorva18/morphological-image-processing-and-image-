import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('segment.jpg',0)
kernel = [[255,255,255],[255,255,255],[255,255,255]]
k,l = img.shape
m = k+2
n = l+2

matrix = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT,0)

i,j=0,0
#padding of image
#for i in range(k):
 #   for j in range(l):
  #      matrix[i+1][j+1] = img[i][j]
np.set_printoptions(threshold=np.nan)
#img =  np.asarray(img)   
#print(img)        
matrix = np.asarray(matrix) 

print(matrix.shape)  
print(kernel[1][2])
print(matrix[122][255])
s,t= 0,0


def dilation(matrix):
	img2 = [[0 for x in range(n)] for  w in range(m)]
	matrix = np.asarray(matrix)
	matrix = cv2.copyMakeBorder(matrix, 1, 1, 1, 1, cv2.BORDER_CONSTANT,0)
	for i in range(k):
		for j in range(l):
			img2[i][j] = matrix[i+1][j+1]
	for i in range(k):
		for j in range(l):  
			if((matrix[i][j] == kernel[0][0]) or (matrix[i][j+1] ==  kernel[0][1] ) or (matrix[i][j+2] == kernel[0][2]) or (matrix[i+1][j] == kernel[1][0]) or (matrix[i+1][j+1] == kernel[1][1]) or (matrix[i+1][j+2] == kernel[1][2]) or (matrix[i+2][j] == kernel[2][0]) or (matrix[i+2][j+1] == kernel[2][1]) or (matrix[i+2][j+2] ==  kernel[2][2])):
				img2[i+1][j+1] = 255
			
				
			else:
				img2[i+1][j+1] = 0
	imgk = [[0 for x in range(l)] for  w in range(k)]
	for i in range(k):
		for j in range(l):
			imgk[i][j]= img2[i+1][j+1] 
	return imgk			

def erosion(img2):
	img3 = [[0 for x in range(n)] for  w in range(m)]
	img2 = np.asarray(img2)
	img2 = cv2.copyMakeBorder(img2, 1, 1, 1, 1, cv2.BORDER_CONSTANT,255)
	
	
	i,j =0,0
	for i in range(k):
		for j in range(l):  
			if(img2[i][j] == kernel[0][0]):
				if(img2[i][j+1] ==  kernel[0][1] ): 
					if (img2[i][j+2] == kernel[0][2]): 
						if(img2[i+1][j] == kernel[1][0]):
							if(img2[i+1][j+1] == kernel[1][1]):
								if(img2[i+1][j+2] == kernel[1][2]):
							 		if(img2[i+2][j] == kernel[2][0]):
							 			if(img2[i+2][j+1] == kernel[2][1]):
							 				if(img2[i+2][j+2] ==  kernel[2][2]):
							 					img3[i+1][j+1] = 255
							 					print(img3[i][j])
							 					
			else:
				img3[i+1][j+1] = 0
	imgk = [[0 for x in range(l)] for  w in range(k)]
	for i in range(k):
		for j in range(l):
			imgk[i][j]= img3[i+1][j+1] 
	return imgk	

#print(img)	

T = 205
result = [[0 for i in range(l)] for j in range(k)]

for i in range(k):
	for j in range(l):
		if (img[i][j]<T):
			result[i][j]=0
		else:
			result[i][j]= 255
imgk = erosion(result)
print(imgk)        	
imgk = np.asarray(imgk)

cv2.imwrite('threshold.jpg',imgk)		


