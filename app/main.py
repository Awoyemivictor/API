from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# For the sqlalchemy engine
models.Base.metadata.create_all(bind=engine)

# to initialize the fastapi library routes
app = FastAPI()


# To grab the router from post and user
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

# ROUTE PATHS & THEIR FUNCTIONS

# 1a. ------ WITH REGULAR SQL --------------------
# @app.get("/posts")
# def get_posts():
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # return {"data": posts}

# 1b. ------ WITH SQLALCHEMY (NOSQL) --------------------
