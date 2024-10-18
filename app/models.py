from typing import List, Optional
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Users Model
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    registered_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    # Relationships
    profile: Mapped["Profile"] = relationship(back_populates="u_profile", uselist=False) # One-to-One Relationship
    posts: Mapped[List["Post"]] = relationship(back_populates="u_posts") # One-to-Many Relationship
    comments: Mapped[List["Comment"]] = relationship(back_populates="u_comments")

    # Methods
    def __repr__(self) -> str:
        return f"User(id{self.id}, username={self.username}, email={self.email}, registered_date={self.registered_date})"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)


# Profiles Model
class Profile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25))
    last_name: Mapped[str] = mapped_column(String(25))
    biography: Mapped[str] = mapped_column(Text)

    # User - Profile Relationship
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    u_profile: Mapped["User"] = relationship(back_populates="profile")


# Categories - Model
class Category(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(25), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    # Relationship
    posts: Mapped[List["Post"]] = relationship(back_populates="c_posts") # One-to-Many Relationship

    # Debugging Purposes
    def __repr__(self) -> str:
        return f"Category(id={self.id}, key={self.key}, name={self.name})"


# Posts Model
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    body: Mapped[str] = mapped_column(Text)
    featured_image: Mapped[str] = mapped_column(String(255))
    timestamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    # User - Post Relationship
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    u_posts: Mapped["User"] = relationship(back_populates="posts")

    # Categories - Post Relationship
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.id))
    c_posts: Mapped["Category"] = relationship(back_populates="posts")

    # Debugging Purposes
    def __repr__(self) -> str:
        return f"Post(id={self.id}, title={self.title}, body={self.body}, \
            user_id={self.user_id}, category_id={self.category_id})"
    

# Comments Model
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    u_comments: Mapped["User"] = relationship(back_populates="comments")
    

# Subscriber Model
class Subscriber(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)

    # Debugging Purposes
    def __repr__(self) -> str:
        return f"Subscriber(id={self.id}, email={self.email})"



