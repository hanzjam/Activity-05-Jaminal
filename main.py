#Activity 5
import cv2 as cv
import numpy as np

def type_data(babypic):
    datum = babypic.dtype
    print("_______________________________________________________")
    print("Image Data Type")
    print("Type of the Image is: ",datum)

def bilang(babypic):
    total = 150000 
    pix = len(babypic[0]) * len(babypic)
    print("_______________________________________________________")
    print("Image Total Pixel Count: ")
    if total == pix:
        edi = "The loaded image is just right!"
    elif total > pix:
        edi = "The loaded image has lower pixel count."
    else:
        edi = "The loaded image has higher pixel count."
        
    print("Image:  ",pix)
    print("Fixed count: ",total)
    print("Result:",edi)
    type_data(babypic)

def another(babypic):
    ano1 = babypic.shape
    ex = 687
    why = 860
    if ano1[0] <= ex and ano1[1] <= why:
        msg = "Just right!"
    else:
        msg = "Wrong input of dimension of image!"
        
    print("_______________________________________________________")
    print("Image Dimension")
    print("Input:  Y:",ano1[0],"X:",ano1[1])
    print("Original: Y:",why,"X:",ex)
    print("The Result: ",msg)
    bilang(babypic)

def blank(babypic,ex,why,clr):
    if clr == 0:
        cn = "Blue"
    elif clr == 1:
        cn = "Green"
    elif clr == 2:
        cn = "Red"

    picture = babypic.item(ex,why,clr)
    print("\nPixel is: ",cn,"Value")
    print("Value is : ",picture)

    before = babypic[ex,why]
    print("             _________________")
    print("             |Blue |Green|Red|")
    print("             |---------------|")
    print("Before Value |",before,"|")
    print("             |---------------|")

    cv.imshow("Before Value",babypic)
    cv.waitKey(0)
    cv.destroyAllWindows()

    modify = int(input("\nModify the value: "))
    babypic.itemset((ex,why,clr), modify)
    pixy = babypic[ex,why]
    print("\n             _________________")
    print("             |Blue |Green|Red|")
    print("             |---------------|")
    print("After Value  |",pixy,"|")
    print("             |---------------|")
    
    cv.imshow("After Value",babypic)
    cv.waitKey(0)
    cv.destroyAllWindows()
    another(babypic)

def go_to(babypic):
    print("Input the: ")
    ex = int(input("X: "))
    why = int(input("Y: "))
    while True:
        clr = int(input("Color Channel: "))
        if clr <= 2:
            blank(babypic,ex,why,clr)
            break
        else:
            print("Wrong input in Color Channel -- Put 0 if Blue; 1 if Green; 2 if Red")



babypic = cv.imread("mybabies.jpg")
bw = babypic.shape
if bw[2] == 3:
    go_to(babypic)
elif bw[2] >= 2:
    print("Image is Grayscale!")
    exit



