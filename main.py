"""I/O System Game"""

import sys,os
import pygame
from pygame.locals import *
import time
from tkinter import *
from tkinter import messagebox

pygame.init()


Tk().wm_withdraw() #to hide the main window

# Intialize the pygame
"""Constants for I/O System."""

WINDOW_RESOLUTION = (1351, 900)
WINDOW_NAME = "I/O System Game"

"""Background Image."""
BACKGROUND_IMAGE = sys.path[0]
YES_IMAGE =sys.path[0]
NO_IMAGE = sys.path[0]
IO_Call = sys.path[0]
up_Arrow =sys.path[0]
down_Arrow=sys.path[0]
system_call=sys.path[0]
rfsystem_call=sys.path[0]
dController=sys.path[0]
interrupts=sys.path[0]

yesIoProcessImage1 = sys.path[0]
yesIoProcessImage2 = sys.path[0]

noProcessImage1 = sys.path[0]
noProcessImage2 = sys.path[0]
noProcessImage3 = sys.path[0]
noProcessImage4 = sys.path[0]
noProcessImage5 = sys.path[0]
noProcessImage6 = sys.path[0]
noProcessImage7 = sys.path[0]
noProcessImage8 = sys.path[0]


bgImage=os.path.join(BACKGROUND_IMAGE,'./images/os-game.png')
yesImage=os.path.join(YES_IMAGE,'./icons/3770375-social-media-slang-bubbles/png/yes.png')
noImage = os.path.join(NO_IMAGE,'./icons/3770375-social-media-slang-bubbles/png/no.png')
ioImage = os.path.join(IO_Call,"./images/all/system_call.png")
upImage = os.path.join(up_Arrow,"./images/all/up_arrow.png")
downImage = os.path.join(down_Arrow,"./images/all/down_arrow.png")
systemCall=os.path.join(system_call,"./images/all/system_call.png")
rfSystemCall=os.path.join(rfsystem_call,"./images/all/return_from_system_call.png")
deviceController=os.path.join(dController,"./images/no/device_controller_commands.png")
interruptMe=os.path.join(interrupts,"./images/no/interrupt.png")
yesIoProcessImage1= os.path.join(down_Arrow,"./images/yes/1.png")
yesIoProcessImage2= os.path.join(down_Arrow,"./images/yes/2.png")

noIoProcessImage1= os.path.join(down_Arrow,"./images/no/1.png")
noIoProcessImage2= os.path.join(down_Arrow,"./images/no/2.png")
noIoProcessImage3= os.path.join(down_Arrow,"./images/no/3.png")
noIoProcessImage4= os.path.join(down_Arrow,"./images/no/4.png")
noIoProcessImage5= os.path.join(down_Arrow,"./images/no/5.png")
noIoProcessImage6= os.path.join(down_Arrow,"./images/no/6.png")
noIoProcessImage7= os.path.join(down_Arrow,"./images/no/7.png")
noIoProcessImage8= os.path.join(down_Arrow,"./images/no/8.png")
BACKGROUND_POSITION = (0, 0)
BACKGROUND_COLOR = (255, 255, 255)
# create the screen
screen = pygame.display.set_mode(WINDOW_RESOLUTION)

# Caption and Icon
pygame.display.set_caption(WINDOW_NAME)
# icon = pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)
yesIcon = pygame.image.load(yesImage)
noIcon = pygame.image.load(noImage)
upIcon = pygame.image.load(upImage)
downIcon = pygame.image.load(downImage)
ioIcon = pygame.image.load(ioImage)
systemCallIcon = pygame.image.load(systemCall)
rfSystemCallIcon= pygame.image.load(rfSystemCall)
devConIcon=pygame.image.load(deviceController)
interrIcon=pygame.image.load(interruptMe)

yesIoImage1 = pygame.image.load(yesIoProcessImage1)
yesIoImage2 = pygame.image.load(yesIoProcessImage2)

noIoImage1 = pygame.image.load(noIoProcessImage1)
noIoImage2 = pygame.image.load(noIoProcessImage2)
noIoImage3 = pygame.image.load(noIoProcessImage3)
noIoImage4 = pygame.image.load(noIoProcessImage4)
noIoImage5 = pygame.image.load(noIoProcessImage5)
noIoImage6 = pygame.image.load(noIoProcessImage6)
noIoImage7 = pygame.image.load(noIoProcessImage7)
noIoImage8 = pygame.image.load(noIoProcessImage8)


yesX,yesY =225,300


noX,noY = 150,300
scIconX,scIconY=160,260
rfscIconX,rfscIconY=1025,270
downX,downY=185,230
downX2,downY2=185,390
downX3,downY3=185,520
downX4,downY4=185,660
devCX,devCY=130,700
interX,interY=1100,725


