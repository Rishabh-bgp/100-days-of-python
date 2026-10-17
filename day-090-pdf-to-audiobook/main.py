"""Day 90 - Portfolio project: PDF to audiobook. Extract the text from a PDF with pypdf and
turn it into speech with an OFFLINE text-to-speech engine.

API-free: the course suggests a cloud TTS API (account + key). This uses whatever local
engine your OS has:
  - Linux: espeak-ng (sudo apt install espeak-ng)  -> writes a .wav file
  - macOS: the built-in `say` command               -> writes an .aiff file
  - Windows: built-in System.Speech via PowerShell  -> writes a .wav file
If none is found it still extracts the text to a .txt file and tells you what to install.

  python main.py                 # uses a generated sample.pdf
  python main.py book.pdf        # your own PDF
"""
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

import make_sample_pdf

HERE = Path(__file__).parent


def extract_text(pdf: Path) -> str:
    reader = PdfReader(pdf)
    return "\n".join((page.extract_text() or "").strip() for page in reader.pages).strip()


def speak_to_file(text: str, out_stem: Path) -> Path | None:
    system = platform.system()
    engine = shutil.which("espeak-ng") or shutil.which("espeak")
    if engine:
        out = out_stem.with_suffix(".wav")
        subprocess.run([engine, "-w", str(out), "-s", "160", text], check=True)
        return out
    if system == "Darwin" and shutil.which("say"):
        out = out_stem.with_suffix(".aiff")
        subprocess.run(["say", "-o", str(out), text], check=True)
        return out
    if system == "Windows":
        out = out_stem.with_suffix(".wav")
        safe = text.replace("'", "''")
        ps = ("Add-Type -AssemblyName System.Speech; $s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
              f"$s.SetOutputToWaveFile('{out}'); $s.Speak('{safe}'); $s.Dispose()")
        subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True)
        return out
    return None


def main(argv: list[str]) -> Path | None:
    out_dir = HERE / "output"
    out_dir.mkdir(exist_ok=True)
    pdf = Path(argv[0]) if argv else make_sample_pdf.make(out_dir / "sample.pdf")
    text = extract_text(pdf)
    txt = out_dir / f"{pdf.stem}.txt"
    txt.write_text(text, encoding="utf-8")
    print(f"Extracted {len(text.split())} words from {pdf.name} -> {txt.name}")
    audio = speak_to_file(text, out_dir / pdf.stem)
    if audio:
        print(f"Audiobook written to {audio} ({audio.stat().st_size // 1024} KB)")
    else:
        print("No offline TTS engine found. Install espeak-ng (Linux) - macOS and Windows have one built in.")
    return audio


if __name__ == "__main__":
    main(sys.argv[1:])
