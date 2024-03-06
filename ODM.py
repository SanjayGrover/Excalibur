import math
import time
import mysql.connector


def feedback():
    suggest=f"Enter your suggestion : {'\n'}"
    for i in range(len(suggest)):
        print(suggest[i],end='')
        time.sleep(0.01)
    data=str(input())
    mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sirsa$1775",
    database="EXCALIBUR"
    )
    mycursor=mydb.cursor()
    string_feed="INSERT INTO FEEDBACK VALUES('user',%s)"
    mycursor.execute(string_feed,(data,))
    mydb.commit()
    mydb.close()
    #Here we will use SQL database to store the suggestion to resolve the issue further, and improve our program.
def solve_odm():
    u=v=a=t=s=u1=None
    result={}
    text=f"Enter the question : {'\n'}"
    for i in range(len(text)):
        print(text[i],end='')
        time.sleep(0.01)
    question=str(input())
    question=question.translate(question.maketrans("","","',.?"))
    question=question.lower()  #Extracting the exact question
    question=question.split()
    
    for i in range(len(question)):
        if question[i] == 'm/s' and (question[i-3] == 'initial' or question[i-4]=='initial'):
            u=float(question[i-1])
        elif question[i]=="rest":
            u=0
        if question[i]=='fall' or question[i]=='dropped' or question[i]=='drop':
            a=10
            u=0            # Setting up the variables
        elif question[i]=='m/s^2':
            a=float(question[i-1])
        if question[i]=='m/s' and (question[i-3] == 'final' or question[i-4] == 'final'):
            v=float(question[i-1])
        elif question[i]=="stop" or question[i]=="stops":
            v=0
        if question[i]=="upward":
            v=0
            a=-10
        if (question[i]=='s' or question[i]=='seconds'):
            t=float(question[i-1])
        if 'g' in question or 'g=10' in question:
            a=10 
        if "g=9.8" in question:
            a=9.8
        if question[i]=='m' or question[i]=='meters':
            s=float(question[i-1])
        if question[i]=='m/s' and (question[i-3] == 'constant' or question[i-4]=='constant'):
            v=float(question[i-1])
            u=float(question[i-1])
        if question[i]=='uniformly' and question[i-1]=='decelerates':
            u=float(question[i+2])
            v=float(question[i+5])
        if question[i]=='uniformly' and (question[i-1]=='accelerates' or question[i-1]=='up') and (question[i+3] == 'm/s'):
            u=float(question[i+2])
            v=float(question[i+5])
        if question[i]=='horizontally':
            u1=float(question[i+5])
            u=0
            a=10
    data_got=f"The values we got are : v={v}  u={u}  a={a}  t={t}  s={s}  {'\n'}"
    for i in range(len(data_got)):
        print(data_got[i],end='')
        time.sleep(0.01)
    if u is not None and v is not None and a is not None and t is None:
        # Calculate time using the first equation of motion: v = u + at
        string=f"Now we are having initial velocity={u}, final velocity={v}, and, acceleration={a}{'\n'}Using these, we can find the time.{'\n'}Using the first equation of motion.{'\n'}Time = (Final Velocity - Initial Velocity) / Acceleration{'\n'}Time = ({v}-{u})/{a}{'\n'}Hence we get Time = {(v-u)/a}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['time'] = (v - u) / a
    if u is not None and v is not None and a is None and t is not None:
        # Calculate acceleration using the second equation of motion: a = (v - u) / t
        result['acceleration'] = (v - u) / t
        string=f"Now we are having initial velocity={u}, final velocity={v}, and, Time={t}{'\n'}Using these, we can find the acceleration.{'\n'}Using the first equation of motion.{'\n'}Acceleration = (Final Velocity - Initial Velocity) / Time{'\n'}Acceleration = ({v}-{u})/{t}{'\n'}Hence we get Acceleration = {(v-u)/t}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
    if u is not None and a is not None and t is not None and s is None:
        # Calculate displacement using the third equation of motion: s = ut + (1/2)at^2
        string=f"Now we are having initial velocity={u}, acceleration={a}, time={t}{'\n'}Using these, we can find the distance. {'\n'}Using the second equation of motion.{'\n'}Displacement = (Initial Velocity)*Time + 0.5(Acceleration)*(Time)^2{'\n'}Displacement = {u} * {t} + 0.5 * {a} * {t} ^2{'\n'}Hence we get Displacement = {u*t+0.5*a*t**2}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['displacement'] = u*t+1/2*a*t**2                                          #finding the unknowns
    if v is not None and a is not None and t is not None and s is None:
        # Calculate displacement using the third equation of motion: s = vt - (1/2)at^2
        string=f"Now we are having final velocity={v}, acceleration={a}, time={t}{'\n'}Using these we can find the initial velocity and then using initial velocity, acceleration, and time we can find the Displacement of the body.{'\n'}Using the first equation of motion. Initial Velocity = Final Velocity - Acceleration * Time{'\n'}Initial Velocity = {v} - {a} * {t}{'\n'}Initial Velocity = {v-a*t}{'\n'}Now we need to calculate Displacement.{'\n'}Using Second Equation of motion.{'\n'} We get,{'\n'}Displacement = (Initial Velocity * Time) + 0.5 * Acceleration * (Time)^2{'\n'}Displacement = {u} * {t} + 0.5 * {a} * {t} ^2{'\n'}Displacement = {u*t + 0.5*a*t**2}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['displacement'] = v*t-1/2*a*t**2
    if u is not None and v is not None and t is not None and s is None:
        # Calculate displacement using the third equation of motion: s = (u + v) * t / 2
        string=f"Now we are having initial velocity = {u}, final velocity = {v}, Time = {t}{'\n'}Using these we can find displacement{'\n'}Using a combined form of First and Second Equation of motion we have : {'\n'}Displacement = (Final Velocity + Initial Velocity) * Time / 2{'\n'}So, Displacement = ({u} + {v}) * {t} / 2 {'\n'}Hence, Displacement = {(u+v)*t/2}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['displacement'] = (u + v) * t / 2
    if u is not None and v is not None and a is not None and s is None:
        # Calculate displacement using the third equation of motion: s = (v^2 - u^2) / (2 * a)
        string=f"Now we are having initial velocity = {u}, final velocity = {v}, Acceleration = {a}{'\n'}Using these we can find the Displacement.{"\n"}Using Third Equation of Motion we have : {'\n'}Displacement = ((Final Velocity)^2 - (Initial Velocity)^2) / (2 * Acceleration){'\n'}So Displacement = ({v}^2 - {u}^2) / (2 * {a}){'\n'}Hence, Displacement = {(v*v - u*u)/(2*a)}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['displacement'] = (v ** 2 - u ** 2) / (2 * a)
    if u is not None and a is not None and t is not None and v is None:
        # Calculate final velocity using the first equation of motion: v = u + at
        result['final_velocity'] = u + a * t
        string=f"Now we are given with initial velocity = {u}, Acceleration = {a}, Time = {t}{'\n'}Using these we can find the Final Velocity{'\n'}Using First Equation of Motion we have : {'\n'}Final Velocity = Initial Velocity + Acceleration * Time{'\n'}So Final Velocity = {u} + {a} * {t}{'\n'}Hence, Final Velocity = {(u+a*t)}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
    if v is not None and a is not None and t is not None and u is None:
        # Calculate initial velocity using the first equation of motion: u = v - at
        string=f"Now we are given with final velocity = {v}, acceleration = {a}, time = {t}{'\n'}Using these we can find the initial velocity.{'\n'}Using First Equation of Motion we have : {'\n'}Initial Velocity = Final Velocity - Acceleration * Time{'\n'}So Final Velocity = {v} - {a} * {t}{'\n'}Hence, Final Velocity = {v-a*t}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['initial_velocity'] = v - a * t
    if u is not None and v is not None and s is not None and a is None:
        # Calculate acceleration using the third equation of motion: a = (v^2 - u^2) / (2 * s)
        string=f"Now we are given with initial velocity = {u}, final velocity = {v}, displacement = {s}{'\n'}Using these we can find the acceleration.{'\n'}Using Third Equation of Motion we have : {'\n'}Acceleration = ((Final Velocity)^2 - (Initial Velocity)^2) / (2 * Displacement){'\n'}So Acceleration = ({v}^2 - {u}^2) / (2 * {s}){'\n'}Hence, Acceleration = {(v*v-u*u)/(2*a)}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['acceleration'] = (v ** 2 - u ** 2) / (2 * s)
    if s is not None and u is not None and a is not None and t is None:
        # Calculate time using the second equation of motion:
        string=f"Now we are given with Displacement = {s}, Initial Velocity = {u}, Acceleration = {a}{'\n'}Using these we can find the Time.{'\n'}Using Second Equation of Motion we have : {'\n'}Displacement = Initial Velocity * Time + Acceleration * (Time)^2{'\n'}So {s} = {u} * Time + 0.5 * {a} * (Time)^2{'\n'}Hence, Time = {(-2*u + math.sqrt(4*u*u + 8*a*s))/(2*a)}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['time'] = (-2*u + math.sqrt(4*u*u + 8*a*s))/(2*a)
    if s is not None and u is not None and a is not None and v is None:
        #Calculate final velocity using the third equation of motion :
        string=f"Now we are given with Displacement = {s}, Initial Velocity = {u}, Acceleration = {a}{'\n'}Using these we can find the Final Velocity.{'\n'}Using Third Equation of Motion we have : (Final Velocity)^2 + (Initial Velocity)^2 = 2 * Acceleration * Displacement{'\n'}So, Final Velocity = square_root({u}^2 + 2 * {a} * {s}){'\n'}Hence, Final Velocity = {math.sqrt(u*u + 2*a*s)}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['final_velocity'] = math.sqrt(u*u + 2*a*s)
    if s is not None and v is not None and a is not None and u is None:
        #Calculate initial velocity using the third equation of motion:
        string=f"Now we are given with Displacement = {s}, Final Velocity = {v}, Acceleration = {a}{'\n'}Using these we can find the Initial Velocity.{'\n'}Using Third Equation of Motion we have : (Final Velocity)^2 - (Initial Velocity)^2 = 2 * Acceleration * Displacement{'\n'}So, Initial Velocity = square_root({v}^2 - 2 * {a} * {s}){'\n'}Hence, Initial Velocity = {math.sqrt(v*v-2*a*s)}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['initial_velocity'] = math.sqrt(v*v-2*a*s)
    if u1 is not None:
        #Calculate horizontal distance:
        string=f"Now we have to find the horizontal distance travelled by the body,{'\n'}We are given with horizontal velocity = {u1}, and time of flight = {s/a}{'\n'}So the horizontal distance = {u} * {s/a}.{'\n'} Hence, we get, Horizontal Distance Travelled = {u*s/a}{'\n'}"
        for i in range(len(string)):
            time.sleep(0.01)
            print(string[i],end='')
        result['horizontal_distance']=u1*(s/a)
    # else:
    #     print("Insufficient data to solve the kinematics problem.")


#4th Equation of motion is not added till now...
    return result   # returning the answer as a dictionary.

result=solve_odm()
string_main=f"The result is :{'\n'}{result}{'\n'}"
for i in range(len(string_main)):
            time.sleep(0.01)
            print(string_main[i],end='')
feed_text=f"Was the answer correct : {'\n'}"
for i in range(len(feed_text)):
    time.sleep(0.01)
    print(feed_text[i],end='')
feed=str(input()).strip().lower()
if(feed=='yes'):
    feed_positive=f"Thanks for using our software! We hope to see you again.{'\n'}"
    for i in range(len(feed_positive)):
        print(feed_positive[i],end="")
        time.sleep(0.01)
elif(feed=='no'):
    feed_negative=f"Please Give us your feedback.{'\n'}"
    for i in range(len(feed_negative)):
        print(feed_negative[i],end='')
        time.sleep(0.01)
    feedback()