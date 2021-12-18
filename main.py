import datetime
import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.graphql import graphql_app

app = FastAPI()
app.mount('/graph', graphql_app)


@app.on_event('startup')
async def startup():
    public_paths = {'/', '/graph'},


@app.get("/")
async def root():
    return {"message": {
        "app_name": settings.APP_NAME,
        "system_time": datetime.datetime.now()
    }}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=True,
        port=settings.PORT,
        debug=False
    )
