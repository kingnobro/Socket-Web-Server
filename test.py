import pymysql

from models.todo import Todo
from models.user import User
from models.session import Session
from models.comment import Comment
from models.weibo import Weibo
from utils import random_string


# noinspection SqlNoDataSourceInspection,SqlResolve
def test():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='wuronghuan',
        # db='web8',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        cursor.execute('DROP DATABASE `web8`')
        cursor.execute('CREATE DATABASE `web8` CHARACTER SET utf8mb4')
        cursor.execute('USE `web8`')

        cursor.execute(User.sql_create)
        cursor.execute(Session.sql_create)
        cursor.execute(Todo.sql_create)
        cursor.execute(Comment.sql_create)
        cursor.execute(Weibo.sql_create)
    connection.commit()
    connection.close()

    form = dict(
        username='kingno',
        password='123',
    )
    User.register_user(form)
    u, result = User.login_user(form)
    assert u is not None, result
    form = dict(
        username='Tom',
        password='123',
    )
    User.register_user(form)

    session_id = random_string()
    form = dict(
        session_id=session_id,
        user_id=u.id,
    )
    Session.new(form)
    s: Session = Session.one(session_id=session_id)
    assert s.session_id == session_id

    form = dict(
        title='test todo',
        user_id=u.id,
    )
    t = Todo.add(form, u.id)
    assert t.title == 'test todo'

    form2 = dict(
        content='hello world',
    )
    c = Comment.add(form2, 2, 3)
    assert c.content == 'hello world'


if __name__ == '__main__':
    test()
