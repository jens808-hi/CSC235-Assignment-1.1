print ("Hello World")
print ("My name is Jena")
print ("In this tutorial we going to learn how to convert an image to pdf file and how to open converted pdf file in Python")
print ("First you need to install pillow library")
print ("From the command line terminal type: pip install pillow")
print ("Select an image that you want to convert to pdf and take note of the file location")
print ("Here is the syntax for converting an image to pdf file: from PIL import Image")
from PIL import Image
print ("Here is the syntax for opening an image with a function: Image.open(image file path to image goes here")
print ("To execute with file path type: Image.open(cookieMonster_eat_cookies.jpg)")
Image.open("cookieMonster_eat_cookies.jpg")
print ("Here is the syntax for saving an image to a variable: img1 = Image.open(image file path to image goes here")
print ("To execute with file path type: img1 = Image.open(cookieMonster_eat_cookies.jpg")
img1 = Image.open("cookieMonster_eat_cookies.jpg")
print ("Here is the syntax for converting the image: img1.conver('represents the image')")
print ("To execute with image processing: image1 = img1.convert('RGB')")
image1 = img1.convert('RGB')
print ("saves the converted image to pdf file (file path to image goes here but change ext to .pdf")
print ("To execute with file path type: image1.save(cookieMonster_eat_cookies.pdf")
image1.save("cookieMonster_eat_cookies.pdf")
print ("Run code and check folder to see if a new pdf file was created")
print ("Next we are going to open that converted pdf file")
print ("Here is the syntax for opening the newly converted pdf file")
print ("import subprocess")
import subprocess
print ("this command brings in the subprocess module, allows you to interact with external program & execute commands)")
print ("path = (pdf file path goes here")
path = ("cookieMonster_eat_cookies.pdf")
print ("this specifies the file path of the pdf")
print ("subprocess.Popen([path], shell=True)")
subprocess.Popen([path], shell=True)
print ("this Popen function creates a new process to run the command and returns a Popen object. Path is a string that represents the command you want to execute. When shell=True this string is interpreted by the system shell.")
print ("Congratulations! You've converted a image to pdf and opened that same pdf file")
