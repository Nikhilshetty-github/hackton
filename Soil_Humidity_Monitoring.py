#!/usr/bin/env python
# coding: utf-8

# In[15]:


def start_watering(input_w):
    if input_w:
        print("Motor start\'s and start watering")
    else:
        pass


# In[16]:


import smtplib
sensor_input = float(input("getting information from sensor in % "))
if sensor_input <= 45:
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)#456 is the send port number
        server.login("sender@gmail.com","password")# this line is used to login to the senders account
        server.sendmail("sender@gmail.com","receiver@gmail.com","message")
        server.quit()
        print("Humidity is in control")
    except Exception as e:#try and except is used to handle the exception or error for ex if user changed the password
        print("Unsuccesfull",e)#except block catches that and prints that
else:
    start_watering(sensor_input)
    print("Humidity was High and watering is done")


# In[ ]:




