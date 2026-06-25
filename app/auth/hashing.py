from passlib.context import CryptContext # type: ignore

pwd = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
) 

def hash_password(password: str)->str:
    hashed_pass = pwd.hash(password)
    return hashed_pass

def verify_password(password: str, stored_hash_password: str)-> bool:
    return pwd.verify(password,stored_hash_password)

hashed = hash_password("soham123")

print(hashed)

print(
    verify_password(
        "soham123",
        hashed
    )
)