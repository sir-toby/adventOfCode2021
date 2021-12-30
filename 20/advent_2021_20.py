import numpy as np
import pdb

def inputFile(fileName):
    file = open(fileName, mode='r')
    text = file.read()

    enhancementMapping = text[:text.find('\n\n')]
    image = (text[text.find('\n\n')+2:]).split('\n')

    return enhancementMapping, image
    
def extendImage(inputImage, symbol, thickness):
    extendedImage = []
    width = len(inputImage[0]) + 2*thickness
    for i in range(thickness):
        extendedImage.append(symbol*width)
    for line in inputImage:
        extendedImage.append(symbol*thickness + line + symbol*thickness)
    for i in range(thickness):
        extendedImage.append(symbol*width)
    return extendedImage

def enhanceImage(image, steps, mapping):
    intermediateMatrix = []
    for y in range(1, len(image)-1):
        intermediateLine = []
        for x in range(1, len(image[0])-1):
            byte = ''
            for ycoord in range(y-1, y+2):
                for xcoord in range(x-1, x+2):
                    byte += image[ycoord][xcoord]
            byte = toNumeric(byte)
            byte = toBit(byte, mapping)
            intermediateLine.append(byte)
        intermediateMatrix.append(''.join(intermediateLine))
    return intermediateMatrix

def toNumeric(byteString):
    newByte = ''
    for bit in byteString:
        if bit == '.': newByte += '0'
        elif bit == '#': newByte += '1'
    newByte = int(newByte, 2)
    return newByte

def toBit(byte, mapping):
    newBit = mapping[byte]
    return newBit

def niceImage(image):
    nice = ''
    for line in image:
        newline = ''.join(line)
        nice = nice + newline + '\n'    
    return nice
    

# Main Part
fileName = '2021_20.txt'
steps = 50

mapping, image = inputFile(fileName)
print('\n'.join(image))
image = extendImage(image, '.', 120)
for i in range(steps):
    image = enhanceImage(image, steps, mapping)
niceImage = '\n'.join(image)
number = niceImage.count('#')
print(number)
print(niceImage)


