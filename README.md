# MulltifacetedDigitRecognintion
The primary objective of this project is to develop an multifaceted digit recognition application that comprises individual applications to recognise numerical digits from 0-9 using speech and handwritten techniques with the help of Long Short Term Memory Network and Convolutional Neural Network respectively. To evaluate the accuracy of both the network models for all the digits from 0-9.

•	This is a novel method to integrate both recognition of spoken and handwritten digits in a single application.


•	Two different neural networks in a single application.



•	Higher accuracy than usual traditional methods.


•	Add on is an webcam integrated script to recognise handwritten digits through webcam


•	MFCC is simple compared to wavelet scattering and Linear Predictive Coding.


•	CNN used achieves higher accuracy with less dataset which means the network is well built.

The main file is samplefinal.py It executes tkinter window holding all three options of spoken, handwritten and webcam digit recognition.

To run main file,


1)clone the repository and download it


2)from the downloaded folder open cmd window


3)execute python samplefinal.py

To execute spoken digit recognition that uses LSTM,

python sound1.py

To execute handwritten digit recogniton that uses CNN,

python guifinal.py

To execute webcam digit recognition that uses CNN

python cam.py

Following are the dependencies of the project

1)tensorflow
2)numpy
3)keras
4)tflearn
5)pyttsx3
6)sounddevice
7)random
8)PIL
9)librosa
10)tkinter

I was completely new to deep learning and neural networks while starting this project but hours of learning helped me in mastering these skills.Keep learning!
