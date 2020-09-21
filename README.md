# Drive Well - Final Year Project

The goal of this project is to design and implement a background monitoring system as an android application in an android smart-phone to monitor and keep track of a driver’s status when they are traveling. The main provision that this project serves to give is to provide safety for both driver and any passengers, which has become especially important with the rise of “Uberification” form of taxi services.

## Technologies used
- The front end was built as an Android application using Android Studio and Java
- The back end for the application is built using Django and Python
- We used an SVM as the model to train and send back the predictions from the back end to the front end

## How it Works

The project focuses on developing an android application that monitors the movement of the vehicle driver and detects anomalies in their driving. All anomalies are detected and classified into different categories during a trip and then a score is assigned to the driver, which is then sent from the android phone to a web server. This process is commonly referred to as action recognition. Scores of all drivers in the system are presented on said server for evaluation by the administrative staff of the online taxi services.This score evaluation provides an easy basis for online taxi services to judge quality of drivers.

- The android application takes images using the front camera(in the background) every seconds and then sends these images to the server from the app.
- The images are sent to the server for initial preprocessing on the images are (Image Scaling, Feature Extraction e.t.c)and then fed to the trained SVM model that predicts the class of the image(Whether the driver is sleeping, doesnt have a hand on the steering wheel, drinking while driving e.t.c)
- Once the trip is over the server calculates a score for the user based on the number of infarctions the driver has violated.
- This score is stored on the database for each driver registered in the system and used to determine which drivers are repeat offenders

This application can then be used to track and take action against drivers that are not following set rules and not being as safe as possible during trips.
