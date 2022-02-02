from codecs import backslashreplace_errors
import pygame
from pygame.locals import*
import pygame.freetype
import random

#consts
WIDTH = 3
SIZE = 120
width = 1000
height = 500
BACKGROUND = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
Color_line= (0, 200, 255)
CLOCK = pygame.time.Clock()

#time consts
TIME = 60
MERGE_TIME = TIME//1.5
QSORT_TIME = TIME//2.5
INS_TIME = TIME*2
BUBLS_TIME = TIME*3.5
    
#Printing Functions   
def Display(screen,arr,size,font):
    screen.fill(BACKGROUND)
    QuickSortTXT = font.render('(1) QuickSort', False, BLACK)
    MergeSortTXT = font.render('(2) MergeSort', False, BLACK)
    BubbleSortTXT = font.render('(3) BubbleSort', False, BLACK)
    InsertionSortTXT = font.render('(4) InsertionSort', False, BLACK)
    QUITTXT = font.render('(6) Quit', False, BLACK)
    REGENERATETXT = font.render('(5) Regenerate another graph', False, BLACK)
    screen.blit(QuickSortTXT,(3,3))
    screen.blit(MergeSortTXT,(3,26))
    screen.blit(BubbleSortTXT,(3,49))
    screen.blit(InsertionSortTXT,(250,3))
    screen.blit(QUITTXT,(250,49))
    screen.blit(REGENERATETXT,(250, 26)) 
    pygame.display.flip()
    printArr(screen,arr,Color_line)
    
    #printing the array
def printArr(screen,arr,color,start=0):
    for i in range(0,len(arr)):
        startingIndex = start + i
        pygame.draw.line(screen,color,(60 + WIDTH*2*startingIndex,500-arr[i]),(60 + WIDTH*2*startingIndex,500),WIDTH)
    pygame.display.flip()

#returns the name of the Sort method
def Sort_Name(event_key):
    if(event_key == pygame.K_1):
        return "Quick Sort"
    if(event_key == pygame.K_2):
        return "Merge Sort"
    if(event_key == pygame.K_3):
        return "Bubble Sort"
    if(event_key == pygame.K_4):
        return "Insertion Sort"
    return " "


#printing a single line
def printCell(screen,Cell,Pos,color,time = TIME):
    if color == Color_line:
        pygame.draw.line(screen,RED,(Pos,500-Cell),(Pos,500),WIDTH)
        pygame.display.flip()
        CLOCK.tick(time)
        pygame.draw.line(screen,Color_line,(Pos,500-Cell),(Pos,500),WIDTH)  
    else:
        pygame.draw.line(screen,color,(Pos,50),(Pos,500),WIDTH)     
    pygame.display.flip()



#Generating arrays Functions
def GenerateRandArray():
    arr = []
    for i in range(0,SIZE):
        arr.append(random.randrange(1,400))
    return arr    

def GeneratePosArray():
    arr = []
    for i in range(0,SIZE):
        arr.append(60+(WIDTH*2*i))
    return arr


#InsertionSort section
def InsertionSort(screen,arr,posArr):
  
    for i in range(1, SIZE): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                printCell(screen,arr[j+1],posArr[j+1],BACKGROUND,INS_TIME)
                arr[j+1] = arr[j]
                printCell(screen,arr[j+1],posArr[j+1],Color_line,INS_TIME)  
                j -= 1
        printCell(screen,arr[j+1],posArr[j+1],BACKGROUND,INS_TIME)
        arr[j+1] = key
        printCell(screen,arr[j+1],posArr[j+1],Color_line,INS_TIME)
        

