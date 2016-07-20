#! /usr/bin/env python
# -*- coding: utf-8 -*-

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import tweepy, time, sys
import textwrap
import random
import codecs
from ulyssesHelperFunction import  getChapter

img = Image.open('/home/ubuntu/ulysses/joycePortrait.png')
font = ImageFont.truetype("/home/ubuntu/ulysses/OpenSans-Regular.ttf",18) 

Draw = ImageDraw.Draw(img)
margin = offset = 5

file = codecs.open('/home/ubuntu/ulysses/ulyssesText.txt', 'rw', 'utf-8')
startPoint=random.randrange(0,7455)
print("first start point: ", startPoint)
count = 0
lines = file.readlines()
#print lines of the text on image
for i in range(startPoint,len(lines)):

		while count <10:
			line=lines[i]
			if len(line) > 44:
				for lineSubstring in textwrap.wrap(line, width=44):
					if count >= 10:
						print('breaking at',count)
						if len(lineSubstring)>38:
							n=lineSubstring.rindex(" ", 0, len(lineSubstring)-5)
							lineSubstring=lineSubstring[0:n]

						Draw.text((margin, offset), lineSubstring+' (...)', font=font, fill="#000000")
						break;
					else:
						lineSubstring=lineSubstring.strip()
						Draw.text((margin, offset), lineSubstring, font=font, fill="#000000")
						offset+=font.getsize(lineSubstring)[1] +15
						count+=1
						i+=1				
			else:
				line=line.strip()
				Draw.text((margin, offset), line, font=font, fill="#000000")
				offset += font.getsize(line)[1] +15
				count+=1
				i+=1
				if count >= 20:
						print('breaking at',count)
						break;

file.close()
chapterData = getChapter(startPoint)

#Print chapter details on image
font = ImageFont.truetype("/home/ubuntu/ulysses/OpenSans-Regular.ttf",10)
Draw.text((30, 440), chapterData['part'], font=font, fill="#000000")
Draw.text((30, 452), chapterData['episode'], font=font, fill="#000000")
Draw = ImageDraw.Draw(img)
Draw = ImageDraw.Draw(img)
img.save("ulyssesSnippet.png")
print "Image created"

 

 
#upload image to twitter
CONSUMER_KEY = [***]
CONSUMER_SECRET = [***]
ACCESS_KEY = [***]
ACCESS_SECRET = [***]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(auth)
API.update_with_media('ulyssesSnippet.png')
print "Image uploaded"