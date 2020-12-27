#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Read Instructions carefully before attempting this assignment

# 1) don't rename any function name
# 2) don't rename any variable name
# 3) don't remove any #comment 
# 4) don't remove """ under triple quate values """
# 5) you have to write code where you found "write your code here"
# 6) after download rename this file with this format "PIAICCompletRollNumber_AssignmentNo.py"
#   Example piaic17896_Assignment1.py
# 7) After complete this assignment please push on your own GitHub repository.
# 8) you can submit this assignment through the google form
# 9) copy this file absolute URL then paste in the google form
#  The example above: https://github.com/EnggQasim/Batch04_to_35/blob/main/Sunday/1_30%20to%203_30/Assignments/assignment1.txt

# * Because all assignment we will be checked through software if you missed any above points 
# * then we can't assign your scores in our database.


# In[3]:


import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
function1()


# In[8]:


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be start from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
   # x = np.arange(1,28,dtype=np.float64).reshape((3,3,3)) #wrtie your code here
    y = np.arange(10,37,dtype = np.int64).reshape((3,3,3))
    
    return y
    """ 
    """
function2()


# In[20]:


#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = []  #wrtie your code here
    for i in range(1,1001):
        if(i%5==0 and i%7==0):
            x.append(i)
    print (x,end = ' ')
function3()


# In[27]:


#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    print("Original array is given below:")
    print(arr)                              #wrtie your code here
    arr[:,[0,1]] = arr[:,[1,0]]
    print("After swapping the columns:")
    return(arr)
function4()


# In[31]:


#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros((4,5)) #wrtie your code here
  
    return z
function5()


# In[54]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr =np.zeros(10,dtype = np.int64)           #wrtie your code here
    arr[4] , arr[7] = 10 ,20    
    return arr
function6()


# In[56]:


#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    #write your code here

    """
    Expected Output:
          array([0, 0, 0, 0], dtype=int64)
    """ 
    y = np.zeros(4,dtype = np.int64)
    return y  
function7()


# In[71]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
     """
     Expected Output:
              array([[6, 6, 6, 6, 6],
                     [6, 6, 6, 6, 6]], dtype=uint32)
     """ 
    
    x = np.full((2,5),6)
    x       #write your code here
    return x
function8()  


# In[122]:


#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    a = np.arange(2,101,2)
    return a
function9()
   


# In[29]:


#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    ans = arr - brr[:,None]
    return ans
     
  
    
function10()


# In[28]:


#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr%2==1] = -1
    return arr
           
function11()


# In[35]:


#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.hstack((arr)) #write your code here 
  
    return ans
function12()
 """
     Expected Output:
              array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
     """ 


# In[27]:


#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    import numpy as np
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    print(f" The array is = \n {arr}")
    print('The numbers which come between 5 and 10 are given below\n:')
    for i in arr:
        if(i>5 and i<10):
            print(i, end = ' ')
function13()


# In[ ]:


#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1) #write reshape code
    ans = #write your code here 
  
    return ans

     """
     Expected Output:
       [array([[10, 11, 12],[13, 14, 15]]), 
        array([[16, 17, 18],[19, 20, 21]]), 
        array([[22, 23, 24],[25, 26, 27]]), 
        array([[28, 29, 30],[31, 32, 33]])]
     """ 


# In[ ]:





# In[81]:


#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = arr[arr[:,1].argsort()] #write your code here 
    """
     Expected Output:
           array([[-4,  1,  7],
                   [ 8,  2, -2],
                   [ 6,  3,  9]])
     """ 
  
    return ans

function15()   


# In[40]:


#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.stack((x,y),axis = -1) #write your code here 
     """
     Expected Output:
                [[[1 2]]

                 [[2 3]]

                 [[3 4]]]
     """ 

    return ans

function16()


# In[17]:


#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    """
array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
      dtype='<U3')
"""
    import numpy as np
    arr = np.arange(1,10*10+1).reshape((10,10)) 
    mask = np.where((arr%3==0 |arr%5==0),"Yes","No")
    return arr[mask]     # Write Your Code HERE
    
function17()


# In[112]:


#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    count = 0                         # Write you code Here
    for i in piaic:
        for j in students:
            if(j==i):
                count+=1
    return count
#Expected output: 3                
function18()


# In[78]:


# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:
     #expected output
    """
    array([[  6,  17,  38,  69, 110],
       [ 17,  54, 101, 158, 225],
       [ 38, 101, 174, 257, 350],
       [ 69, 158, 257, 366, 485],
       [110, 225, 350, 485, 630]])
    """


    X = np.arange(1,26).reshape(5,5)  # Write your code here
    w = X               
    W = np.transpose(w)     # Write your code here
    b =  5                  # Write your code here
    output = (X*W)+b        # Write your code here
    return output         
function19()


# In[113]:


#Task20
def function20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def abc(x):
        return x*2+3-2
    return abc(x)
#Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])

function20()


# In[ ]:





# In[ ]:


# Rough Work.


# In[73]:


x = np.arange(1,26).reshape(5,5)
x


# In[74]:


w = x
w


# In[77]:


W = np.transpose(w)
W


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




