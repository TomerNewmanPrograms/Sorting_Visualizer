import pygame
from pygame.locals import*
import pygame.freetype
import random

TIME = 120
WIDTH = 2
SIZE = 200
width = 1000
height = 500
BACKGROUND = (255, 255, 255)
Color_line=(0, 0, 255)
CLOCK = pygame.time.Clock()
         
    
    
def Display(screen,arr,size,font):
    screen.fill(BACKGROUND)
    
    QuickSortTXT = font.render('For QuickSort press 1', False, (0, 0, 0))
    MergeSortTXT = font.render('For MergeSort press 2', False, (0, 0, 0))
    BubbleSortTXT = font.render('For BubbleSort press 3', False, (0, 0, 0))
    InsertionSortTXT = font.render('For InsertionSort press 4', False, (0, 0, 0))
    QUITTXT = font.render('To Quit press 5', False, (0, 0, 0))
    REGENERATETXT = font.render('To Regenerate another graph press 6', False, (0, 0, 0))
    screen.blit(QuickSortTXT,(3,3))
    screen.blit(MergeSortTXT,(3,26))
    screen.blit(BubbleSortTXT,(3,49))
    screen.blit(InsertionSortTXT,(250,3))
    screen.blit(QUITTXT,(250,26))
    screen.blit(REGENERATETXT,(250, 49))
    pygame.display.flip()
    printArr(screen,arr,Color_line)
    


def GenerateRandArray():
    arr = []
    for i in range(0,SIZE):
        arr.append(random.randrange(1,400))
    return arr    

def GeneratePosArray():
    arr = []
    for i in range(0,SIZE):
        arr.append(60+(4*i))
    return arr

def printArr(screen,arr,color,start=0):
    for i in range(0,len(arr)):
        startingIndex = start + i
        pygame.draw.line(screen,color,(60 + 4*startingIndex,500-arr[i]),(60 + 4*startingIndex,500),WIDTH)
    pygame.display.flip()

def printCell(screen,Cell,Pos,color):
    if color == Color_line:
        pygame.draw.line(screen,Color_line,(Pos,500-Cell),(Pos,500),WIDTH)
    else:
        pygame.draw.line(screen,color,(Pos,50),(Pos,500),WIDTH)       
    pygame.display.flip()




def main():
    pygame.init()
    pygame.font.init()
    MYFONT = pygame.font.SysFont('freesansbold.ttf', 30)
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Sorting Visualizer Algorithm')
    pygame.display.flip()
    arr = GenerateRandArray()
    posArr = GeneratePosArray()
    Display(screen,arr,Color_line,MYFONT)
    toSort = True
    RUNNINGTXT = MYFONT.render('Sorting!!!  Please wait until the end :)', False, (0, 0, 0))
    RETRYTXT = MYFONT.render('Finished!!! To try again press 6! :)', False, (0, 0, 0))
    ENDTXT = MYFONT.render('To Quit press 5! :)', False, (0, 0, 0))
    runned = False
    while toSort:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                    screen.fill(BACKGROUND)
                    printArr(screen,arr,Color_line)
                    screen.blit(RUNNINGTXT,(300,3))
                    runned = True
                  
                if event.key == pygame.K_1:
                    QuickSort(screen,arr,posArr,0,SIZE-1)

                if event.key == pygame.K_2:
                    MergeSort(screen,arr,posArr)

                if event.key == pygame.K_3:
                    BubbleSort(screen,arr,posArr)

                if event.key == pygame.K_4:
                    InsertionSort(screen,arr,posArr)

                if event.key == pygame.K_5:
                    toSort = False

                if runned:
                    screen.fill(BACKGROUND)
                    screen.blit(RETRYTXT,(3,3))
                    screen.blit(ENDTXT,(3,40))
                    printArr(screen,arr,Color_line)
                    pygame.display.flip()
                    runned = False

                if event.key == pygame.K_6:
                    arr = GenerateRandArray()
                    posArr = GeneratePosArray()
                    Display(screen,arr,Color_line,MYFONT)

               



