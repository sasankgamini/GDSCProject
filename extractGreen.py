import cv2
import numpy as np

#IMAGE BEFORE
imageBefore = cv2.imread('outputBefore.png')
imageBefore = cv2.resize(imageBefore, (600,480))
#convert to hsv to make it easier to find range of green
hsvimage = cv2.cvtColor(imageBefore, cv2.COLOR_BGR2HSV) 
#converting hsv values to np arrays
lowgreen = np.array([(36,0,0)])
highgreen = np.array([(86,255,255)])
#finding all green pixels(black/white image)
mask = cv2.inRange(hsvimage, lowgreen, highgreen)
#took original image and multiplied it with the black/white image(mask image) and black pixels ended up being the same since it has a value of zero
finalImageBefore = cv2.bitwise_and(imageBefore,imageBefore,mask=mask)



#IMAGE AFTER
imageAfter = cv2.imread('outputAfter.png')
imageAfter = cv2.resize(imageAfter, (600,480))
#convert to hsv to make it easier to find range of green
hsvimage = cv2.cvtColor(imageAfter, cv2.COLOR_BGR2HSV) 
#converting hsv values to np arrays
lowgreen = np.array([(36,0,0)])
highgreen = np.array([(86,255,255)])
#finding all green pixels(black/white image)
mask = cv2.inRange(hsvimage, lowgreen, highgreen)
#took original image and multiplied it with the black/white image(mask image) and black pixels ended up being the same since it has a value of zero
finalImageAfter = cv2.bitwise_and(imageAfter,imageAfter,mask=mask)



#finding all black pixels(black/white image) in before image
beforeImageGrayscale = cv2.cvtColor(finalImageBefore, cv2.COLOR_BGR2GRAY)
#finding coordinates of black pixels in before image
coordsBlackBefore = np.column_stack(np.where(beforeImageGrayscale == 0))

#finding all black pixels(black/white image) in after image
afterImageGrayscale = cv2.cvtColor(finalImageAfter, cv2.COLOR_BGR2GRAY)
#finding coordinates of black pixels in after image
coordsBlackAfter = np.column_stack(np.where(afterImageGrayscale == 0))

#finding coords where there is black in after image, and green in before image
coordsBlackDifference = np.column_stack(np.where((afterImageGrayscale == 0) & (beforeImageGrayscale != 0)))


#plotting red where there used to be trees
deforestationImage = imageAfter.copy()
for coord in coordsBlackDifference:
  deforestationImage[coord[0],coord[1]] = (0,0,255)

cv2.imshow('Image Before Deforestation',imageBefore)
cv2.imshow('Image After Deforestation',imageAfter)
cv2.imshow('Representation', deforestationImage)
cv2.waitKey()
cv2.destroyAllWindows()