rightX,rightY=235,300
rightX2,rightY2=750,300 
rightX3,rightY3=200,750


upX,upY=1100,250
upX2,upY2=1100,710
upX3,upY3=1100,630
upX4,upY4=1100,550
upX5,upY5=1100,305          
ioX,ioY=120,240
yesImage1X,yesImage1Y = 300,40


def rotateimg(img,arrowspin):
    return pygame.transform.rotate(img,arrowspin)

def yesLocation(img,x,y):
    screen.blit(img, (yesX,yesY))

def noLocation(x,y):
   screen.blit(noIcon, (noX,noY))

def ioCallLocation(x,y):
    screen.blit(ioIcon,ioX,ioY)

def upLocation(x,y):
   screen.blit(upIcon,(upX,upY))
def systemCallLocation(x,y):
    screen.blit(systemCallIcon,(scIconX,scIconY))

def rfsystemCallLocation(x,y):
    screen.blit(rfSystemCallIcon,(rfscIconX,rfscIconY))


def devConLoc(x,y):
    screen.blit(devConIcon,(devCX,devCY))

def interrLoc(x,y):
    screen.blit(interrIcon,(interX,interY))

def image1Loc(x,y):
    screen.blit(yesIoImage1,(yesImage1X,yesImage1Y))
    
def image2Loc(x,y):
    screen.blit(yesIoImage2,(yesImage1X,yesImage1Y))

def image3Loc(x,y):
    screen.blit(noIoImage1,(yesImage1X,yesImage1Y)) 

def image4Loc(x,y):
     screen.blit(noIoImage2,(yesImage1X,yesImage1Y))

def image5Loc(x,y):
     screen.blit(noIoImage3,(yesImage1X,yesImage1Y))

def image6Loc(x,y):
     screen.blit(noIoImage4,(yesImage1X,yesImage1Y))

def image7Loc(x,y):
     screen.blit(noIoImage5,(yesImage1X,yesImage1Y))

def image8Loc(x,y):
    screen.blit(noIoImage6,(yesImage1X,yesImage1Y))

def image9Loc(x,y):
    screen.blit(noIoImage7,(yesImage1X,yesImage1Y))

def image10Loc(x,y):
    screen.blit(noIoImage8,(yesImage1X,yesImage1Y))          





####Down Locations#####
def downLocation(x,y):
    screen.blit(downIcon,(downX,downY))

def downLocation2(x,y):
    screen.blit(downIcon,(downX2,downY2))

def downLocation3(x,y):
    screen.blit(downIcon,(downX3,downY3))

def downLocation4(x,y):
        screen.blit(downIcon,(downX4,downY4))   




###Right Locations####
def rightLocation(x,y):
    rightimg=rotateimg(downIcon,100)
    screen.blit(rightimg,(rightX,rightY))

def rightLocation2(x,y):
    rightimg=rotateimg(downIcon,100)
    screen.blit(rightimg,(rightX2,rightY2))  
    

def rightLocation3(x,y):
    rightimg=rotateimg(downIcon,100)
    screen.blit(rightimg,(rightX3,rightY3))


 ###Up Locations###
def upLocation(x,y):
    upimg=rotateimg(downIcon,180)
    screen.blit(upimg,(upX,upY))

def upLocation2(x,y):
    upimg=rotateimg(downIcon,180)
    screen.blit(upimg,(upX2,upY2))        

def upLocation3(x,y):
    upimg=rotateimg(downIcon,180)
    screen.blit(upimg,(upX3,upY3)) 

def upLocation4(x,y):
    upimg=rotateimg(downIcon,180)
    screen.blit(upimg,(upX4,upY4)) 

def upLocation5(x,y):
    upimg=rotateimg(downIcon,180)
    screen.blit(upimg,(upX5,upY5))        


