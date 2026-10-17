"""Day 46 - Musical Time Machine: pick a date, scrape that week's top 100 songs, make a playlist.

Account-free: the course scrapes Billboard and creates a Spotify playlist (Spotify developer
account + OAuth). Here it scrapes a bundled sample chart (chart_YYYY-MM-DD.html, fictional
songs) and writes a local playlist as both CSV and M3U.
"""
import csv
from pathlib import Path

from bs4 import BeautifulSoup

HERE = Path(__file__).parent


def available_dates() -> list[str]:
    return sorted(p.stem.removeprefix("chart_") for p in HERE.glob("chart_*.html"))


def scrape_chart(date: str) -> list[dict]:
    soup = BeautifulSoup((HERE / f"chart_{date}.html").read_text(encoding="utf-8"), "html.parser")
    rows = soup.select("li.chart-row") or soup.select("li")
    songs = []
    for row in rows:
        title = row.select_one("h3.c-title") or row.select_one("h3")
        artist = row.select_one("span.artist") or row.select_one("span.c-label")
        if title:
            songs.append({"rank": len(songs) + 1, "title": title.get_text(strip=True),
                          "artist": artist.get_text(strip=True) if artist else "Unknown"})
    return songs


def write_playlist(date: str, songs: list[dict]) -> tuple[Path, Path]:
    out = HERE / "playlists"
    out.mkdir(exist_ok=True)
    csv_path, m3u_path = out / f"{date}_top100.csv", out / f"{date}_top100.m3u"
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["rank", "title", "artist"])
        w.writeheader()
        w.writerows(songs)
    lines = ["#EXTM3U", f"#PLAYLIST:{date} Billboard-style 100"]
    for s in songs:
        lines += [f"#EXTINF:-1,{s['artist']} - {s['title']}", f"{s['artist']} - {s['title']}.mp3"]
    m3u_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return csv_path, m3u_path


def main(ask=input) -> None:
    dates = available_dates()
    date = ask(f"Which year do you want to travel to? Type the date in YYYY-MM-DD format {dates}: ").strip()
    if date not in dates:
        print(f"No bundled chart for {date}; using {dates[0]}.")
        date = dates[0]
    songs = scrape_chart(date)
    csv_path, m3u_path = write_playlist(date, songs)
    print(f"Wrote {len(songs)} songs to {csv_path.name} and {m3u_path.name}")


if __name__ == "__main__":
    main()
