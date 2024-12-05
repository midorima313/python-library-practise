import numpy as np 

# creating an array
a = np.array([1,2,3,4]) # this can be a tuple or a dictionary or a iterable
print(a)
print(type(a))
a1 = np.array(())

# array creation method - zeros , ones , full
a2 = np.zeros((3,4) , dtype="int" , order='c')
print(a2)

a3 = np.ones([4,5] , dtype='float' , order='f')
print(a3)

a8 = np.full([3,4] , "Ind" , order='f')
print("full method example" , a8)

ref_array = np.array([[2,3] , [4,5]])
a9 = np.full(ref_array.shape , fill_value=9, like = ref_array)
print("full method with like" , a9)

#----------------------------------------------------------------------------------------------------

# arrange function np.arrange(start , end , step , dtype='int')
a4 = np.arange(10)
print(a4)

a5 = np.arange(2,10,2) # start and stop added
print(a5)

# -------------------------------------------------------------------------------------------------

# linspace 
a6 = np.linspace(2,20,10,endpoint=False,dtype='int')
print(a6)

a7 , steps = np.linspace(0 , 20 , num=10, retstep=True, dtype=int)
print("step value is ", steps)
print(a7)

# ---------------------------------------------------------------------------------------------------------------

# getting version and pre-defined functions

# print(dir(np))

print(np.__version__)

# --------------------------------------------------------------------------------

# numpy.random.random - generate an array of random numbers of flota type
a10 = np.random.random() #-> single value
print(a10)

a11 = np.random.random(10) # -> 1D array with 10 items
print(a11)

a12 = np.random.random([3,2]) #-> 2D array 
print(a12)

# --------------------------------------------------------------------------------------

#numpy.random.randint -> numpy.random.randint(low, high=None, size=None, dtype=int, endpoint=False)

a13 = np.random.randint(2 , high = 200 , size=(4,5))
print(a13)

#-----------------------------------------------------------------------------------

# array inspection
a14 = np.random.randint(2 , high = 200 , size=(4,5))
#shape -> no of row and column
print(a14.shape)
#size -> no of elements
print(a14.size)
#dimension -> array dimension
print(a14.ndim)
#datatype
print(a14.dtype)

#---------------------------------------------------------------------------------

# reshape and resize
ref_array2 = np.array([1,2,3,4,5,6,7,8,9,10,-1,-2])
a15 = ref_array2.reshape(3,4)
print(a15) 

a16 = ref_array2.resize(3,4)
print(a16) #-> this will give None because line 89 is not returning anything. its making changes to the original array
print(ref_array2)

ref_array3 = np.array([1,2,3,4,5,6,7,8,9,10,-1,-2])
ref_array3.resize(5,4)
print(ref_array3) # in resize if new size is smaller than original it will ignore extra elements and if more, it will add zero to fill the array

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# array mathematics 

#sum
a17 = np.array([2,3,4,5,6])
print(np.sum(a17))
print(a17.sum())

# column wise addition
a18 = np.array([[10,20],[10,20]])
print(np.sum(a18,axis=0))

#row-wise addition
print(np.sum(a18 , axis=1))

# add/subtract/multiply/divide two array - element-wise
a19 = np.array([1,2,3])
a20 = np.array([4,5,6])
print(np.add(a19,a20))
print(np.subtract(a19,a20))
print(np.multiply(a19,a20))
print(np.divide(a19,a20))

#list as input. also works with tuples , dictionary
l1 = [1,2,3]
l2 = [4,5,6]
print(np.add(l1,l2))
print(type(np.add(l1,l2)))

# floor , ceil
a20 = np.array([7,6,17])
a21 = np.array([2,5,4])
print("divide -> " , np.divide(a20,a21))
print("divide -> to type int " , np.divide(a20,a21).astype(int))
print("divide floor ->" , np.floor(np.divide(a20,a21).astype(int)))
print("divide floor ->" , np.ceil(np.divide(a20,a21).astype(int)))

#-------------------------------------------------------------------------------------------------------------------------

