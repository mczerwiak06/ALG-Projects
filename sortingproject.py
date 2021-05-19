import time
import random
import copy
import sys

sys.setrecursionlimit(10**6)

###quicksort###
def partition(arr, p, r):
    pivot = arr[r]
    smaller = p
    for j in range(p, r):
        if arr[j] <= pivot:
            arr[smaller], arr[j] = arr[j], arr[smaller]
            smaller = smaller + 1

    arr[smaller], arr[r] = arr[r], arr[smaller]

    return smaller


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
   
###heapsort###
#tworzenie kopca
def tworzKopiec(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        tworzKopiec(arr, n, largest)
       
def tworzKopiec1(arr):
    n=len(arr)
    for i in range(n//2 - 1, -1, -1):
        tworzKopiec(arr,n,i)
       
#sortowanie
def sortujKopiec(arr):
    n = len(arr)
    tworzKopiec1(arr)
    for i in range(n -1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i]
        tworzKopiec(arr, i, 0)
 
###bubblesort###
def bubblesort(arr): 
    for i in range(len(arr)):
        j=len(arr)-1 
        while j>i:   
            if arr[j]<arr[j-1]:
                tmp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=tmp
            j-=1




#wypelnianie tablicy losowymi liczbami
list = [random.randint(-100,100) for _ in range(2500)]
#tworzenie płytkich kopi tablicy vet na potrzeby testów

tabtest1 = copy.copy(list)
tabtest2 = copy.copy(list)
tabtest3 = copy.copy(list)

#sorotowanie listy do testów
list.sort(reverse=True)
#list.sort()

#kopiowanie listy do testów
sortedtab1 = copy.copy(list)
sortedtab2 = copy.copy(list)
sortedtab3 = copy.copy(list)

################## sortowanie list nieposortowanych ###################
#pomiar dla quicksort:
#print("tabtest1: ")
#print(tabtest1)
#start_time = time.time()
#quicksort(tabtest1, 0, len(tabtest1)-1)
#print("Posortowanie quicksort zajęło: %s sec" % (time.time() - start_time))
#print("tabtest1 sort:")
#print(tabtest1)

#pomiar dla heapsort:
#print("tabtest2: ")
#print(tabtest2)
#start_time = time.time()
#tworzKopiec(tabtest2, len(tabtest2), 0)
#sortujKopiec(tabtest2)
#print("Posortowanie heapsort zajęło: %s sec" % (time.time() - start_time))
#print("tabtest2 sort:")
#print(tabtest2)

#pomiar dla bubblesort:
#print("tabtest3: ")
#print(tabtest3)
#start_time = time.time()
#bubblesort(tabtest3)
#print("Posortowanie bubble zajęło: %s sec" % (time.time() - start_time))
#print("tabtest3 sort:")
#print(tabtest3)

################## sortowanie list posortowanych  ###################
#pomiar dla quicksort:
#print("sortedtab1: ")
#print(sortedtab1)
start_time = time.time()
quicksort(sortedtab1, 0, len(sortedtab1)-1)
print("Posortowanie quicksort zajęło: %s sec" % (time.time() - start_time))
#print("sortedtab1 sort:")
#print(sortedtab1)

#pomiar dla heapsort:
#print("sortedtab2: ")
#print(sortedtab2)
start_time = time.time()
tworzKopiec(sortedtab2, len(sortedtab2), 0)
sortujKopiec(sortedtab2)
print("Posortowanie heapsort zajęło: %s sec" % (time.time() - start_time))

#pomiar dla bubblesort:
#print("sortedtab3: ")
#print(sortedtab3)
start_time = time.time()
bubblesort(sortedtab3)
print("Posortowanie bubble zajęło: %s sec" % (time.time() - start_time))
#print("sortedtab3 sort:")
#print(sortedtab3)
