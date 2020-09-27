#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tclab
import time
def temp_info():
    temp_in = int(input("getting info from sensor"))#this can be done by connecting input and output of sensor to port
    temp_out = 0
    if temp_in != 0:
        temp_out = temp_out + temp_in
        print("Current Temperature is :",temp_out)
        if temp_out >= 35:
            print("temperature is high")
        elif temp_out <= 35 and temp_out >= 29:
            print("Modarate Temperature")
        elif temp_out <= 29 and temp_out >=21:
            print("cold")
        else:
            print("too cold")
    else:
        pass


# In[2]:


import datetime
def rain_info():
    rain_input = int(input("getting information from sensor"))
    rain_output = 0
    now = datetime.datetime.now()
    if rain_input != 0:
        rain_output = rain_output + rain_input
        print("Its raining from ",now.strftime("%H:%M:%S"))
    else:
        pass


# In[6]:


rain_information = "y"
temp_information = "y"
rain_information = input("Do you want to know the current rain information y or n ")
while rain_information.lower() != "n":
    rain_info() 
    break
else:
    rain_information = "n"
    
temp_information = input("Do you want to know the current temperature y or n ")
while temp_information.lower() != "n":
    temp_info()
    break
else:
    temp_information = "n"


# In[ ]:




