# 🧠 AI Audio Assistant (STT & TTS with API)

This project is a smart voice assistant based on **Speech-to-Text (STT)** and **Text-to-Speech (TTS)** powered by AI APIs including OpenAI, DeepSeek, and Ollama.

---

## 🎯 Features

- 🎙️ Convert user speech to text (STT)
- 🧠 Answer questions using various AI APIs
- 🗣️ Convert AI responses to voice and play them (TTS)
- 🔄 Supports multi-turn conversations
- 🧪 Connects to various models (ChatGPT, DeepSeek, LLaMA 3)

---

## 📁 File Structure

| File | Description |
|------|-------------|
| `assist_chatgpt.py` | Uses OpenAI Assistant API for answering and generating speech |
| `assist_deepseek.py` | Connects to DeepSeek model via Ollama |
| `assist_ollama.py` | Connects to LLaMA 3 model via Ollama |
| `jarvis_chatgpt.py` | Main STT + TTS interface for ChatGPT |
| `jarvis_deepseek.py` | Main STT + TTS interface for DeepSeek |
| `jarvis_ollama.py` | Main STT + TTS interface for Ollama |

---

## ⚙️ Requirements

Install required libraries using:

```bash
pip install openai pygame ollama googlesearch-python
```

Make sure `RealtimeSTT` and `Silero` are set up properly for speech recognition.

---

## 🚀 How to Run

1. (Optional) Create `tools_*.py` files to manage smart device commands or extra features.
2. Run one of the main assistant files:

```bash
python jarvis_chatgpt.py
# or
python jarvis_deepseek.py
# or
python jarvis_ollama.py
```

3. The assistant listens to your voice, processes it, and plays back the AI-generated response.

---

## 🧠 AI Models & APIs Used

- **ChatGPT Assistant** (via OpenAI API)
- **DeepSeek-R1** (via Ollama)
- **LLaMA 3** (via Ollama)
- **Text-to-Speech** using `tts-1` model, voice: "echo"

---

## 📌 Notes

- Replace all `"your API key"` values with your actual keys securely.
- For Ollama, make sure models are downloaded before use (e.g. `ollama run llama3.1:8b`).
- Tags like `#lights-1` or `#3d_printer-0` should be used correctly to simulate or control devices.

---

## 👨‍💻 Author

Amirali Kamali  
[GitHub: AmiraliKamali](https://github.com/AmiraliKamali)

---

## ⚠️ Security Notice

Make sure API keys and sensitive credentials are **not committed** to GitHub. Use environment variables or a `.env` file for security.
