"""Write a small multi-page sample PDF using only the standard library (no reportlab)."""
from pathlib import Path

PAGES = [
    ["Chapter One", "Every journey of a hundred days begins with a single line of code.",
     "Today we turn a PDF into speech, entirely offline."],
    ["Chapter Two", "The text is extracted page by page,", "then handed to a local text-to-speech engine."],
]


def _escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def make(path: Path) -> Path:
    objects = ["<< /Type /Catalog /Pages 2 0 R >>", None, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    kids = []
    for lines in PAGES:
        stream = "BT /F1 16 Tf 72 720 Td 22 TL " + " ".join(f"({_escape(l)}) '" for l in lines) + " ET"
        objects.append(f"<< /Length {len(stream)} >>\nstream\n{stream}\nendstream")
        content_id = len(objects)
        objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                       f"/Resources << /Font << /F1 3 0 R >> >> /Contents {content_id} 0 R >>")
        kids.append(f"{len(objects)} 0 R")
    objects[1] = f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(kids)} >>"
    out = b"%PDF-1.4\n"
    offsets = []
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n{obj}\nendobj\n".encode("latin-1")
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode()
    out += "".join(f"{o:010d} 00000 n \n" for o in offsets).encode()
    out += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    path.write_bytes(out)
    return path


if __name__ == "__main__":
    print("wrote", make(Path(__file__).with_name("sample.pdf")))
