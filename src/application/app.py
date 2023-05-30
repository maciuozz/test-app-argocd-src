"""
Module for define API endpoints
"""

import uvicorn
from fastapi import FastAPI


app = FastAPI(
    port=8081
)

root_endpoint_message = {"message": "Hello world finally updated"}
health_message = {"health": "ok"}

"""
Root endpoint definition
"""
@app.get("/")
async def root():
    """Result of calling the root endpoint
    Returns
    -------
    'Hello world' message
    """
    return root_endpoint_message

@app.get("/health")
async def health():
    """Result of calling /health endpoint
    Returns
    -------
    JSON message with health status
    """
    return health_message

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
