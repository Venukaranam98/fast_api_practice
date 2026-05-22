from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from models import Post

from schemas import PostSchema

from routers.auth import get_current_user

router = APIRouter()

@router.post("/posts")

def create_post(

    post: PostSchema,

    db: Session = Depends(get_db),



):

    new_post = Post(

        title=post.title,

        content=post.content,

        user_id=1

    )


    db.add(new_post)

    db.commit()


    return {

        "message": "Post created successfully"

    }

@router.get("/posts")

def get_posts(

    db: Session = Depends(get_db)

):

    posts = db.query(

        Post

    ).all()


    return posts