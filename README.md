# 🌍 AI Voice Translator

A real-time desktop application that translates live conversations between two people speaking different languages.

The application captures speech, converts it to text, optionally refines incomplete spoken sentences using an LLM, translates the text, generates natural speech, and plays the translated audio in real time.

Designed for online meetings, voice calls, interviews, and multilingual conversations.

---

## ✨ Features

* 🎙️ Real-time voice translation
* 🌐 Two-way conversation support
* 🤖 Optional LLM-based speech cleanup
* 🔊 Natural AI voices using Microsoft Edge TTS
* ⚡ Low-latency processing pipeline
* 🖥️ Simple desktop interface
* 🔄 Works with communication platforms that support custom microphone and speaker devices

---

## 🛠️ Technology Stack

* Python 3.12.7
* Whisper Speech-to-Text
* Groq API (LLM Speech Cleanup)
* Google Translate
* Microsoft Edge TTS
* VB-Audio Virtual Cable
* CustomTkinter

---

## 📁 Project Structure

```text
VoiceTranslator/
│
├── src/
├── docs/
├── audio/
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

Clone the repository:

```bash
git clone <repository-url>
cd VoiceTranslator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
python src/main.py
```

---

## 📚 Documentation

Complete documentation is available in the `docs` folder.

* 01_installation.md — Complete installation guide
* 02_audio_setup.md — Windows, VB Cable, and meeting software configuration
* 03_user_guide.md — Using the application
* 04_architecture.md — Internal system design
* 05_developer_guide.md — Project structure and development
* 06_troubleshooting.md — Common issues and solutions
* 07_faq.md — Frequently asked questions

---

## 📷 Screenshots

Add the following images after creating them:

* Main application interface
* Live translation example
* System architecture diagram

---

## 💡 Supported Use Cases

* International meetings
* Online interviews
* Remote collaboration
* Language learning
* Customer support
* Cross-language communication

---

## 📄 License

This project is intended for educational and research purposes unless otherwise specified.

---

## 👨‍💻 Author

Developed by **Momina**

Software Engineering Student

Passionate about building practical software solutions using AI and automation.
