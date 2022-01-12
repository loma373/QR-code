# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:18:06 2022

@author: Amol
"""

import qrcode as qr

img=qr.make("https://www.youtube.com")
img.save("youtubeqr.jpg")



