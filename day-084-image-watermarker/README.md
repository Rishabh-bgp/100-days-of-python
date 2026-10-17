# Day 84: Image Watermarker

Day 84 - Portfolio project: image watermarking desktop app (tkinter + Pillow).
Pick an image, type your watermark text, preview, and save a watermarked copy.

Also works without a GUI:
  python main.py --cli input.jpg output.png "© My Name" [--tiled]
  python main.py --demo         # makes a sample image and watermarks it

**Topic:** Portfolio

**Concepts:** Pillow, tkinter file dialogs

## Notes

Core watermark function also works from the CLI.

This project opens a window (tkinter/turtle), so it needs a desktop session. On Linux you may need `sudo apt install python3-tk`.

## Files

- `main.py`
- `requirements.txt`
- `watermark.py`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
