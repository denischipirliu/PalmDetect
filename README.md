# ✋ Palm Detect - Gesture-Controlled LED System 💡

## 🔥 Introduction  
Ever wished you could control things with just a wave of your hand? Well, now you can! 🎉 **Palm Detect** is a futuristic project that lets you **control LEDs using hand gestures**—no buttons, no switches, just pure **gesture magic**! 🪄✨  

With the power of **computer vision** and **machine learning**, this system detects your hand movements and translates them into real-time **LED brightness and count adjustments**. 🤯  

---

## 🌟 Features  
✅ **Real-time hand tracking** using `mediapipe` and `OpenCV` 🖐️  
✅ **Adjust LED brightness** by moving fingers closer or further apart 🌡️  
✅ **Control the number of active LEDs** by raising fingers 🫏  
✅ **Seamless Python-Arduino integration** with `pyfirmata` 🔄  
✅ **Instant response**—zero noticeable delay ⚡  

---

## 🛠️ What You Need  

### 🏰️ Hardware:  
🔹 **Arduino Board** (e.g., Uno)  
🔹 **LEDs** (up to 5)  
🔹 **USB cable**  
🔹 **Resistors & jumper wires**  

### 💻 Software:  
🟢 **Python 3**  
🟢 **OpenCV** (`pip install opencv-python`)  
🟢 **Mediapipe** (`pip install mediapipe`)  
🟢 **PyFirmata** (`pip install pyfirmata`)  

---

## 🚀 How It Works  
🔹 **Wave your hand!** The webcam captures your gestures in real-time.  
🔹 **Left hand = Brightness control** 🌟 (move fingers apart for more light, closer for dimming).  
🔹 **Right hand = LED count** 🔢 (raise fingers to turn on more LEDs).  
🔹 **Python talks to Arduino**, making the magic happen! ✨  

---

## 🎯 Setup & Installation  

### 1⃣ Install Dependencies  
```bash
pip install opencv-python mediapipe pyfirmata
```

### 2⃣ Upload Firmata to Arduino  
1. Open **Arduino IDE**  
2. Go to **File > Examples > Firmata > StandardFirmata**  
3. Upload it to your **Arduino board**  

### 3⃣ Run the Palm Detect Script! 🏃‍♂️  
```bash
python main.py
```

### 4⃣ Extra Step (Important! ⚠️)  
Before running the script, make sure to **close the Arduino IDE**.  
> If the Arduino IDE is open, it **might block access to the COM port**, causing the script to fail.  

---

## 🎮 How to Use  
✅ **Raise fingers on your right hand** to control **the number of LEDs**.  
✅ **Move your left-hand fingers closer/further** to adjust **brightness**.  
✅ **Press ‘Q’ to exit** the program.  

🔄 **The system updates LEDs in real-time—no noticeable delay!**  

---

## ✍️ Author 
🚀 **Denis Chipirliu**  
  
---
 
