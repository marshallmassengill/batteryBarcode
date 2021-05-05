#!/usr/bin/python3

import os, sys
from PIL import Image

#DPI = 300, 11.811 = DPMM
#16mm x 16mm squares in a row
numSquares = 8  #8 Squares
mode = "1" #1-bit pixel data (black/white)
#~189 dots in 16mm
totalWidth = 189*numSquares
totalHeight = 189
squareSide = 189

barcodeIteration = 0
barcodeMaxValue = 256

while barcodeIteration < barcodeMaxValue:
    binaryFormat = format(barcodeIteration, '08b')
    print("Binary is: " + binaryFormat)
    #make the barcode image and add a 6 pixel border to it
    #base color is black for the border
    barcodeImg = Image.new(mode, (totalWidth+6,totalHeight+6), "black")
    #iterate through the binary string
    i = 0
    for position in binaryFormat:
        if position == "0":
            imagePos = Image.new(mode, (squareSide, squareSide), "white")
        elif position == "1":
            imagePos = Image.new(mode, (squareSide, squareSide), "black")
        else:
            sys.exit("Serious issue, fix it")
        barcodeImg.paste(imagePos, (squareSide*i+3, 3))
        i += 1
    barcodeName = "batteryBarcode_300dpi_value"+ str(barcodeIteration) +".png"
    barcodeImg.save(barcodeName)
    barcodeIteration +=1

#char1 = Image.new(mode, (squareSide, squareSide), "black")

#barcodeImg = Image.new(mode, (totalWidth+6,totalHeight+6), "black")
#barcodeImg.paste(char1, (squareSide*0+3, 3))
#barcodeImg.paste(char2, (squareSide*1+3, 3))
#barcodeImg.paste(char3, (squareSide*2+3, 3))
#barcodeImg.paste(char4, (squareSide*3+3, 3))
#barcodeImg.paste(char5, (squareSide*4+3, 3))
#barcodeImg.paste(char6, (squareSide*5+3, 3))
#barcodeImg.paste(char7, (squareSide*6+3, 3))
#barcodeImg.paste(char8, (squareSide*7+3, 3))
#barcodeImg.show()
#barcodeImg.save('barcodeTest.png')
