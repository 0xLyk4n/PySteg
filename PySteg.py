#import ImageTK module from Pillow library
from PIL import ImageTk, Image
import math #import math module
import os #import os

# Only works with PNG images due to JPG compression issues messing up the message
# Function to encode the secret message
# A python program to encode a secret message
def encodeMessage(image, msg, fileName):
    msg = "." + msg
    width, height = image.size
    if (width * height) < len(msg):
        raise ValueError
    pixels = image.load()
    for i in range(0, len(msg)):
        encodedChar = str(ord(msg[i]))
        row = math.ceil(i/float(width))
        column = i%width
        pixel = pixels[row-1, column-1]
        newPixel = list(pixel)
        newPixel[0] = str(newPixel[0])
        newPixel[1] = str(newPixel[1])
        newPixel[2] = str(newPixel[2])

        if ord(msg[i]) >= 100:
            r = list(newPixel[0])
            r[-1] = encodedChar[0]
            newPixel[0] = ''.join(r)

            r = list(newPixel[1])
            r[-1] = encodedChar[1]
            newPixel[1] = ''.join(r)

            r = list(newPixel[2])
            r[-1] = encodedChar[2]
            newPixel[2] = ''.join(r)

        elif ord(msg[i]) >= 10:
            r = list(newPixel[0])
            r[-1] = '0'
            newPixel[0] = ''.join(r)

            r = list(newPixel[1])
            r[-1] = encodedChar[0]
            newPixel[1] = ''.join(r)

            r = list(newPixel[2])
            r[-1] = encodedChar[1]
            newPixel[2] = ''.join(r)

        else:
            r = list(newPixel[0])
            r[-1] = '0'
            newPixel[0] = ''.join(r)

            r = list(newPixel[1])
            r[-1] = '0'
            newPixel[1] = ''.join(r)

            r = list(newPixel[2])
            r[-1] = encodedChar[0]
            newPixel[2] = ''.join(r)


        newPixel[0] = int(newPixel[0])
        newPixel[1] = int(newPixel[1])
        newPixel[2] = int(newPixel[2])
        pixels[row-1, column-1] = tuple(newPixel)
    row = math.ceil(len(msg)/float(width))
    column = len(msg)%width
    pixel = pixels[row, column]
    newPixel = list(pixel)
    newPixel[0] = str(newPixel[0])
    newPixel[1] = str(newPixel[1])
    newPixel[2] = str(newPixel[2])

    r = list(newPixel[0])
    r[-1] = '1'
    newPixel[0] = ''.join(r)
    
    r = list(newPixel[1])
    r[-1] = '2'
    newPixel[1] = ''.join(r)

    r = list(newPixel[2])
    r[-1] = '7'
    newPixel[2] = ''.join(r)



    newPixel[0] = int(newPixel[0])
    newPixel[1] = int(newPixel[1])
    newPixel[2] = int(newPixel[2])
    pixels[row-1, column-1] = tuple(newPixel)
    image.save("./export/" + fileName)

#Function for decoding the message
def decodeMessage(image):
    pixels = image.load()
    encodedText = ""
    for w in range(0, image.size[0]):
        for h in range(0, image.size[1]):
            pixel = pixels[w,h]
            encodedChar = int(str(pixel[0])[-1]) * 100 + int(str(pixel[1])[-1]) * 10 + int(str(pixel[2])[-1])
            if(encodedChar == 127):
                return encodedText
            else:
                encodedText+=chr(encodedChar)
    return encodedText

#main func
if __name__== "__main__":
    while True:
        choice = input("Decode or encrypt? (d/e): ")
        while not(choice == 'd' or choice == 'e'):
            print("\n[ERROR] Invalid choice, please input 'd' or 'e'!")
            choice = input("\nDecode or encrypt? (d/e): ")
        print()
        if(choice == 'd'):
            for subdir, dirs, files in os.walk("./decrypt"):
                for file in files:
                    filepath = subdir + os.sep + file

                    if filepath.endswith(".png"):
                        print("Decoded message from [" + file + "]: " + decodeMessage(Image.open("./decrypt/" + file)))
            print("\nFinished Decoding images.")
        
        else:
            msg = input('Enter message to encode: ')

            for subdir, dirs, files in os.walk("./encrypt"):
                for file in files:
                    filepath = subdir + os.sep + file

                    if filepath.endswith(".png"):
                        try:
                            encodeMessage(Image.open("./encrypt/" + file), msg, file)
                            print("Encoded message into [" + file + "]")
                        except ValueError:
                            print("Message too long to encode in [" + file + "]")
            print("\nFinished Encoding images.")

#end of script
