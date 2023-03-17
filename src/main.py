from uuid import uuid4
import logging
import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from middleware.security import SecurityMiddleware
from routes.game import router

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8888",
    "http://localhost",
    "http://localhost:8888",
]

app.include_router(router)
app.add_middleware(SecurityMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = uuid4()
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(
        f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

    logger.info(request.headers)

    return response

if __name__ == "__main__":
    uvicorn.run("app", host="0.0.0.0", port=8888, reload=True)
