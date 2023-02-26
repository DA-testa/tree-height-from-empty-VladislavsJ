# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    if int(parents[int(n)])==-1:
        return(1)
    else: return compute_height(parents[int(n)],parents)+1
    # Your code here
    return max_height



def main():
    #
    text = int(input())
    print(text)
    nodes= [text]
    nodes = input().split()
    print(nodes[1])
    max_height = 0
    height=0
    for cnt in range(0,text):
        height = compute_height(cnt,nodes)
        if max_height<height:
            max_height=height
    print(max_height)
    #compute_height(text,nodes)
    #if text[0] == 'F':
     #   x = open(text1, "r")
     #   text1 = list(x.read())
    #
    
    #           
    # Printing answer, write your code here
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