#InsertionSort section
def InsertionSort(screen,arr,posArr):
  
    for i in range(1, SIZE): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                printCell(screen,arr[j+1],posArr[j+1],BACKGROUND)
                arr[j+1] = arr[j]
                printCell(screen,arr[j+1],posArr[j+1],Color_line)
                CLOCK.tick(TIME)   
                j -= 1
        printCell(screen,arr[j+1],posArr[j+1],BACKGROUND)
        arr[j+1] = key
        printCell(screen,arr[j+1],posArr[j+1],Color_line)
        CLOCK.tick(TIME)  
        

#BubbleSort section
def BubbleSort(screen,arr,posArr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                printCell(screen,arr[j],posArr[j],BACKGROUND)
                printCell(screen,arr[j+1],posArr[j+1],BACKGROUND)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                printCell(screen,arr[j],posArr[j],Color_line)
                printCell(screen,arr[j+1],posArr[j+1],Color_line)
                CLOCK.tick(TIME)  
                


 #QuickSort section         
def partition(screen,arr,posArr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end
    while True:       
        while low <= high and arr[high] >= pivot:
            high = high - 1
       
        while low <= high and arr[low] <= pivot:
            low = low + 1

        if low <= high:
            printCell(screen,arr[low],posArr[low],BACKGROUND)
            printCell(screen,arr[high],posArr[high],BACKGROUND)
            arr[low], arr[high] = arr[high], arr[low]
            printCell(screen,arr[low],posArr[low],Color_line)
            printCell(screen,arr[high],posArr[high],Color_line)
            CLOCK.tick(TIME//2)        
        else:          
            break

    printCell(screen,arr[start],posArr[start],BACKGROUND)
    printCell(screen,arr[high],posArr[high],BACKGROUND)
    arr[start], arr[high] = arr[high], arr[start]
    printCell(screen,arr[start],posArr[start],Color_line)
    printCell(screen,arr[high],posArr[high],Color_line)
    CLOCK.tick(TIME//2)
    return high

def QuickSort(screen,arr,posArr,start,end):
    if start >= end:
        return

    p = partition(screen,arr,posArr, start, end)
    QuickSort(screen,arr,posArr, start, p-1)
    QuickSort(screen,arr,posArr, p+1, end)









#MergeSort section
def MergeSort(screen,arr,posArr):
    if len(arr) > 1:
        mid = len(arr)//2
        LeftArr = arr[:mid]
        LeftPosArr = posArr[:mid]
        RightArr = arr[mid:]
        RightPosArr = posArr[mid:]

        MergeSort(screen,LeftArr,LeftPosArr)
        MergeSort(screen,RightArr,RightPosArr)
        i = j = k = 0

        while i < len(LeftArr) and j < len(RightArr):
            printCell(screen,arr[k],posArr[k],BACKGROUND)
            if LeftArr[i] < RightArr[j]:
                arr[k] = LeftArr[i]
                i += 1
                printCell(screen,arr[k],posArr[k],Color_line)
                CLOCK.tick(TIME)
                
            else:
                arr[k] = RightArr[j]
                j += 1              
                printCell(screen,arr[k],posArr[k],Color_line)
                CLOCK.tick(TIME)               
            k += 1
 

        while i < len(LeftArr):
            printCell(screen,arr[k],posArr[k],BACKGROUND)
            arr[k] = LeftArr[i]
            i += 1
            k += 1
            printCell(screen,arr[k-1],posArr[k-1],Color_line)
            CLOCK.tick(TIME)
            
 
        while j < len(RightArr):
            printCell(screen,arr[k],posArr[k],BACKGROUND)
            arr[k] = RightArr[j]
            j += 1
            k += 1
            printCell(screen,arr[k-1],posArr[k-1],Color_line)
            CLOCK.tick(TIME)
            



main()
