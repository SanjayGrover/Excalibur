'A ball has a mass of 10 Kg, suppose it travels at 100 m/s. Find the kinetic energy possessed by it? '
' A mass of 2 Kg is taken from the ground to the height of 10 m. Find the potential energy of the object? '
'A man climbs on to a wall that is 3.6 m high and gains 2268 J of potential energy. What is the mass of the man?'
'Suppose a 10 Kg was kept at 20 m height. Now, this block is dropped. Find out the final velocity of the block just before it hits the ground?'
'A bowling ball that has a weight of 2.2 Kg falls 50 m to the ground below. And find the ball’s gravitational potential energy when it reaches the bottom.'

import math
import time
def feedback():
    suggest=f"Enter your suggestion : {'\n'}{'\n'}"
    for i in range(len(suggest)):
        print(suggest[i],end='')
        time.sleep(0.0001)

def solve_energy():
    v=w=a=s=m=u=None
    result={}
    texts=f"Enter the question:{'\n'}"
    for i in range(len(texts)):
        print(texts[i],end='')
        time.sleep(0.01)
                         
    question=str(input())
    question=question.translate(question.maketrans("","","',?"))
    question=question.lower()  #Extracting the exact question
    question=question.split()
    for i in range(len(question)):
        if question[i]=='kg':
            m=float(question[i-1])
        if question[i]=='m/s':
            u=float(question[i-1])
            print(u)
        if question[i]=='dropped' or question[i]=='dropped.':
            u=0
            a=9.8
        if question[i]=='m':
           s=float(question[i-1])
        if question[i]=='j':
            w=question[i-1]
        if question[i]=='mass':
            m='exist'
        if question[i]=='final' and question[i+1]=='velocity':
            v='exist'
    if m is None:
       print("A body without mass is not defined")
    if m is not None and u is not None:
       result['Inital Kinetic Energy']=0.5*m*u*u
    if m is not None and s is not None and u is None:
        result['Potential energy']=m*9.8*s
    if w is not None and s is not None and m is not None:
        result['Mass']=w/(9.8*s)
    if m is not None and s is not None and u is not None and v is not None:
        string=f"Potential energy strored in ball when it is at a height of 20m=(mass of ball)*(accelration due to gravity)*(height).{"\n"}=10*9.8*20{"\n"}Now.as ball is dropped initaial velocity is zero.{"\n"}Kinetic energy is given by 0.5*mass*velocity*velocity{"\n"}Hence,initial kinetic energy will be zero and difference between initaial and final kinetic energy will be equal to potential energy.{"\n"}Let velocity of ball jus before it touches ground is 'v'.{"\n"}Final kinetic energy=0.5*v*v{"\n"}Now,0.5*v*v=10*9.8*20.{"\n"}Soving equation we get:"
        for i in range(len(string)):
            print(string[i],end='')
            time.sleep(0.01)
        result['Velocity just before obeject touches ground']=math.sqrt(u*u+2*9.8*s)
    return result
    
    
    
result=solve_energy()
print("The result is:",result)
feed=str(input("Was the answer correct? ")).strip().lower()
if feed=='yes':
   string1=f"Thank you for using our software!We hope to see you again."
   for i in range(len(string1)):
       print(string1[i],end='')
       time.sleep(0.01)
elif feed=='no':
   string1=f"PLease give your suggestion."
   for i in range(len(string1)):
       print(string1[i],end='')
       time.sleep(0.01)
   feedback()


