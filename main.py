# Copyleft 🄯 2025, Germano Castanho
# Free software under the GNU GPL v3


import random
import time
import uuid
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from groq import Groq

_ = load_dotenv(find_dotenv())


DOCS_DIR = Path(__file__).parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)


CLIENT = Groq()
MAX_RETRY = 3
TIMEOUT = 60


def get_source_path():
    print("Bem-vindo ao Audio Transcriber! 🎙️")
    time.sleep(1)

    source_path = input("Forneça o caminho ao arquivo: 📁\n")
    return source_path


def retry_transcription(source_path):
    for n in range(MAX_RETRY):
        try:
            timeout = TIMEOUT * (2**n)
            transcript = CLIENT.audio.transcriptions.create(
                model="whisper-large-v3",
                file=source_path,
                language="pt",
                response_format="text",
                temperature=0.2,
                timeout=timeout,
            )

            return transcript

        except Exception as e:
            if n < MAX_RETRY - 1:
                backoff = (2**n) + random.uniform(0.5, 1.5)
                time.sleep(backoff)
                source_path.seek(0)

            else:
                print("Erro! Ocorreu um erro inesperado! ☠️")
                print(f"Detalhes: {e}")


def transcribe_audio(source_path):
    print("Transcrevendo arquivo... Por favor, aguarde! ⏳")
    doc_dir = DOCS_DIR / f"{uuid.uuid4()}.md"

    try:
        with open(source_path, "rb") as input_file:
            transcript = retry_transcription(input_file)

        with open(doc_dir, "w", encoding="utf-8") as output_file:
            output_file.write(transcript)
            print("Successo! Seu arquivo foi transcrito! 🚀")
            print(f"Salvo como: {doc_dir.name}")

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado! 📁")
        print("Por favor, tente novamente! 🛠️")

    except KeyboardInterrupt:
        print("Processo interrompido! ❌")
        print("Saindo... 👋")

    except Exception as e:
        print("Erro! Ocorreu um erro inesperado! ☠️")
        print(f"Detalhes: {e}")


def main():
    source_path = get_source_path()
    transcribe_audio(source_path)


if __name__ == "__main__":
    main()