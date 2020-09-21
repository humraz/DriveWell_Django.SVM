# Drive Well - Final Year Project

The goal of this project is to design and implement a background monitoring system as an android application in an android smart-phone to monitor and keep track of a driver’s status when they are traveling. The main provision that this project serves to give is to provide safety for both driver and any passengers, which has become especially important with the rise of “Uberification” form of taxi services.

##Technologies used
- The front end was built as an Android application using Android Studio and Java
- The back end for the application is built using Django and Python
- We used an SVM as the model to train and send back the predictions from the back end to the front end

##How it Works
- The android application takes images using the front camera(in the background) every seconds and then sends these images to the server from the app.
- The images are fed to the trained SVM model that predicts the class of the image(Whether the driver is sleeping, doesnt have a hand on the steering wheel, drinking while driving e.t.c)
- Once the trip is over the server calculates a score for the user based on the number of infarctions the driver has violated.
- This score is stored on the database for each driver registered in the system and used to determine which drivers are repeat offenders

This application can then be used to take action against drivers that are not following rules or not being as safe as possible during trips.

The web application also has a front end webpage to that allows admministrators to monitor the drivers scores and add, remove or blacklist drivers as needed providing full control to the administrators
