from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

#----------- Users sending data to us -----------------
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# User create post    
class PostCreate(PostBase):
    pass

# Response Back to the User after he creates account
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # for sqlalchemy to convert it to a regular pydantic model
    class Config:
        from_attributes = True
        
        
#------------ We sending data back to the user --------------
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    # for sqlalchemy to convert it to a regular pydantic model
    class Config:
        orm_mode = True
        
class PostOut(BaseModel):
    Post: Post
    votes: int
    
    class Config:
        orm_mode = True
        
        
# User creating an account
class UserCreate(BaseModel):
    email: EmailStr
    password: str
        

#------------ Retrieving information from the user --------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
# Schema for access token
class Token(BaseModel):
    access_token: str
    token_type: str
    
# Schema for token data
class TokenData(BaseModel):
    id: Optional[str] = None
    
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    