import pygame
import time
from pygame.locals import *
import random
import pymsgbox as mb
import pyautogui
pygame.init()
# ____________________ seting the display______________________________________
display=pygame.display.set_mode((500,500))
clock=pygame.time.Clock()

################################# game booleans ############################
running=True
cricles=True
crose=False
move=False

row1_s=True
row1_m=True
row1_e=True

row2_s=True
row2_m=True
row2_e=True

row3_s=True
row3_m=True
row3_e=True
# _________________________________________________________________________
pic1=pygame.image.load("pic.png")
pic1=pygame.transform.scale(pic1 ,(100,100))

AI_list=[[78,74], [252,83],  [417,79],
        [78,250], [255,253], [420,258],
        [78,414], [255,421], [413,420]]
# ____________________________________________________________________________
circlepositionList=[[[78,74], [252,83], [417,79]]
,[[78,250],[255,253], [420,258]]
,[[78,414],[255,421], [413,420]]

,[[78,74],[78,250],[78,414]]
,[[252,83],[255,253],[255,421]]
,[[417,79],[420,258], [413,420]]

,[[78,74],[255,253],[413,420]]
,[[417,79],[255,253],[78,414]]]
# _________________________________________________________________________
crosepositionList=[[[78,74], [252,83], [417,79]]
,[[78,250],[255,253], [420,258]]
,[[78,414],[255,421], [413,420]]

,[[78,74],[78,250],[78,414]]
,[[252,83],[255,253],[255,421]]
,[[417,79],[420,258], [413,420]]

,[[78,74],[255,253],[413,420]]
,[[417,79],[255,253],[78,414]]]
# _____________________relative functions to gamewin____________________________
def removeitemcircle(x):
    for item in circlepositionList:
        for i in item:
            try:
                item.remove(x)
            except Exception as e:
                pass
    
def removeitemcrose(x):
    for item in crosepositionList:
        for i in item:
            try:
                item.remove(x)
            except Exception as e:
                pass
# _________________________________________________________________________
def circle():
    for x,y in cricles_position:
        pygame.draw.circle(display,((0,0,0)), (x,y), 50, 10)

def croses():
    for x1,y2 in crose_position:
        display.blit(pic1,(x1-50,y2-50))
# _________________________________________________________________________

def lines():
    display.fill((255,255,255))
    pygame.draw.line(display,((0,0,0)),(0,166),(500,166),10)
    pygame.draw.line(display,((0,0,0)),(0,332),(500,332),10)
    
    pygame.draw.line(display,((0,0,0)),(166,0),(166,500),10)
    pygame.draw.line(display,((0,0,0)),(332,0),(332,500),10)
# _______________________lists for circle and croses_______________________
crose_position=[]
cricles_position=[]
# _________________________________________________________________________
def gamewin():
    for i in range(0,8):
        if circlepositionList[i]==[]:
            mb.confirm("Circle win the game","Win game")
            quit()
    for i in range(0,8):
        if crosepositionList[i]==[]:
            mb.confirm("Crose win the game","Win game")
            quit()
# ++++++++++++++++++++++++++++ function for game reset +++++++++++++++++++++++++++++++++++
def gameresart():
    global AI_list,circlepositionList,crosepositionList,crose_position,cricles_position
    AI_list.clear()
    circlepositionList.clear()
    crosepositionList.clear()
    crose_position.clear()
    cricles_position.clear()

    AI_list=[[78,74],[252,83],[417,79],[78,250],[255,253],[420,258],[78,414],[255,421],[413,420]]
# _________________________________________________________________________
    circlepositionList=[[[78,74], [252,83], [417,79]]
    ,[[78,250],[255,253], [420,258]]
    ,[[78,414],[255,421], [413,420]]

    ,[[78,74],[78,250],[78,414]]
    ,[[252,83],[255,253],[255,421]]
    ,[[417,79],[420,258], [413,420]]

    ,[[78,74],[255,253],[413,420]]
    ,[[417,79],[255,253],[78,414]]]
