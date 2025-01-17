import numpy as np
from PIL import Image

im_gray = np.array(Image.open('/home/ubuntu/key.png').convert('L'))
print(type(im_gray))
# <class 'numpy.ndarray'>

thresh = 128

im_bool = im_gray > thresh
print(im_bool)
# [[ True  True  True ...  True  True False]
#  [ True  True  True ...  True  True False]
#  [ True  True  True ...  True False False]
#  ...
#  [False False False ... False False False]
#  [False False False ... False False False]
#  [False False False ... False False False]]

maxval = 255

im_bin = (im_gray > thresh) * maxval
print(im_bin)
# [[255 255 255 ... 255 255   0]
#  [255 255 255 ... 255 255   0]
#  [255 255 255 ... 255   0   0]
#  ...
#  [  0   0   0 ...   0   0   0]
#  [  0   0   0 ...   0   0   0]
#  [  0   0   0 ...   0   0   0]]

Image.fromarray(np.uint8(im_bin)).save('/home/ubuntu/key_new.png')
