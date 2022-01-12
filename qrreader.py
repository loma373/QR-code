# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:29:07 2022

@author: Amol
"""

import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("youtubeqr.jpg"))
print("Decoded text is: ", val)