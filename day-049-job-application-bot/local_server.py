"""Run a Flask app (or a static folder) on 127.0.0.1 in a background thread, for Selenium bots."""
import logging
import threading

from werkzeug.serving import make_server


class LocalServer:
    def __init__(self, app, port: int = 0) -> None:
        logging.getLogger("werkzeug").setLevel(logging.ERROR)
        self.server = make_server("127.0.0.1", port, app)
        self.url = f"http://127.0.0.1:{self.server.server_port}"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def __enter__(self) -> "LocalServer":
        self.thread.start()
        return self

    def __exit__(self, *exc) -> None:
        self.server.shutdown()
