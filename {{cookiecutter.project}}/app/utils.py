# -*- coding: utf-8 -*-
#   import os
#   from datetime import datetime, timedelta, timezone
#   from functools import wraps

#   import jwt
#   from argon2 import PasswordHasher
#   from argon2.exceptions import VerifyMismatchError
#   from dotenv import load_dotenv
#   from graphql import GraphQLError

#   from app.db.database import Session
#   from app.db.models import User

#   load_dotenv()

#   ALGORITHM = os.getenv("ALGORITHM")
#   TOKEN_EXPIRE_MINUTES = os.getenv("TOKEN_EXPIRE_MINUTES")
#   SECRET_KEY = os.getenv("SECRET_KEY")

"""
This is here for when we start creating JWT tokens.
Reveiw the PyJWT package and clean up the `get_authenticated_user function.
"""


#   def get_authenticated_user(context):
#       request_object = context.get("request")
#       auth_header = request_object.headers.get("Authorization")

#       token = [None]
#       if auth_header:
#           token = auth_header.split(" ")

#       if auth_header and token[0] == "Bearer" and len(token) == 2:
#           token = auth_header.split(" ")[1]

#           try:
#               payload = jwt.decode(token[1], SECRET_KEY, algorithms=[ALGORITHM])

#               if datetime.now(timezone.utc) > datetime.fromtimestamp(
#                   payload.get("exp"),
#                   tz=timezone.utc,
#               ):
#                   raise GraphQLError("Token has expired")

#               with Session() as session:
#                   user = (
#                       session.query(User)
#                       .filter(User.email == payload.get("sub"))
#                       .first()
#                   )

#                   if not user:
#                       raise GraphQLError("User does not exist")

#                   return user

#           # This will catch all JWT errors
#           except jwt.exceptions.PyJWTError:
#               raise GraphQLError("Invalid authentication token")

#           # This will catch all other Non-JWT errors such as database errors. It will mask
#           # The errors from being exposed to the front nad will give a generic error. You
#           # will log to catch the specific error that through this to learn more and what
#           # The error was exactly.
#           except Exception as e:
#               # Logger will go here!
#               raise GraphQLError("Could not authenticate.")

#       else:
#           raise GraphQLError("Missing authorization header")


#   def generate_token(email):
#       # now + token_lifespan
#       expiration_time = datetime.utcnow() + timedelta(
#           minutes=TOKEN_EXPIRE_MINUTES,
#       )

#       payload = {
#           "sub": email,
#           "exp": expiration_time,
#       }

#       token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

#       return token


#   def hash_password(pwd):
#       ph = PasswordHasher()
#       return ph.hash(pwd)


#   def verify_password(pwd_hash, pwd):
#       ph = PasswordHasher()

#       try:
#           ph.verify(pwd_hash, pwd)
#       except VerifyMismatchError:
#           raise GraphQLError("Invalid password")
