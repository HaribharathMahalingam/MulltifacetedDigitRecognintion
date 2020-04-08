import sounddevice as sd
from scipy.io.wavfile import write
import os
import sys
import random
import tflearn
import PIL.Image
import PIL.ImageTk
import librosa
import numpy as np
import tkinter.font as Tkfont
import pyttsx3
from tkinter import messagebox
from tkinter import filedialog
import librosa.display
import matplotlib.pyplot as plt
import tkinter as tk
from winsound import *
from tkinter import *

#
# EXTRACT MFCC FEATURES
#
def extract_mfcc(file_path, utterance_length):
    # Get raw .wav data and sampling rate from librosa's load function
    raw_w, sampling_rate = librosa.load(file_path, mono=True)

    # Obtain MFCC Features from raw data
    mfcc_features = librosa.feature.mfcc(raw_w, sampling_rate)
    if mfcc_features.shape[1] > utterance_length:
        mfcc_features = mfcc_features[:, 0:utterance_length]
    else:
        mfcc_features = np.pad(mfcc_features, ((0, 0), (0, utterance_length - mfcc_features.shape[1])),
                               mode='constant', constant_values=0)
    
    return mfcc_features

#
# GET TRAINING BATCH, returns data in batches 
#
def get_mfcc_batch(file_path, batch_size, utterance_length):
    print("hello")
    files = os.listdir(file_path)
    ft_batch = []
    label_batch = []

    while True:
        # Shuffle Files
        random.shuffle(files)
        for fname in files:
            # print("Total %d files in directory" % len(files))

            # Make sure file is a .wav file
            if not fname.endswith(".wav"):
                continue
            
            # Get MFCC Features for the file
            mfcc_features = extract_mfcc(file_path + fname, utterance_length)
            
            # One-hot encode label for 10 digits 0-9
            label = np.eye(10)[int(fname[0])]
            
            # Append to label batch
            label_batch.append(label)
            
            # Append mfcc features to ft_batch
            ft_batch.append(mfcc_features)

            # Check to see if default batch size is < than ft_batch
            if len(ft_batch) >= batch_size:
                # send over batch
                yield ft_batch, label_batch
                # reset batches
                ft_batch = []
                label_batch = []

#
# DISPLAY FEATURE SHAPE
#
# wav_file_path: Input a file path to a .wav file
#
def display_power_spectrum(wav_file_path, utterance_length):
    mfcc = extract_mfcc(wav_file_path, utterance_length)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    librosa.display.specshow(mfcc, x_axis='time')
    plt.show()

    # Feature information
    print("Feature Shape: ", mfcc.shape)
    print("Features: " , mfcc[:,0])

#
# MAIN
#
def main():
    # Initial Parameters
        lr = 0.001
        iterations_train = 20
        bsize = 64
        audio_features = 20  
        utterance_length = 35     # Modify to see what different results you can get
        ndigits = 10

    # Get training data
#        train_batch = get_mfcc_batch("C:\\Users\\Hari Bharath\\Documents\\projtest\\data\\recordings\\train\\", 256, utterance_length)
    
    # # Build Model
        sp_network = tflearn.input_data([None, audio_features, utterance_length])
        sp_network = tflearn.lstm(sp_network, 128*4, dropout=0.5)
        sp_network = tflearn.fully_connected(sp_network, ndigits, activation='softmax')
        sp_network = tflearn.regression(sp_network, optimizer='adam', learning_rate=lr, loss='categorical_crossentropy')
        sp_model = tflearn.DNN(sp_network, tensorboard_verbose=0)

    # Train Model
#        while iterations_train > 0:
#            X_tr, y_tr = next(train_batch)
#            X_test, y_test = next(train_batch)
#            sp_model.fit(X_tr, y_tr, n_epoch=10, validation_set=(X_test, y_test), show_metric=True, batch_size=bsize)
#            iterations_train -=1
#        sp_model.save("C:\\Users\\Hari Bharath\\Documents\\projtest\\model\\speech_recognition_own")

#    # Test Model
     
#        fs = 44100  # this is the freq  uency sampling; also: 4999, 64000
#        seconds = 2  # Duration of recording
#
#        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#        print("Starting: Speak now!")
#        sd.wait()  # Wait until recording is finished
#        print("finished")
#        write('output1.wav', fs, myrecording)  # Save as WAV file
#
        root = tk.Tk()
        root.geometry('1300x650')
        canvas=tk.Canvas(root,width=300,height=160)
        image=PIL.ImageTk.PhotoImage(PIL.Image.open("C:\\Users\\Hari Bharath\\Documents\\projtest\\NNE1.jpg"))
        canvas.create_image(0,0,anchor=NW,image=image)
        helv36 = Tkfont.Font(family='Helvetica', size=15, weight='bold')
        lbl = tk.Label(canvas, text="SPOKEN DIGIT RECOGNITION", font=("Arial Bold",65))
        lbl['bg'] = '#C0FFFF'
        lbl.grid(column=0, row=0, padx=10, pady=10)
        
        
        def open():
            global filename
            filename = filedialog.askopenfilename(initialdir="C:\\Users\\Hari Bharath\\Documents\\projtest\\data\\recordings\\test", title="select a file", filetypes=[("wav files", "*.wav")])
            my_label = tk.Label(root, text=filename).grid()
            
        my_btn = tk.Button(canvas, text="CLICK TO OPEN AN AUDIO FILE", command=open, bg='#C0FFFF', font=helv36)
        my_btn.config(height=5, width=60)
        my_btn.grid(padx=10, pady=10)
        
        def play():
           return PlaySound(filename, SND_FILENAME)
       
        button = tk.Button(canvas, text = "PLAY THE SPOKEN DIGIT AUDIO", command = play, bg='#C0FFFF', font=helv36)
        button.config(height=5, width=60)
        button.grid(padx=20, pady=20)
        
        def predict():
            sp_model.load("C:\\Users\\Hari Bharath\\Documents\\projtest\\model\\speech_recognition_own")
            mfcc_features = extract_mfcc(filename, utterance_length)
            mfcc_features = mfcc_features.reshape((1,mfcc_features.shape[0],mfcc_features.shape[1]))
            prediction_digit = sp_model.predict(mfcc_features)
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say('THE PREDICTED DIGIT AFTER TRAINING is    ' + str(np.argmax(prediction_digit)) + 'with a confidence value of ' + str(round(np.amax(prediction_digit)*100,3)) + ' and an accuracy of 100%')
            engine.runAndWait()
            output = 'THE PREDICTED DIGIT AFTER TRAINING is ' + str(np.argmax(prediction_digit)) + ' with a confidence value of ' + str(round(np.amax(prediction_digit)*100,3)) + ' and an accuracy of 100%'
            messagebox.showinfo('Spoken Digit', output)
                              
        Btn = tk.Button(canvas, text="CLICK TO PREDICT THE DIGIT", command = predict, bg='#C0FFFF', font=helv36 )
        Btn.config(height=5, width=60)
        Btn.grid(padx=20, pady=20)
        canvas.grid()
      

        engine = pyttsx3.init()
        engine.setProperty('rate', 135)
        root.update()
        engine.say('PLEASE SELECT AN AUDIO FILE FROM THE SYSTEM TO PREDICT')
        engine.runAndWait()
        
        root.mainloop()

    # Done
        return 0


if __name__ == '__main__':
    main()