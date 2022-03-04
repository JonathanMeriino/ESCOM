import numpy as np
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg')

cv2.imshow('Imagen Original',img)

cv2.waitKey(0)