# 👋 **Hand Tracking Application**

In this project, we developed a hand tracking application that allows users to control a box on the screen using their finger movements. The application tracks the position of the hand and allows interaction within a specified area.

## **🛠️ Requirements**

To run this project, you need to have the following libraries installed:

- **OpenCV** `cv2`
- **cvzone** `HandTrackingModule`

You can install the required libraries using the following commands:


**-> pip install opencv-python**

**-> pip install cvzone**


## **🚀 Usage**
Follow these steps to run the project:

-Camera: The application works by using your computer's camera. Make sure your camera is on.

-Hand Movements: When the distance between your index finger (landmark 8) and middle finger (landmark 12) is less than 30 pixels, a selection is made.

-Box Control: During selection, the box on the screen moves according to the position of your index finger. To move the box, bring your index finger over the box, then pinch your fingers together (bringing the distance below 30 pixels) to drag the box.

## **🔧 Ending the Application**
The application can be terminated by pressing the q key while it is running.

## **📄 License**
This project is licensed under the MIT License. For more information, please refer to the LICENSE file.

---
This *README.md* file will help users understand how to use your hand tracking application. If you need any further modifications or explanations, feel free to ask!

