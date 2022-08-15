# Attendance_system
 
This repository contains code for facial recognition using openCV and python with a tkinter gui interface. If you want to test the code then run main.py or main_notebook.ipynb file

Technology used :
-openCV (Opensource Computer Vision)
-Python
-tkinter GUI interface
-MongoDB


Here I worked on Face Recognition Attendance System(FRAS) by using OpenCV(Python) and MongoDB. One can mark thier attendance by simply facing the camera. 

How it works :
When we run the main_notebook.ipynb file then a window pops up and asks for the admin username and password. After login correctly, a new window open and ask for Emp_Id, Emp_name, etc. After entering information then we have to click the Check button. if the id is not present in a database then and then only the Take_image button gets enabled until then the Take_image button is disabled. After clicking the Take_images button a window will pop up and it will capture some images (say 60) and images will get stored in the data folder. After clicking the Train_image button, it will create a Trainer.yml file and store it in the Trainer folder.
Now all initial setups are done. By running the Track_Image.ipynb file camera of the running machine is opened. If a face is recognised by the system then the Id and Name of the person is shown on Image, and the recognised person attendance will get marked on a database as soon as the running camera window will get close. And if the camera captures unknown faces or objects then those images will also get stored in the Unknown_Images folder.
For running Track_images file you can set timings so that it will run the specific function at the given time. 


Thank you
