from fastapi import FastAPI
from fastapi_tutorial.app.schemas import PostCreate
from fastapi_tutorial.app.schemas import PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "First Post", "content": "This is the content of the first post."},
    2: {"title": "Second Post", "content": "This is the content of the second post."},
    3: {"title": "Third Post", "content": "This is the content of the third post."},
    4: {"title": "Fourth Post", "content": "This is the content of the fourth post."},
    5: {"title": "Fifth Post", "content": "This is the content of the fifth post."},
}
@app.get("/posts")
def get_posts(limit: int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = text_posts.get(post_id)
    if post:
        return post
    return {"error": "Post not found"}

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post_id = max(text_posts.keys()) + 1
    new_post = {"title": post.title, "content": post.content}
    text_posts[new_post_id] = new_post
    return PostResponse(**new_post)