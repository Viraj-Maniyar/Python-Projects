from time import *
import random as r

def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
        except:
            error +=1
    return error
     # Generate a random test case with length n.

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)



test =["Its never good to give them details, Janice told her sister."," Always be a little vague and keep them guessing. Her sister listened intently and nodded in agreement."," She didn't fully understand what her sister was saying but that didnt matter.","She loved her so much that she would have agreed to whatever came out of her mouth.","Sometimes its the first moment of the day that catches you off guard.","Thats what Wendy was thinking. She opened her window to see fire engines screeching down the street.","While this wasnt something completely unheard of, it also wasnt normal.","It was a sure sign of what was going to happen that day.","She could feel it in her bones and it wasnt the way she wanted the day to begin.","All he could think about was how it would all end.","There was still a bit of uncertainty in the equation, but the basics were there for anyone to see."]

test1 = r.choice(test)
print("*****Typing Speed Calculator*****")
print(test1)
print()
print()

time_1= time()
testinput = input(" Enter : ")
time_2= time()

print ('speed : ',speed_time(time_1,time_2,testinput),"w/sec")
print("Error :",mistake(test1,testinput))