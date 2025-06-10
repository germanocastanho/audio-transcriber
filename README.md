# 🎙️ Audio Transcriber

**Audio Transcriber** is a Python script that transcribes **audio and video files** into text using OpenAI's transcription models. Specifically designed for **Brazilian Portuguese** content, it automatically infers speakers from context and formats the transcription appropriately. Perfect for any audio/video content that needs accurate transcription! 📄

# 🚀 Main Features

- **Easy Transcription**: 🔊 Convert audio/video files to text with a simple command-line interface.
- **Brazilian Focused**: 🇧🇷 Optimized for accurate transcription of Brazilian Portuguese content.
- **Context Inference**: 👥 Automatically identifies speakers and formats dialogue appropriately.
- **Markdown Output**: 📝 Saves transcriptions as simple but useful markdown files with unique IDs.
- **Format Flexibility**: 🎥 Supports various file formats, including _MP3, MP4, WAV, M4A_ and more.

# ✅ Prerequisites

- **Python 3.12+**, available through the [**official website**](https://www.python.org/downloads/).
- **OpenAI API Key**, obtainable from the [**OpenAI platform**](https://platform.openai.com/login).

# 🛠️ Local Installation

```bash
# Clone the repository
git clone https://github.com/germanocastanho/audio-transcriber.git

# Navigate to the directory
cd audio-transcriber

# Set up a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up your API key
echo "OPENAI_API_KEY=YOUR_API_KEY" > .env

# Run the "main.py" script
python3 main.py
```

# 📜 Free Software

Distributed under the [**GNU GPL v3**](LICENSE), ensuring freedom - as in "free speech" - to use, modify, and redistribute the software, as long as these freedoms are preserved in any derivative versions. By using or contributing, you support the **free software** philosophy and help build a libertarian technological environment! ✊
