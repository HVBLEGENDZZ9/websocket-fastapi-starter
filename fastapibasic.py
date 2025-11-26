from fastapi import FastAPI
import uvicorn
from basemodel import NumberModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/add")
def add_nums(number: NumberModel):
    result = number.value1 + float(number.value2)
    return {"label": number.label, "result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
