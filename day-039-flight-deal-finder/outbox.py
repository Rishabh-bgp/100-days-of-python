"""Account-free email: write .eml files to ./outbox, or send to a LOCAL debugging SMTP server.

Replaces Gmail SMTP + app password. By default messages go to the outbox/ folder.
Set LOCAL_SMTP=1 to deliver with smtplib to localhost:1025 instead; start a throwaway
server first with:  python -m aiosmtpd -n -l localhost:1025   (pip install aiosmtpd)
No login, no account, nothing leaves your machine.
"""
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path

OUTBOX = Path(__file__).with_name("outbox")


def send_email(to: str, subject: str, body: str, sender: str = "me@example.com", outbox: Path = OUTBOX) -> Path:
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = sender, to, subject
    msg.set_content(body)
    if os.environ.get("LOCAL_SMTP"):
        with smtplib.SMTP("localhost", int(os.environ.get("LOCAL_SMTP_PORT", "1025"))) as conn:
            conn.send_message(msg)
        print(f"[local smtp] To: {to} | Subject: {subject}")
        return outbox
    outbox.mkdir(exist_ok=True)
    path = outbox / f"{datetime.now():%Y%m%d-%H%M%S-%f}-{to.replace('@', '_at_')}.eml"
    path.write_bytes(bytes(msg))
    print(f"[outbox] To: {to} | Subject: {subject}\n{body}\n")
    return path
