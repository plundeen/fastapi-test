#!/usr/bin/env python3
"""Demo app to play around with FastAPI"""

import multiprocessing
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    """index endpoint"""
    return {"hello": "world!"}

@app.get("/test")
def test():
    """test endpoint"""
    return "Yep, this is the test endpoint all right!"

@app.get("/table")
def table():
    """return an HTML table"""
    data = '''
    <html>
        <body>
            <table>
                <thead>
                    <tr>
                    <td>Foo</td>
                    <td>Bar</td>
                    </tr>
                </thead>
                <tr>
                    <td>1</td>
                    <td>2</td>
                </tr>
            </table>
        </body>
    </html>
    '''

    # with open('C:/Users/phillundeen/AppData/Local/Temp/failure_table.html', 'r') as f:
    #     data = f.read()
    return HTMLResponse(content=data, status_code=200)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    uvicorn.run(app, port=8000, reload=False)
    