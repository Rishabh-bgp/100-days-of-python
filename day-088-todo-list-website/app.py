"""Day 88 - Portfolio project: to-do list website. Multiple lists, add tasks with optional
due dates, tick them off, delete, and filter by status. Flask 3 + SQLite (SQLAlchemy 2.0).

Run with:  flask --app app run
"""
import os
from datetime import date

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///todo.db")
db.init_app(app)


class TodoList(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    tasks: Mapped[list["Task"]] = relationship(back_populates="todo_list", cascade="all, delete-orphan")


class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(250))
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    due: Mapped[str | None] = mapped_column(String(10), nullable=True)
    list_id: Mapped[int] = mapped_column(ForeignKey("todo_list.id"))
    todo_list: Mapped[TodoList] = relationship(back_populates="tasks")

    @property
    def overdue(self) -> bool:
        return bool(self.due) and not self.done and self.due < date.today().isoformat()


with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(TodoList)).first():
        db.session.add(TodoList(name="Today"))
        db.session.commit()


@app.route("/")
def home():
    first = db.session.execute(db.select(TodoList).order_by(TodoList.id)).scalars().first()
    return redirect(url_for("show_list", list_id=first.id))


@app.route("/list/<int:list_id>")
def show_list(list_id: int):
    todo = db.get_or_404(TodoList, list_id)
    status = request.args.get("status", "all")
    tasks = [t for t in todo.tasks if status == "all" or (status == "done") == t.done]
    lists = db.session.execute(db.select(TodoList).order_by(TodoList.name)).scalars().all()
    return render_template("index.html", todo=todo, tasks=tasks, lists=lists, status=status)


@app.post("/list")
def new_list():
    name = request.form.get("name", "").strip()
    if name and not db.session.execute(db.select(TodoList).where(TodoList.name == name)).scalar():
        db.session.add(TodoList(name=name))
        db.session.commit()
    found = db.session.execute(db.select(TodoList).where(TodoList.name == name)).scalar()
    return redirect(url_for("show_list", list_id=found.id) if found else url_for("home"))


@app.post("/list/<int:list_id>/task")
def add_task(list_id: int):
    text = request.form.get("text", "").strip()
    if text:
        db.session.add(Task(text=text, due=request.form.get("due") or None, list_id=list_id))
        db.session.commit()
    return redirect(url_for("show_list", list_id=list_id))


@app.post("/task/<int:task_id>/toggle")
def toggle(task_id: int):
    task = db.get_or_404(Task, task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("show_list", list_id=task.list_id))


@app.post("/task/<int:task_id>/delete")
def delete(task_id: int):
    task = db.get_or_404(Task, task_id)
    list_id = task.list_id
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("show_list", list_id=list_id))
