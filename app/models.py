"""
数据库模型
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app

from . import db, login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    def __repr__(self):
        return '<Role {name}>'.format(name=self.name)

    @staticmethod
    def insert_roles():
        roles = {
            "User": (Permission.FOLLOW | Permission.COMMENT |
                     Permission.WREITE_ARTICLES, True),
            "Moderator": (Permission.FOLLOW | Permission.COMMENT |
                          Permission.WREITE_ARTICLES | Permission.MODERATE_COMMENTS,
                          False),
            "Administor": (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            print(role)
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.merge(role)
        db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {name}>'.format(name=self.name)

# 没有这个函数就好报错，为什么？
@login_manager.user_loader
def user_load(user_id):
    return User.query.get(int(user_id))


class Permission:
    """
    权限表示
    """
    FOLLOW = 0x01
    COMMENT = 0x02
    WREITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTOR = 0x08


