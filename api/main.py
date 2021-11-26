from fastapi import FastAPI

from api.routers import verification_letter

app = FastAPI()

app.include_router(verification_letter.router)
