# Q1 Determine the gravitational force if two masses are 30 kg and 50 kg separated by a distance 4 m .
# Q2 A 50 kg astronaut stands on the surface of a earth , calculate the force experienced . 
# Q3 Determine the gravitational potential energy if two masses are 10 kg and 50 kg separated by a distance 4 m . 

import math
import time

def feedback():
    suggest=f"Enter your suggestion : {'\n'}{'\n'}"
    for i in range(len(suggest)):
        print(suggest[i],end='')
        time.sleep(0.02)
    data=str(input())
    #Here we will use SQL database to store the suggestion to resolve the issue further, and improve our program.


def solve_grav():
    s1=f"Enter all the values in SI Units m for metre , kg for kilogram and please maintain 1 space between value and unit and after unit{'\n'}"
    for i in range(len(s1)):
        print(s1[i],end='')
        
    question = str(input())
    question = question.translate(question.maketrans("", "", "',?"))
    question = question.lower()  # Extracting the exact question
    question = question.split()

    m = None
    me= 5.972*(10**24)
    G=6.67/(10**11)
    l=[]
    for i in range(0, len(question)):
        if question[i] == 'kg':
            m = float(question[i-1])
            l.append(m)        
    r=None        
    for i in range(0,len(question)):
         if question[i] == 'm':
            r = float(question[i-1])
    if(r==None):
        r=6.671*(10**6)
    m1=l[0]
    if len(l)==1:
        m2=me
    else:
        m2=l[1]
    F=(G*m1*m2)/(r*r)
    potentail=F*r
    print("The gravitational potential energy is\n",potentail)
    return F

result=solve_grav()
string_main=f"The Force is :{'\n'}{result} Newton {'\n'}"
for i in range(len(string_main)):
            time.sleep(0.02)
            print(string_main[i],end='')
feed_text=f"Was the answer correct : {'\n'}"
for i in range(len(feed_text)):
    time.sleep(0.02)
    print(feed_text[i],end='')
feed=str(input()).strip().lower()
if(feed=='yes'):
    feed_positive=f"Thanks for using our software! We hope to see you again.{'\n'}"
    for i in range(len(feed_positive)):
        print(feed_positive[i],end="")
        time.sleep(0.02)
elif(feed=='no'):
    feed_negative=f"Please Give us your feedback.{'\n'}"
    for i in range(len(feed_negative)):
        print(feed_negative[i],end='')
        time.sleep(0.02)
    feedback()          
