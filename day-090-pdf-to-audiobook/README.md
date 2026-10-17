# Day 90: PDF to Audiobook

Day 90 - Portfolio project: PDF to audiobook. Extract the text from a PDF with pypdf and
turn it into speech with an OFFLINE text-to-speech engine.

API-free: the course suggests a cloud TTS API (account + key). This uses whatever local
engine your OS has:
  - Linux: espeak-ng (sudo apt install espeak-ng)  -> writes a .wav file
  - macOS: the built-in `say` command               -> writes an .aiff file
  - Windows: built-in System.Speech via PowerShell  -> writes a .wav file
If none is found it still extracts the text to a .txt file and tells you what to install.

  python main.py                 # uses a generated sample.pdf
  python main.py book.pdf        # your own PDF

**Topic:** Portfolio

**Concepts:** PDF text extraction, text-to-speech

## Notes

API-free (replaced cloud text-to-speech APIs with the OS's offline engine: espeak-ng on Linux, `say` on macOS, System.Speech on Windows). Tested on Linux only.

## Files

- `main.py`
- `make_sample_pdf.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
python make_sample_pdf.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