# _________________________________________________________________________
    crosepositionList=[[[78,74], [252,83], [417,79]]
    ,[[78,250],[255,253], [420,258]]
    ,[[78,414],[255,421], [413,420]]

    ,[[78,74],[78,250],[78,414]]
    ,[[252,83],[255,253],[255,421]]
    ,[[417,79],[420,258], [413,420]]

    ,[[78,74],[255,253],[413,420]]
    ,[[417,79],[255,253],[78,414]]]



# +++++++++++++++++++++ mainloop ++++++++++++++++++++++++++++++  
while running:
    lines()
    croses()
    circle()
    cricles_x_y=[]
    croses_x_y=[]
    gamewin()
    #________________ for Dbugging
    # mouse_position=pygame.mouse.get_pos()
    # print(circlepositionList ,"\n")
    # _________________________________________________________________________
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button== 1:
                if cricles:
                    cricles=False
                    crose=True
                    mouse_position=pygame.mouse.get_pos()
                    if row1_s:
                        if mouse_position[0]<162 and mouse_position[1]<160:
                            cricles_x_y.append(78)
                            cricles_x_y.append(74)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([78,74])
                            removeitemcircle([78,74])
                            row1_s=False
                            break
                    if row1_e: 
                        if mouse_position[0]>338<499 and mouse_position[1]<160:
                            cricles_x_y.append(417)
                            cricles_x_y.append(79)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([417,79])
                            removeitemcircle([417,79])
                            row1_e=False
                            break
                    if row1_m:
                        if mouse_position[0]>162<327 and mouse_position[1]<160:
                            cricles_x_y.append(252)
                            cricles_x_y.append(83)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([252,83])
                            removeitemcircle([252,83])
                            row1_m=False
                            break
                    if row3_s:
                        if mouse_position[0]<163 and mouse_position[1]>338<499:
                            cricles_x_y.append(78)
                            cricles_x_y.append(414)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([78,414])
                            removeitemcircle([78,414])
                            row3_s=False
                            break
                    if row3_e:
                        if mouse_position[0]>338<499 and mouse_position[1]>338<499:
                            cricles_x_y.append(413)
                            cricles_x_y.append(420)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([413,420])
                            removeitemcircle([413,420])
                            row3_e=False
                            break
                    if row3_m:
                        if mouse_position[0]>162<327 and mouse_position[1]>338<499:
                            cricles_x_y.append(255)
                            cricles_x_y.append(421)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([255,421])
                            removeitemcircle([255,421])
                            row3_m=False
                            break
                    if row2_s:
                        if mouse_position[0]<163 and mouse_position[1]>160<326:
                            cricles_x_y.append(78)
                            cricles_x_y.append(250)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([78,250])
                            removeitemcircle([78,250])
                            row2_s=False
                            break
                    if row2_e:
                        if mouse_position[0]>338<499 and mouse_position[1]>160<326:
                            print("work")
                            cricles_x_y.append(420)
                            cricles_x_y.append(258)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([420,258])
                            removeitemcircle([420,258])
                            row2_e=False
                            break
                    if row2_m:
                        if mouse_position[0]>162<327 and mouse_position[1]>160<326:
                            cricles_x_y.append(255)
                            cricles_x_y.append(253)
                            cricles_position.append(cricles_x_y)
                            AI_list.remove([255,253])
                            removeitemcircle([255,253])
                            row2_m=False
                            break



# _____________________ COMPUTER TURN___________________________________
        elif crose:
            crose=False 
            cricles=True
            try:
                list1=random.choice(AI_list)
                removeitemcrose(list1)
                AI_list.remove(list1)
            except Exception as e:
                mb.confirm("Tie!!!!!!!!!!!!!","TIE")
                quit()
            croses_x_y.append(list1[0])
            croses_x_y.append(list1[1])
            crose_position.append(croses_x_y)
# +++++++++++++++++press r to restart the game++++++++++++++++++++++++
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                gameresart()
                row1_s=True
                row1_m=True
                row1_e=True

                row2_s=True
                row2_m=True
                row2_e=True

                row3_s=True
                row3_m=True
                row3_e=True
    

    clock.tick(20)
    pygame.display.update()
# _______________________________THE END_____________________________________