# Deploying without a hosting account

## 1. Run with gunicorn (Linux/macOS)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
gunicorn -c gunicorn.conf.py app:app      # http://127.0.0.1:8000
```

On Windows gunicorn isn't available; use `pip install waitress` and then `waitress-serve --port=8000 app:app`.

## 2. Run in Docker (optional)

```bash
docker build -t my-blog .
docker run --rm -p 8000:8000 -e SECRET_KEY=change-me -v blogdata:/app/instance my-blog
```

The SQLite database lives in `/app/instance`; the named volume keeps it between runs.

## 3. Production checklist (what the course's deploy day teaches)

- Keep secrets out of code: `SECRET_KEY` and `DATABASE_URL` come from environment variables (see `.env.example`).
- Use a real WSGI server (gunicorn or waitress), not `flask run`.
- Pin dependencies in `requirements.txt`.
- Use Postgres for multi-user production by setting `DATABASE_URL=postgresql+psycopg://...` and adding `psycopg[binary]`. SQLite is fine on one machine.
- Sharing on your local network: run gunicorn bound to `0.0.0.0` and open `http://<your-ip>:8000` from another device.
- Git basics: `git init`, `git add`, `git commit`, `.gitignore` for `*.db`, `.env` and `.venv`, then push to any Git host if you want a backup.
