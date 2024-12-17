import re
import os

file = open('etl2.xformat', 'rb') #open file
str_bytes = file.read() #read file as bytes (encoding is unknown)
pattern = b'(.PNG(.*?)IEND)' #create regex pattern of (wildcard)PNG(wildcards up to first found IEND)IEND
img_strings = re.findall(pattern, str_bytes, re.DOTALL) #get the resulting bytes for each image, including newlines

sample_num = 1

if not os.path.exists("./images/"): #create images directory if it doesn't already exist
    os.makedirs("./images/")

for char_num in range(len(img_strings)): #etl2.xformat has 52796 images, ~10 of most characters(?)
    f = open("./images/{}.png".format(char_num + 1), "wb") #create numbered png file (indices differ from etl2-metadata.json, which sometimes skips a few for some reason, like from 3560 to 3601)
    f.write(img_strings[char_num][0]) #write bytes to specified file
    f.close()