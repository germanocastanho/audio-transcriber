# Copyleft 🄯 2025, Germano Castanho
# Free software under the GNU GPL v3


import time
import uuid
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())


DOCS_DIR = Path(__file__).parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)


CLIENT = OpenAI()
PROMPT = """Transcribe the provided audio or video file. Identify the speakers from contextual cues and format their speeches accordingly. Ensure accurate transcription and proper formatting. The transcription must be in Brazilian Portuguese only. Do not include any commentary or explanations. Just provide the transcription in a clean and readable format."""


def get_source_path():
    print("Welcome to the Audio Transcriber! 🎙️")
    time.sleep(1)

    source_path = input("Provide the path to the file: 📁\n")
    return source_path


def transcribe_audio(source_path):
    print("Transcribing your file... Please wait! ⏳")
    doc_dir = DOCS_DIR / f"{uuid.uuid4()}.md"

    try:
        with open(source_path, "rb") as input_file:
            transcript = CLIENT.audio.transcriptions.create(
                file=input_file,
                model="gpt-4o-transcribe",
                chunking_strategy="auto",
                language="pt",
                prompt=PROMPT,
                response_format="text",
                temperature=0.2,
                timeout=None,
            )

        with open(doc_dir, "w", encoding="utf-8") as output_file:
            output_file.write(transcript)
            print("Success! Your file has been transcribed! 🚀")
            print(f"Saved as: {doc_dir.name}")

    except FileNotFoundError:
        print("Error: The provided path wasn't found! 📁")
        print("Please check the path and try again! 🛠️")

    except TimeoutError:
        print("Error: The transcription request timed out! ⏰")
        print("Please check your connection and try again! 🌐")

    except Exception as e:
        print("Error! An unexpected error occurred! ❌")
        print(f"Details: {e}")


def main():
    source_path = get_source_path()
    transcribe_audio(source_path)


if __name__ == "__main__":
    main()
