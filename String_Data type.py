#!/usr/bin/env python
# coding: utf-8

# ### Strings
# - Strings are characters or a sequence of characters enclosed in single quotes ('') or double  quotes (" ") or triple quotes
# (''' ''').
# - Triple -quotes are used as multiline strings,multiline comments and as doc strings.
# - It is an immutable data type, which means once a string is created, it cannot be modified.
# - However, it is possible to create a new string by concatenating two or more strings

# In[3]:


### Creating a string
s1 = 'this is a string, enclosed in single quotes'
s2 = 'this is a string, enclosed in single quotes'
s3 = '''this is a multi-string, 
enclosed in triple single quotes'''
print(s1, s2, s3, sep='\n')

"""this is an informative
multi-line comment,
created by using triple double quotes"""


# In[5]:


# Complier error 
a = "this cup now belong's to INDIA" #other way to print
print(a)
b = 'this cup now belong\'s to INDIA' # \ is a escape character
print(b)


# In[5]:


### Escape character
print('a\n') # new line
print('a\tb') # tab/ four spaces
print('ab\rc') # moves the cursor to start of the line


# ### Raw-string and format-string
# - Reading everything in raw form .
# - A special type of string that allows you to include backslashes ( \ ) without interpreting them as escape sequences.

# In[6]:


# r-strings
print('c:\abc\newfolder\j.jpg')# compliers error
print('c:\\abc\\newfolder\\j.jpg') # alternative method of printing
print(r'c:\abc\newfolder\j.jpg') # using r string




# In[7]:


r ,h = 5,7
vol = (22/7)*(r**2)*h
print('the volume of a cyl, whose radius is', r,'whose h is', h, 'is', vol)
print(f'the vol of cyl whose r and h are {r} and {h} respectively is {vol}')


# In[4]:


### Format-string
Example for formatting string:
volume of a sphere

print(f'a sphere with diameter {10} cms, volume will be {(22/7)*((10/2)**3)*(4/3)} cubic cms')


# ## String Indexing:
# 
# - strings can be indexed :“Indexing” means referring to an element of an iterable by its position within the iterable.
# - since strings are sequence of chars,and this seq has an indexing value.
# 
# - Indexing is of two types:
# - Accessing Characters by Positive Index Number
# - Accessing Characters by Negative Index Number
# 

# In[14]:


# positive indexing :
    
In positive indexing ,we move from left to right and the start index is '0' and the end index is 'n-1'
where n is len of the string.
x = 'Python'
print(x[3]) # accessing h using postive indexing (left to right starts with 0 and end with n-1)


# # Negative indexing:
#     
# - In negative indexing ,we move from right to left and the start index is '-1' and the end index is '-n'
# - where n is len of the string.backward direction indexing

# In[ ]:


print(x[-3]) # accessing 'h' using negative indexing (right to left starts with -1 and end index is -n)


# In[20]:


x = 'abAcBde'
print(x[4])


# # Slicing 
# - The extraction of a part of a string, list, or tuple.
# 
# - it can be viewed as : Collection[start:end:step]
# - start position is a and end is n so we start with a and we stop until m as n is not considered
# 
# [start
# end
# step sclicing]
# ## syntax for slicing 
#  -  var[start_index:end index:step_size]
#     

# In[22]:


x = 'i am not sure what to take as an example'
#len(x)
x[0:13]


# In[24]:


### Slicing (positive indexing)
x = 'i am not sure what to take as an example'
print(len(x))
print(x[0:13])
print(x[0:41])
print(x[0:41:2])
print(x[0:41:1])
print(x[::])


# In[26]:


print('abc', 'def')
print('xyz')


# In[28]:


### Reversing the string\\ Negative Indexing
x = 'python'
print(x)
print(x[::-1])


# In[30]:


x[::-1]


# In[32]:


x[-1:-7:-1]


# In[35]:


x[6:0:-1]


# In[37]:


# string concatination
    adding 2 values or more
# to add 2 variable
a, b = 'Inno', 'Minds'
c = a+b
c


# In[8]:


# To add a space between them, add a " "
a = "Hello"
b = "world"
c = a + " " + b
## interger
print(c)
x = 5
y = 10
print(x + y)


# In[39]:


c *= 3
print(c)


# In[42]:


c*3


# In[9]:


c*3
c+c+c


# ## string Concatentaion 
# - adding 2 values or more
# 

# In[11]:


x = 'hi'
print(x+x)  # x+x
print(x*5)  # x+x+x+x+x


# In[ ]:




