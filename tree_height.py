# python3

import sys
import threading

def compute_height(n,parents):
    # Write this function
    if n != len(parents):
        print("size \"n\" don't match with nodes amount ")
        return -1
    
    #recursion don't work it became too deep for solving, 
    #I have to use array to save heights of previous nodes
    heights = [0]*n
    # if nodeNum<cnt: mean that this cnt number already calculated, and I can take it from array nodeNum
    # if not, go to next branch, until -1 or nodeNum<cnt
    max_height = 0
    for cnt in range(len(parents)):
        height=0
        nodeNum=int(cnt)
        while int(parents[nodeNum]) != -1:
                if nodeNum<cnt:
                    height += heights[nodeNum]
                    break
                else:    
                    nodeNum = int(parents[nodeNum])
                    height+=1
        heights[int(cnt)]=height
        if height>max_height:
            max_height=height+1

    return max_height

def main():
    file_terminal = input()
    FileContains_a=False
    if file_terminal[0] == 'F':
        FileLocation = input()
        
        file_name = FileLocation.split("/")
        if "a" in file_name[-1]:
            print("file name have letter a")
            FileContains_a=True
            return
        # FileLocation = path + /fileName
        #for github + /test/.
        text1 = (open("/test/." + FileLocation, "r").read()).split("\n")
        # don't allow file names with letter a
        
        nodeCnt = int(text1[0]) 
        parents=text1[1].split()
        
    elif file_terminal[0] == 'I':     
        nodeCnt = int(input())
        #parents= [text]
        parents = input().split()
    if not FileContains_a:
        height = compute_height(nodeCnt,parents)
        print(height)

    # Printing answer, write your code here
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
