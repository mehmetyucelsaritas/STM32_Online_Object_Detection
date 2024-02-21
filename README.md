# STM32 Object (Agricultural Herb) Detection and Tracking Project

## Overview
In agricultural fields, efficient detection and removal of agricultural herbs can significantly increase yield. This STM32 project aims to provide a mechanism to detect and track agricultural herbs, represented by green objects, in an agricultural field. The project utilizes STM32 microcontroller, servo motors, cameras, and other electronic devices to achieve this goal. Here you can [watch the video representation of project.](https://youtu.be/UNbD-ZfWUSE) 

## General Preliminary Design
**The project consists of two main sections:**
1. Image Processing: In this section, the position of the herb is detected using a camera connected to a computer. The coordinates of the herb(object) are then sent to the STM32 microcontroller via communication protocols.
2. Data Handling and Actuation: The STM32 microcontroller receives the coordinates of the herb and directs servo motors to point a laser at the herb's location. Additionally, the coordinates are displayed on an LCD screen.

## Concepts and Sensors Utilized
- Pooling
- Interrupts
- USART and I2C Communication Protocols
- PWM (Pulse Width Modulation)
- STM32 Libraries
- LCD Display
- Red Laser
- Servo Motors
- Pan Tilt Kit
- 3D printed Mount

## Section 1: Image Capture and Processing Pipeline
- Object to Be Tracked: Physical objects in the camera frame initiate the tracking process.
- Camera: Captures images of the herb online, serving as the main sensor input.
- Computer CPU: Processes the digital image using Python and OpenCV.
- Python Image Processing: Analyzes the image to detect the object and obtain its coordinates.
- Coordinates of Object: Resulting coordinates of the object within the frame are used for tracking.

## Section 2: Data Handling and Actuation Pipeline
- Serial Protocol: Coordinates are communicated to the STM32 microcontroller via USART.
- STM32 and C Programming: Coordinates received by the microcontroller are processed and servo motors are controlled accordingly.
- I2C Protocol: Coordinates are displayed on an LCD screen connected to the STM32.
- Pan Tilt Servo Driving and Data Conversion: Servo motors adjust their angles to point the laser at the herb's location.
- Laser: Provides a visual indication of the herb's position.
