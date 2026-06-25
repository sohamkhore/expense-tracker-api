from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.oauth2 import oauth2_scheme
from app.auth.jwt_handler import verify_access_token
from app.dependencies import get_db

from app.models.user import User

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
   

    user_id = verify_access_token(token)
   

    user = db.query(User).filter(User.id == int(user_id)).first()
    

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials"
        )

    return user