## Inspiration
Being in a college dorm is hard. There are often random people who come through the door is often challenging to know who exactly is at your door. Current systems such as 'Ring' have the ability to see the real-time camera feed of your door, however, these types of systems **come with many drawbacks.** Primarily, you have to pull up an app and wait for your app feed to load for around 20 seconds, which could be too long in many cases. Plus if that person left, or is not visible in the camera anymore, you don't have an instant idea of who was at the door if they are not in the live feed anymore and you have to go back into the footage, **taking around 1-2 minutes**. These 1-2 minutes could be crucial in emergency situations. And from a college student's perspective, a 'Ring' type system is too expensive and difficult to mount to a dorm room door.

## What it does
FaceSafe is an advanced facial recognition system designed for use in college dormitories. The system utilizes neural network processing to run a sophisticated face detection algorithm that can detect and identify individuals who approach the dormitory entrance. The algorithm is based on a pre-existing set of known faces, which can be easily expanded upon to provide a more comprehensive security solution.
When an individual is detected, the system sends an email notification to the authorized personnel and **displays the individual's name, picture, and time of entry on the mobile application**. In the event that an unknown face is detected, the system will notify authorized personnel of an unknown individual approaching the dormitory entrance. The system is designed to provide a secure, convenient and efficient way of identifying individuals entering and exiting dormitories, ensuring safety and security for students and staff.

## How we built it
The system is composed of three main components: face detection, cloud communication, and the user interface.

Face Detection: The face detection component of the system utilizes the OpenCV library for capturing images and videos from a camera, Adam Geitgey's face_detection API for the neural network architecture. The system was trained using a dataset of faces, all implemented in Python. The face detection algorithm is based on the Single Shot MultiBox Detector (SSD) which is a deep learning-based object detection algorithm that is able to detect faces in real-time. This algorithm makes use of a convolutional neural network (CNN) to extract features from the image, and a MultiBox layer to predict bounding boxes and class labels at different scales. The SSD network was trained on the WIDER FACE dataset which consists of 32,203 images and 393,703 faces of different scales, poses, and occlusions.

The face detection process starts with capturing an image or video frame from a camera. The captured image is then passed through the SSD network which outputs the bounding boxes and class labels of the detected faces. The bounding boxes are then used to crop the face region from the image, which is then passed through a face alignment process to normalize the face for further processing.

Face Recognition: Once face detection is done, the next step is to recognize the detected face. The system uses a deep learning-based face recognition algorithm, which is based on the FaceNet architecture. The FaceNet architecture is a one-shot learning algorithm that uses a deep neural network to map a face to a 128-dimensional embedding vector. The embedding vector is a compact representation of the face that captures its unique characteristics of the face. The system was trained on a dataset of faces, and the embedding vectors of the known faces were stored in a database. When a new face is detected, its embedding vector is calculated and compared to the embedding vectors in the database to find the closest match.

Cloud Communication: The detection results are then communicated to a cloud server using Google Cloud Platform's Firebase Firestore, which is a serverless NoSQL document database that stores and retrieves data with low latency. The data of the detected face, including the individual's name, picture, and time of entry is then stored and retrieved on the client side using the mobile app. This allows authorized personnel to have real-time updates on who is entering and exiting the dormitory.

User Interface: The system includes a user interface which is a mobile application that was developed using Java (for the backend) and XML (for the front end). The app uses the Google Cloud Platform's Firebase Realtime Database to collect the data that was pushed from the python script. The app also uses the Java Time API to get the current time and to display the time of the entry of the individual. When there is a change in the database, the app is triggered, sends a notification email, and displays the individual's face, time of entry, and name on the app. This allows authorized personnel to quickly and easily identify and respond to individuals entering the dormitory.

## Challenges we ran into
One of the main challenges we encountered during the development of FaceSafe was creating a wireless solution for the system. Our initial plan was to use a Raspberry Pi as the primary device for the system, which would be placed at the door and would be able to stream the webcam footage to an external computer for processing. However, we quickly ran into issues with the Raspberry Pi's limited processing power. The model we were using was from 2014, which proved to be insufficient for running the necessary neural network architecture for the face detection component of the system. Despite our efforts to optimize the code and streamline the process, we were unable to achieve the desired level of performance. As a result, we had to revert to a wired solution for the system, which required the use of a more powerful computer for the face detection component. This added an additional layer of complexity to the system but ultimately resulted in a more robust and reliable solution.

## Accomplishments that we're proud of
One of the accomplishments that we're particularly proud of with FaceSafe is the successful integration of multiple technologies to create a cohesive and functional system. The combination of the face detection component, which utilized the OpenCV library and Adam Geitgey's face_detection API, the cloud-based data storage and retrieval using Google Cloud Platform's Firebase Firestore, and the user interface for the mobile app, which was developed using java and XML, required a significant amount of coordination and planning to bring together.

We're also proud of the high level of accuracy that we were able to achieve with the face detection component of the system. The ability to accurately detect and identify individuals in real-time even in challenging lighting conditions was a significant achievement.

Additionally, we're proud of the ease of use and intuitive design of the mobile app, which allows users to easily view and manage the detected individuals and their corresponding information, including the name, picture, and time of detection.

Overall, we're proud of the successful creation of a functional and effective face detection system that can be used for a variety of applications, including college dorms and other secure environments.

## What we learned
During the development of FaceSafe, we learned a great deal about various technologies and techniques that are essential for building an effective face detection system. One of the key things we learned was the importance of selecting the right tool for the task. We experimented with multiple face detection libraries and found that using Adam Geitgey's face_detection API was the best suited for our needs, it provided the highest level of accuracy and it didn't require us to train the neural network from scratch.

We also learned the importance of proper data management and storage, especially in a cloud-based environment. We had to learn the intricacies of Google Cloud Platform's Firebase Firestore, which allowed us to store and retrieve data quickly and efficiently.

Another important aspect we learned was the importance of designing and developing a user-friendly interface that is intuitive and easy to use. We learned how to create a visually appealing, functional, and responsive mobile app using java and XML, and how to use JavaTime API to show the time based on the system clock.

Lastly, we learned about the importance of testing and optimizing the system for performance, especially when using resource-constrained devices like Raspberry Pi. We learned that a wired solution is more reliable and efficient than a wireless one in cases where the device has limited processing power.

## What's next for FaceSafe
The development of FaceSafe is an ongoing process, and there are several areas where we plan to make improvements and add new features. Some of the things we have planned for the future of FaceSafe include:

1. Improving the accuracy of the face detection algorithm: We plan to continue training the face detection algorithm with a larger and more diverse dataset to improve its accuracy and robustness.

2. Adding more security features: We plan to integrate additional security features like facial recognition, multi-factor authentication, and security cameras to make the system more secure and reliable.

3. Expanding the system's capabilities: We plan to add new features like motion detection, visitor management, and access control to make the system more versatile and useful for a wider range of applications.

4. Improving the mobile app: We plan to make the app more user-friendly and efficient by adding features like push notifications, real-time updates, and a more intuitive user interface.

5. Making the system wireless: We will try again to make the system wireless using more advanced hardware and software that can handle the processing of the data and use the raspberry pi as a wireless gateway.

6. Integrating with other systems: We plan to integrate the system with other systems like smart home devices and security cameras to create a more comprehensive security solution.

7. Overall, we believe that FaceSafe has a lot of potential and we are excited to continue working on it to make it even better and more useful for our target audience.
