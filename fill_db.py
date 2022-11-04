"""Create and populate a small database. Creates the file "data.db" """
from datetime import datetime
from time import sleep
from app import db, app
from models import Task

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        t = Task(title="some task", date=datetime.utcnow())
        print(t)
        db.session.add(t)
        db.session.commit()

        sleep(2)
        t = Task(title="some other task", date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()

        tasks = Task.query.all()
        print(tasks)
