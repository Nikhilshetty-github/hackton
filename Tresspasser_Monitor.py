#!/usr/bin/env python
# coding: utf-8

# In[20]:


import smtplib
def alert_message(Message):
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)#456 is the send port number
        server.login("sender@gmail.com","password")# this line is used to login to the senders account
        server.sendmail("sender@gmail.com","receiver@gmail.com","message")
        server.quit()
        print("Message sent succesfully")
    except Exception as e:#try and except is used to handle the exception or error for ex if user changed the password
        print("Unsuccesfull",e)#except block catches that and prints that


# In[22]:


def buzzer(input):  # here we will connect the ports of input and output of buzzer
    if input != 0: # pid_output is taken as input to the buzzer
        print("Buzzer on!!")
    else:
        print("Buzzer off")


# In[28]:



import smtplib
pid_input = input("get info from pid")#here it reads the sensor input
pid_output = 0
if pid_input != 0:
    pid_output = pid_output + 1  # if the pids input is high the output is incremented
    if pid_output != 0 :
        alert_message(pid_output) #this will send the alert message to the user here message alert is done by calling a function
        buzzer(pid_output)#pid_output is given to the buzzer as input turning on and off of buzzer is done by calling a function

    else:
        pass
else:
    pass


# In[ ]:




