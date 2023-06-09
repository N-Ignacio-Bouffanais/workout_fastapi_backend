from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth.router import users
from .api.router import routines
from .auth import models
from .auth import schemas


app = FastAPI(
    title="Social media app with fast API",
    description="This is going to be the backend with Fast API",
    version="1.0.0",
    contact={
        "name": "Nicolas Bouffanais",
        "url": "https://portfolio-nicolas-bouffanais.vercel.app/",
        "email": "nicolas.bouffanais.1999@gmail.com",
    },
)
app.include_router(users)
app.include_router(routines)

# I need to change this later to merge the backend with the frontend
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to my app"}
