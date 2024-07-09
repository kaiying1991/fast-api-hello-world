import uvicorn
from fastapi import FastAPI

app = FastAPI()

fruits = {
	'1': 'apple',
	'2': 'orange',
	'3': 'watermelon'
}

@app.get('/')
def get_fruits():
	return fruits

@app.post('/')
def new_fruit(fruit:dict):
	fruits.update(fruit)
	return fruit

uvicorn.run(app, host="0.0.0.0", port=8000)