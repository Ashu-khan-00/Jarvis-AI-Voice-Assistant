# Jarvis-AI-Voice-Assistant
A Python AI assistant that wakes on “Jarvis” and handles the rest.

# 🤖 Jarvis – AI Voice Assistant (Python)
Jarvis is a Python-based **AI voice assistant** that listens for a wake word, understands spoken commands, performs tasks like opening websites, playing music, fetching news, and answering questions using **OpenAI**.
It works hands-free using speech recognition and text-to-speech.

## ✨ Features
* 🎙️ **Wake word detection** – activates when you say **“Jarvis”**
* 🗣️ **Speech-to-Text** using Google Speech Recognition
* 🔊 **Text-to-Speech** using `pyttsx3`
* 🌐 Open popular websites:
  * Google
  * YouTube
  * Facebook
  * LinkedIn
* 🎵 **Music playback** using a custom music library
* 📰 **Live News Headlines** (Sports, Tech, Business, Health, etc.)
* 🤖 **AI-powered responses** using OpenAI (GPT model)
* ⚡ Fast and lightweight command processing

## 🧠 How Jarvis Works
1. Jarvis listens continuously in the background
2. When it hears **“Jarvis”**, it replies **“Ya”**
3. It then listens for your command
4. Based on your command, it:
   * Opens websites
   * Plays music
   * Reads news
   * Or asks OpenAI for intelligent responses
   * 
## 🛠️ Tech Stack
* Python 3
* `speech_recognition`
* `pyttsx3`
* `requests`
* `webbrowser`
* **OpenAI API**
* **NewsAPI**

---

## 📂 Project Structure

```
Jarvis-AI/
│
├── jarvis.py              # Main assistant script
├── musicLibrary.py        # Custom music dictionary
├── README.md              # Project documentation
└── requirements.txt       # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `requirements.txt`

```txt
speechrecognition
pyttsx3
requests
openai
pyaudio
```

> ⚠️ **Note:**
> If `pyaudio` fails to install on Windows, download the `.whl` file from
> [https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

---

## 🔑 API Keys Setup

### 🔹 OpenAI API Key

Replace this line:

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

👉 **Never expose your API key in public repositories**

Use environment variables instead:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

### 🔹 NewsAPI Key

Get a free key from: [https://newsapi.org](https://newsapi.org)
Replace:

```python
newsapi = "YOUR_NEWS_API_KEY"
```

---

## ▶️ Run the Project

```bash
python jarvis.py
```

You’ll hear:

```
Initializing Jarvis.
```

Say:

```
Jarvis
```

Jarvis replies:

```
Ya
```

Now give your command 🎙️

---

## 🗣️ Example Commands

* **“Open Google”**
* **“Play believer”**
* **“Tech news”**
* **“Sports news”**
* **“Who is Elon Musk?”**
* **“Explain quantum computing”**

---

## 🚀 Future Improvements

* 🔒 Secure API key management
* 📱 GUI / Desktop App
* 🌍 Multilingual support
* 🧠 Memory-based conversations
* 📅 Calendar & reminders
* 🏠 Smart home integration

---

## 🧑‍💻 Author

**Mohd Ashraf Khan**
Aspiring Software Engineer | AI & Python Enthusiast

If you like this project, don’t forget to ⭐ the repo!

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.



