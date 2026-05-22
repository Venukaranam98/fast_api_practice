from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String,ForeignKey

from database import Base
from sqlalchemy.orm import relationship


class Student(Base):

    __tablename__ = "students"


    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    name = Column(

        String

    )


    marks = Column(

        Integer

    )



class User(Base):

    __tablename__ = "users"


    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    username = Column(

        String(100),

        unique=True

    )


    email = Column(

        String(255),

        unique=True

    )


    password = Column(

        String(255)

    
    )
    posts = relationship(

    "Post",

    back_populates="owner"

)


class Post(Base):

    __tablename__ = "posts"


    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    title = Column(

        String

    )


    content = Column(

        String

    )


    user_id = Column(

        Integer,

        ForeignKey("users.id")

    )
    owner = relationship(

    "User",

    back_populates="posts"

)