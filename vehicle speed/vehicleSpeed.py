# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import os
import time

cascase_src = "cars.xml"
video_src = "Cars - 1900.mp4"

# Corrdinate First Line A
ax1 = 200
ay = 250
ax2 = 600

# Corrdinate Seconed Line B
bx1 = 450
by = 600
bx2 = 1300

# Calculate Speed = distance(km) / time(s)
def CalculateSpeed(time):
    
    try:
        speed = (9.144/1000)/(time/3600)
        return speed
    except ZeroDivisionError:
        print("You Can't dived by zero")


# Cars Number
i = 1
start_time = time.time()

# Read Video ----

cap = cv2.VideoCapture(video_src)

car_cascad = cv2.CascadeClassifier(cascase_src)

while True :
        
    ret,img = cap.read()
    
    
        
    if(type(img)==type(None)):
        break
    
    # Somoothing And Imporoving 
    
    blurred = cv2.blur(img , ksize=(15,15))
    gray = cv2.cvtColor(blurred , cv2.COLOR_BGR2RGB)
    
    # Get Coordinate For Cars and Store it in cars
    cars = car_cascad.detectMultiScale(gray , 1.1 , 2)
    
    # Draw First and Seconed Line by the Coordinate
    #Line A
    cv2.line(img , (ax1,ay) , (ax2,ay) , (255,0,0) , 2 )
    #Line B
    cv2.line(img , (bx1,by) , (bx2,by) , (255,0,0) , 2 )

    # Get Coordinate and draw it in rectangle
    for (x,y,w,h) in cars:
        
        # Recatngle in Cars
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,0,255) , 2)
        
        # Boint in center car
        cv2.circle(img , ( int( (x+x+w)/2) , int( (h+y+y)/2) ) , 4 , (0,255,0) , -1)        
    
        # ay == Y Hight Claculate new time untile be Start time at the first Line
        while int(ay) == int((y+y+h)/2):
            cv2.line(img , (ax1,ay) , (ax2,ay) , (0,255,0) , 2 )
            start_time = time.time()
            break
        
        while int(ay) <= int((y+y+h)/2):
            
           # if int(by) <= int((y+y+h)/2) & int(by+10) >= int((y+y+h)/2):
            
                cv2.line(img , (bx1,by) , (bx2,by) , (0,255,0) , 2 )
                speed = CalculateSpeed(time.time() - start_time)
                
                print("Car number " + str(i) + "Is Running by " + str(speed) + "Km/H")
                i = i + 1
                break
            #else:
             #   cv2.putText(img, "Saved", (100, 250),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0) , 3)
                
              #  break
        
    cv2.imshow("Video" , img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
        
        

        
        
            

















