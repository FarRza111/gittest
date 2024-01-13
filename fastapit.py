from typing import Optional, List
from pydantic import BaseModel,Field
from fastapi import FastAPI

app = FastAPI()

class ProfileInfo(BaseModel):
    short_description: str
    long_bio: str

class User(BaseModel):
    username: str = Field(alias='name',
                          title = 'THIS IS USERNAME',
                          description='BE GREATER',
                          min_length=1,
                          max_length=25,
                          default='HELLO'
                          )
    profile_info: ProfileInfo
    liked_posts: Optional[List[int]] = Field(
        description='array of post ids user liked',
        min_length= 1, max_length=2
    )

def get_user_info() -> User:
    profile_info_data = {
        'short_description': 'my bio description',
        'long_bio': 'this is our long bio'
    }

    profile_info = ProfileInfo(**profile_info_data)

    user_content = {
        'name': 'Farizo',
        'liked_posts': [1],
        'profile_info': profile_info
    }

    return User(**user_content)

@app.get("/user/me", response_model=User)
def test_endpoint():
    user = get_user_info()
    return user
