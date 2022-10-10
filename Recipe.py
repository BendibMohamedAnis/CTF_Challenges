from time import sleep
import cv2 as cv

# Load two images
img1 = cv.imread('eggs.jpg')
img2 = cv.imread('eggshell.jpg')

img2_fg = cv.bitwise_not(img1,img2,mask = None)

img_flour = cv.imread('flour.jpg')
img_floor_mix= cv.bitwise_and(img2_fg,img_flour)

water = cv.imread('water.jpg')
sugar = cv.imread('sugar.jpg')
img_sw_mix= cv.bitwise_and(water,sugar)
sirup = cv.imread('sirup.jpg')
img_mix2= cv.bitwise_and(img_sw_mix,sirup)
img_mix3=  cv.bitwise_and(img_mix2,img_floor_mix)

secret_flavour = cv.imread('secret_flavour.jpg')
pancake = cv.imread('pancake.png')

flag = cv.bitwise_xor(secret_flavour, pancake, img_mix3)




cv.imshow('res',flag)
cv.imwrite('lol321".png',flag) 
cv.waitKey(6000)