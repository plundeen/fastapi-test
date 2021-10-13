#!/usr/bin/env python3
"""Demo app to play around with FastAPI"""

import multiprocessing
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """index endpoint"""
    return {"hello": "world!"}

@app.get("/test")
def test():
    """test endpoint"""
    return "Yep, this is the test endpoint all right!"

if __name__ == '__main__':
    multiprocessing.freeze_support()
    uvicorn.run(app, port=8000, reload=False)
    