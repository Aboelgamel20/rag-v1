from fastapi import FastAPI

app = FastAPI()

@app.get('/welcome')
def welcome():
    return "welcome to the first trial of the program."