def ProcessThroughIo(counter,spinner):
    

    if(counter==1):
        image1Loc(yesImage1X,yesImage1Y)
        downLocation(downX,downY)
        systemCallLocation(scIconX,scIconY)
        
        
    if(counter==2):
        image2Loc(yesImage1X,yesImage1Y)
    
        rightLocation(rightX,rightY)
        if spinner<=360:
            yesimg=rotateimg(yesIcon,spinner)
            yesLocation(yesimg,yesX,yesY)
        else:
            yesLocation(yesIcon,yesX,yesY)


    if(counter==3):
        image2Loc(yesImage1X,yesImage1Y)
       
        upLocation5(upX5,upY5)
        rfsystemCallLocation(rfscIconX,rfscIconY)    
        
    if(counter==4):
        image3Loc(yesImage1X,yesImage1Y)
        downLocation2(downX2,downY2)
        noLocation(noX,noY)
    if(counter==5):
        image4Loc(yesImage1X,yesImage1Y)
        downLocation3(downX3,downY3)

    if(counter==6):
        image5Loc(yesImage1X,yesImage1Y)

        devConLoc(devCX,devCY)
        downLocation4(downX4,downY4)

    if(counter==7):
        image6Loc(yesImage1X,yesImage1Y)
    
        rightLocation3(rightX3,rightY3)

    if(counter==8):
        image7Loc(yesImage1X,yesImage1Y)
        upLocation2(upX2,upY2)


    if(counter==9):
         upLocation3(upX3,upY3)
         image8Loc(yesImage1X,yesImage1Y)
        #image8Loc(yesImage1X,yesImage1Y)    
    if(counter==10):
        upLocation4(upX4,upY4)
        image9Loc(yesImage1X,yesImage1Y) 
        #image9Loc(yesImage1X,yesImage1Y)

    if(counter==11):
        upLocation5(upX5,upY5)
        image10Loc(yesImage1X,yesImage1Y)
        #image10Loc(yesImage1X,yesImage1Y)

    











def ProcessBackIo(counter,spinner):
    if(counter==1):
        image1Loc(yesImage1X,yesImage1Y)
   

running = True
countOps=0
spinner = 0
messagebox.showinfo('View','Use Left or Right Directional to Navigate')
while running:
    
    screen.fill(BACKGROUND_COLOR)
    mx,my = pygame.mouse.get_pos()
    
    background = pygame.image.load(bgImage)
    
   
    screen.blit(background, BACKGROUND_POSITION)
    
    
    downLocation(downX,downY)
    
    for event in pygame.event.get():
        #Getting the coordinates of cursor during run
        
        
        pos = pygame.mouse.get_pos()
        

        if event.type == pygame.QUIT:
            running = False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
                
                    #Would like it to generate new images at this point on click.
                    print("Mouse Clicked over Image")
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                countOps+=1
                print("Right key Pressed")
               
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                countOps-=1
                print("Left key Pressed")

    ProcessThroughIo(countOps,spinner)
    spinner+=5
    
    ProcessBackIo(countOps,spinner)
   
    if(countOps<=0):
        downX,downY=1350,1350

    if(countOps==1):
        downY+=2
        if(downY>=298):
           downX,downY=185,230
           downLocation(downX,downY)
           
    if(countOps==2):
        downX,downY=1350,1350   
        rightX+=6
        
        if(rightX>=560):
            rightX,rightY=235,300
            rightLocation(rightX,rightY)
    #    rightX,rightY=1350,1350
    #    rightX2+=6
    #    rightLocation2(rightX2,rightY2)        
    #if(rightX2>=1000): 
    #    rightX2,rightY2=1350,1350
    #    upY-=0.6
    #    upLocation(upX,upY)
    #if(upY<=200):
    #     upX,upY=1350,1350
    if(countOps==3):
        upY5-=4
        if(upY5<=230):
            upX5,upY5=1100,305
            upLocation5(upX5,upY5)     
          
    if(countOps==4):
        rightX,rightY=1350,1350
        downY2+=1
        if(downY2>=425):
           downX2,downY2=185,390    
           downLocation2(downX2,downY2)

    if(countOps==5):
        downX2,downY2=1350,1350
        downY3+=1
        if(downY3>=540):
            downX3,downY3=185,520
            downLocation3(downX3,downY3)
    if(countOps==6):
        downX3,downY3=1350,1350
        downY4+=2
        if(downY4>=730):
            downX4,downY4=185,660
            downLocation3(downX4,downY4)

    if(countOps==7):
        downX4,downY4==1350,1350
        rightX3+=6
        if(rightX3>=576):
            rightX3,rightY3=210,750
            rightLocation3(rightX3,rightY3)

    if(countOps==8):
        rightX3,rightY3=1350,1350
        upY2 -=1
        if(upY2<=710):
            upX2,upY2=1100,720
    if(countOps==9):
        upY3-=0.5
        if(upY3<=630):
            upX3,upY3=1100,650
            upLocation3(upX3,upY3)

    if(countOps==10):
        upY4-=4
        if(upY4<=363):
            upX4,upY4=1100,540
            upLocation4(upX4,upY4)

    if(countOps==11):
        upY5-=4
        if(upY5<=230):
            upX5,upY5=1100,305
            upLocation5(upX5,upY5)                  


    pygame.display.update()