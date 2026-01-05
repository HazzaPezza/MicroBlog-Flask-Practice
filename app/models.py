# File used to manipulate SQLAlchemy ORM to create DB tables for application.
# Class User inherits Model from db which we've imported from the __init__.py file.
# SQL query structures then become lines of Python code. Much easier to deal with.
from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    """
    Class declares ORM model for Users table in database.
    """
    # Mapped[int] declares type of variable
    # Mapped_column declares how it's mapped to db.
    # In this case it allows us to specify it as primary key.
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)

    # Password element is stored as plain text but will need to be a hashed element.
    # Hashing allows for data security.
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')

    # This function tells Python how to print database objets. Useful for debugging.ß
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    """
    Class declares ORM model for Post table in database. 
    Takes in foreign key for user_id from User table.
    """
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True,
        default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    