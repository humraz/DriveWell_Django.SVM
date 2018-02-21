import numpy as np
import cv2
import os
import pickle
from sklearn import svm

scoremap = { "Normal" : 0, "Phone" : -1, "Drinking" : -0.5}

def ClassifyAndScore():
	score=100
	images = os.listdir("image/16")
	#print images
	for i in images:
		
		if i.endswith(".jpg"):
			cl = ClassifyImage(i)
			os.remove(os.path.join("image/16",i))
			if( score >= 0):
				score += scoremap[cl]

		

	return score

def ClassifyImage(filename):

	countlist = {"Normal": 0, "Phone": 0, "Drinking": 0}
	a = []
	b = []
	for i in range(0, 64):
		b.append(0.5)
	a.append(b)

	img = cv2.imread(os.path.join("image/16",filename), 0)
	img = Preprocessing(img)
	kp, des = FeatureExtraction(img)
	print des
	filename = 'finalized_model.sav'
	loaded_model = pickle.load(open(os.path.join( filename), 'rb'))
	if not (type(des) is np.ndarray):

		
		return "Normal"
	prediction = loaded_model.predict(des)
	print prediction

	#Takes aggregate of predictions on individual descriptors and chooses best class
	for i in prediction:
		countlist[i] +=1
	
	return max(countlist.items(), key = lambda x: x[1])[0]

#Cropping, Resize, Binary Threshold
def Preprocessing(img):

	croppedx2 = int(img.shape[1]*0.85)
	croppedy2 = int(img.shape[0]*0.85)
	croppedx1 = img.shape[1] - croppedx2
	croppedy1 = img.shape[0] - croppedy2

	#Cropped Image
	crop = img[croppedy1:croppedy2, croppedx1:croppedx2]
	#Resized Image
	resize = cv2.resize(crop, (320, 240), interpolation =  cv2.INTER_LINEAR)
	#Binary Thresholded Image
	ret, threshed = cv2.threshold( resize, 100, 255, cv2.THRESH_BINARY)

	return threshed

#Returns keypoints and descriptors of image as a tuple
def FeatureExtraction(img):
	surf = cv2.xfeatures2d.SURF_create()
	surf.setHessianThreshold(400)

	kp, des = surf.detectAndCompute(img, None)
	
	return kp,des


#HIGHESTBLOCK
