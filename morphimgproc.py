import cv2
import numpy as np
import matplotlib as plt 
#read image
img = cv2.imread('noise.jpg',0)
k,l = (img.shape)
print(k,l)
#sobel for horizontal direction
kernel = [[255,255,255],[255,255,255],[255,255,255]]
m = k+2
n = l+2
#matrix = [[0 for j in range(n)] for i in range(m)]
#result = [[0 for x in range(n)] for  w in range(m)] 
#result2 = [[0 for x in range(n)] for  w in range(m)]

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
	

img2 = [[0 for x in range(l)] for  w in range(k)] 
img2 = dilation(img)
img2 = np.asarray(img2)		
img3 = [[0 for x in range(l)] for  w in range(k)] 	
img3 = erosion(img2)
img4 = erosion(img3)


img5 = dilation(img4)



img5 = np.asarray(img5)
#imgk = img5/255
cv2.imwrite('res_noise1.jpg',img5)

img2a = [[0 for x in range(l)] for  w in range(k)] 
img2a = erosion(img)
img2a = np.asarray(img2a)		
img3 = [[0 for x in range(l)] for  w in range(k)] 	
img3a = dilation(img2a)
img4a = dilation(img3a)


img5a = erosion(img4a)



img5a = np.asarray(img5a)
#imgk2 = img5a/255
cv2.imwrite('res_noise2.jpg',img5a)


kernel = np.asarray(kernel)

b = erosion(img5)
b = np.asarray(b)
boundary  = [[0 for x in range(l)] for  w in range(k)]
for i in range(k):
	for j in range(l):
		boundary[i][j] = img5[i][j] - b[i][j]
boundary = np.asarray(boundary)

boundary = np.asarray(boundary)

cv2.imwrite('res_bound1.jpg',boundary)
ba = erosion(img5a)
ba = np.asarray(ba)
boundary  = [[0 for x in range(l)] for  w in range(k)]
for i in range(k):
	for j in range(l):
		boundary[i][j] = img5a[i][j] - ba[i][j]
boundary = np.asarray(boundary)

boundary = np.asarray(boundary)

cv2.imwrite('res_bound2.jpg',boundary)



