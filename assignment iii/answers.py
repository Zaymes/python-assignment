

# bubble sort

def bubble_sort(li):
    length = len(li)
    for i in reversed(range(length)):
        for j in range(length):
            if j<i:
                if li[j] > li[j+1]:
                    a = li[j]
                    li[j] = li[j+1]
                    li[j+1] = a
            else:
                break
        print(li[i])
    return li


print(bubble_sort([2,1,4,5,8,7,6,9]))





# Insertion sort

def insertion_sort(li):
    li_len = len(li)
    for i in range(li_len):
        for j in reversed(range(li_len)):
            if j!= 0:
                if li[j] < li[j-1]:
                    a = li[j]
                    li[j] = li[j-1]
                    li[j-1] = a
            else:
                break
    return li


print(insertion_sort([2,1,4,5,8,7,6,9]))





#  Quick sort

def partition(li, low, high):
    i = low-1
    pivot = li[high]

    for j in range(low, high):
        if pivot > li[j]:
            i += 1
            li[i], li[j] = li[j], li[i]

    li[i+1], li[high] = li[high], li[i+1]
    print(li)
    return i+1



def quick_sort(li, low , high):

    if low < high:

        pi = partition(li, low ,high)

        quick_sort(li, low, pi-1 )
        quick_sort(li, pi+1, high)

li =[10,7,8,9,1,5]
n = len(li)
quick_sort(li,0,n-1)
print(li)
            





# binary search

def binary_search1(li,low,high, item):
    mid = int((low+high)/2)
    length = len(li[low:high])

    if length == 0 :
        return -1

    else:
        if item > li[mid]:
            return binary_search1(li, mid+1, high, item)
        elif item < li[mid]:
            return binary_search1(li, low, mid, item)
        elif item == li[mid]:
            return item, mid


item, index = binary_search1([1,2,3,4,5,6,7,8,9,10], 0, 9, 9)
print('The item: {} is in index {}'.format(item, index))





# merge sort


# merge sort

def merge(l1,l2,l3):
    i=j=k=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l3[k] = l1[i]
            i += 1
        else:
            l3[k] = l2[j]
            j += 1
        k+=1
    while i<len(l1):
        l3[k] = l1[i]
        i+=1
        k+=1
    while j<len(l2):
        l3[k] = l2[j]
        j+=1
        k+=1


def merge_sort(li):
    if len(li)>1:
        mid = len(li)//2
        L = li[:mid]
        R = li[mid:]

        merge_sort(L)
        merge_sort(R)

        merge(L,R,li)

        return li




#linear search

def linear_search(li,x):
    for item in li:
        if x == item:
            return item
    return -1


linear_search([1,2,3,4,5,6,7],7)



# interpolation search

def interpolation_search(li,low, high, x):
    

    if (low<=high and x>=li[low] and x<=li[high]):

        position = low + ((high-low)//(li[high]-li[low])*(x-li[low]))

        if li[position] == x:
            return position

        elif x>li[position]:
            return interpolation_search(li,position+1, high, x)
        
        elif x<li[position]:
            return interpolation_search(li,low,position-1,x)
    
    return -1

arr = [ 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 ]  

n = len(arr)

interpolation_search(arr, 0, n-1, 16)






# Dijkstra’s Algorithm


import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    def minDistance(self, dist, sptSet):
        global min_index
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0)





# tower of hanoi for 'n' number of disks

def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))
        return

    hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)


disks = int(input('Enter number of disks: '))
hanoi(disks, 'A', 'B', 'C')