#BubbleSort section
def BubbleSort(screen,arr,posArr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                printCell(screen,arr[j],posArr[j],BACKGROUND,BUBLS_TIME)
                printCell(screen,arr[j+1],posArr[j+1],BACKGROUND,BUBLS_TIME)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                printCell(screen,arr[j],posArr[j],Color_line,BUBLS_TIME)
                printCell(screen,arr[j+1],posArr[j+1],Color_line,BUBLS_TIME)
                 
                


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
            printCell(screen,arr[low],posArr[low],BACKGROUND,QSORT_TIME)
            printCell(screen,arr[high],posArr[high],BACKGROUND,QSORT_TIME)
            arr[low], arr[high] = arr[high], arr[low]
            printCell(screen,arr[low],posArr[low],Color_line,QSORT_TIME)
            printCell(screen,arr[high],posArr[high],Color_line,QSORT_TIME)       
        else:          
            break

    printCell(screen,arr[start],posArr[start],BACKGROUND,QSORT_TIME)
    printCell(screen,arr[high],posArr[high],BACKGROUND,QSORT_TIME)
    arr[start], arr[high] = arr[high], arr[start]
    printCell(screen,arr[start],posArr[start],Color_line,QSORT_TIME)
    printCell(screen,arr[high],posArr[high],Color_line,QSORT_TIME)
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
        #merging the two arrays
        while i < len(LeftArr) and j < len(RightArr):
            printCell(screen,arr[k],posArr[k],BACKGROUND,MERGE_TIME)
            if LeftArr[i] < RightArr[j]:
                arr[k] = LeftArr[i]
                i += 1
                printCell(screen,arr[k],posArr[k],Color_line,MERGE_TIME)
                
            else:
                arr[k] = RightArr[j]
                j += 1              
                printCell(screen,arr[k],posArr[k],Color_line,MERGE_TIME)              
            k += 1
 

        while i < len(LeftArr):
            printCell(screen,arr[k],posArr[k],BACKGROUND,MERGE_TIME)
            arr[k] = LeftArr[i]
            i += 1
            k += 1
            printCell(screen,arr[k-1],posArr[k-1],Color_line,MERGE_TIME)
            
 
        while j < len(RightArr):
            printCell(screen,arr[k],posArr[k],BACKGROUND,MERGE_TIME)
            arr[k] = RightArr[j]
            j += 1
            k += 1
            printCell(screen,arr[k-1],posArr[k-1],Color_line,MERGE_TIME)






            
#Main function
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
    
    FINTXT = MYFONT.render('Finished.', False, (0, 0, 0))
    ENDTXT = MYFONT.render('(5) Try again', False, (0, 0, 0))
    RETRYTXT = MYFONT.render('(6) Quit', False, (0, 0, 0))
    runned = False
    while toSort:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
            if event.type == pygame.KEYDOWN:
                #if some Sort method was chosen:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                    screen.fill(BACKGROUND) 
                    printArr(screen,arr,Color_line)
                    SortName = Sort_Name(event.key)
                    RUNNINGTXT = MYFONT.render(SortName, False, (0, 0, 0))
                    screen.blit(RUNNINGTXT,(420,3))
                    pygame.display.flip()
                    runned = True
                  
                if event.key == pygame.K_1: #User wants to QuickSort
                    QuickSort(screen,arr,posArr,0,SIZE-1)

                if event.key == pygame.K_2: #User wants to MergeSort
                    MergeSort(screen,arr,posArr)

                if event.key == pygame.K_3: #User wants to BubbleSort
                    BubbleSort(screen,arr,posArr)

                if event.key == pygame.K_4: #User wants to InsertionSort
                    InsertionSort(screen,arr,posArr)

                if event.key == pygame.K_6: #User wants a new Try
                    toSort = False

                if event.key == pygame.K_5: #User wants to Quit
                    arr = GenerateRandArray()
                    posArr = GeneratePosArray()
                    Display(screen,arr,Color_line,MYFONT)

                if runned: #if finnished Sorted, a new messege is appeared
                    screen.fill(BACKGROUND)
                    screen.blit(FINTXT,(3,3))
                    screen.blit(ENDTXT,(3,40))
                    screen.blit(RETRYTXT,(3,70))
                    printArr(screen,arr,Color_line)
                    pygame.display.flip()
                    runned = False

                

   

main()
