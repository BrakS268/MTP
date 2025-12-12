from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def hello():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>FastAPI Hello</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin-top: 300px;
                    background: gray;
                    font-family: Arial;
                }
                .container {
                    background: white;
                    padding: 40px;
                    border-radius: 15px;
                    text-align: center;
                }
                h1 {
                    color: black;
                    font-size: 48px;
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, World!</h1>
            </div>
        </body>
        </html>
        """


uvicorn.run(app)