# equal and array_equal
# element-wise comparison and returns the return in an nd array - equal()
a22 = np.array([11,55,90])
a23 = np.array([20,2,45])
print(np.equal(a22,a23)) 

t1 = (10,20)
l3 = [10 , 40]
print(np.equal(t1,l3)) 

#array_equal -> checking the overall array and returnig a boolean -> array_equal
print(np.array_equal(a22,a23))
print(np.array_equal(t1,l3)) 

#-------------------------------------------------------------------------------------------------------

# numpy.random.seed() -> create the same sets of random numbers based on the seed value
a24 = np.random.random([2,3])
a25 = np.random.random([2,3])
print("is a24's elements equal to the elements of a25" , np.equal(a24,25)) # false

np.random.seed(12345)
a26 = np.random.random([2,4])
# call the random.seed() method before random.random() method
np.random.seed(12345)
a27 = np.random.random([2,4])
print(a26)
print(a27)
print("is a26 equall to a27" , np.equal(a26,a27))

#------------------------------------------------------------------------------------------------------------

# Aggregate functions - sum, median, mean, max, min, standard deviation

a28 = np.random.randint(0,100 ,[25])
print(a28)
sum = a28.sum()
print("sum->",sum)
median = np.median(a28)
print("median->",median)
print("mean->",a28.mean())
print("min->",a28.min())
print("max->",a28.max())
print("standard deviation->",a28.std())

#-------------------------------------------------------------------------------------------------------------------------

#Exploration of Array
#Slicing - Remember the syntax. simialr to list - [start:stop:step]
a29 = np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
# 1D array
print(a29[1:7])
print(a29[:])
print(a29.size)
print(a29[-15:15])

# 2D array [row-start : row-end , col-start:col-end]
a30 = np.random.randint(0 , 100 , [3,3])
print(a30)
print(a30[1:3 , 1:3])

#--------------------------------------------------------------------------------------------------------------------------------------

#Concate -> joins a sequence of array in an already existing axis
a31 = np.array([1,2,3,4])
a32 = np.array([10,20,30])
print(np.concatenate((a31,a32) , axis=0))
# print(np.concatenate((a31,a32) , axis=1)) -> error because this is a 1d array and there is no columns i.e no pre-defined axis 1 

a33 = np.array([[1,2] , [3,4]])
a34 = np.array([[5,6] , [7,8]])
print(np.concatenate([a33 , a34] , axis=1)) # column wise
print(np.concatenate([a33 , a34] , axis=0)) # row wise

# vstack -> row-wise or vertical stacking of rows of array
print(np.vstack([a33 , a34]))

# hstack -> column-wise or horizontal stacking of columns of array
print(np.hstack([a34 , a33]))

#----------------------------------------------------------------------------------

#column_stack - this is a handy method which can be used for combining many same sized array into a single 2d array where each individual array becomes a column of the resulting array
a35 = np.array(['a','a','a'])
a36 = np.array(['b','b','b'])
a37 = np.array(['c','c','c'])
a38 = np.column_stack((a35 , a36 , a37))
print(a38)

a39 = np.array([[1,2,3] , [4,5,6]])
a40 = np.array([[7,8,9] , [10,11,12]])
a41 = np.column_stack((a39,a40))
print(a41)

#-------------------------------------------------------------------------------------

#hsplit -> split the array horizontally or column-wise np.hsplit(array , index_of_section)
a42 = np.array([1,2,3,4,5,56,6,9])
a43 = np.hsplit(a42 , 2)
print(a43)
print(a43[0])

a44 = np.array([[1,2,3,4] , [5,6,7,8]])
a45 = np.hsplit(a44 , 2)
print(a45)

#vsplit
a46 = np.array([[1,2,3,4] , [5,6,7,8] , [9,10,11,12] , [13,14,15,16]])
a47 = np.vsplit(a46 , 2)
print(a47)

#--------------------------------------------------------------------------------------------------------

#transpose , dot-product , cross-product 
a48 = np.array([1,2,3,4,5,6,7,8])
a48.resize((2,4))
print(a48)
print(a48.T)
print("dot product ->",a48.dot(a48.T))
print("cross product ->",np.cross(a48 , a48.T))







