#import image from Pillow library        	
from PIL import Image
#opens an image with function Image.open ("file path to image goes here") 	
Image.open("cookieMonster_eat_cookies.jpg")
#saves the image to a variable
img1 = Image.open("cookieMonster_eat_cookies.jpg")
#converts the image 
image1 = img1.convert('RGB')
#save converted image to pdf file ("file path to image goes here but change ext to .pdf")
image1.save("cookieMonster_eat_cookies.pdf")
#brings in the subprocess module, allows you to interact with external program & execute commands 
import subprocess
#specifies the file path of the pdf
path = ("cookieMonster_eat_cookies.pdf")
#Popen function creates a new process to run the command and returns a Popen object 
subprocess.Popen([path], shell=True)
