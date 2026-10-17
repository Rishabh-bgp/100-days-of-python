"""Day 63 exercise: the same table with raw sqlite3, then with SQLAlchemy 2.0 Core-style ORM."""
import sqlite3

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


def raw_sqlite() -> list[tuple]:
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT UNIQUE NOT NULL, author TEXT, rating REAL)")
    con.execute("INSERT INTO books VALUES (1, 'Sample Book', 'A. Writer', 9.3)")
    return con.execute("SELECT * FROM books").fetchall()


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    rating: Mapped[float]


def orm() -> list[str]:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Book(title="Sample Book", rating=9.3), Book(title="Another Book", rating=7.5)])
        s.commit()
        book = s.get(Book, 1)
        book.rating = 9.5
        s.commit()
        return [f"{b.title}: {b.rating}" for b in s.scalars(select(Book).order_by(Book.rating.desc()))]


if __name__ == "__main__":
    print(raw_sqlite())
    print(orm())
