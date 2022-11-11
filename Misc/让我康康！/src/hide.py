import cv2
import numpy as np

image = cv2.imread('79877384_p1.png')
hide = image /48
cv2.imwrite('hidden.png', hide)

image = cv2.imread('hidden.png')
hide = image *48
cv2.imwrite('a.png', hide)