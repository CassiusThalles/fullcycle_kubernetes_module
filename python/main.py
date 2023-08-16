from fastapi import FastAPI, Response, status
import os
import datetime

startedAt = datetime.datetime.now()

app = FastAPI()

environment_variables = os.environ

@app.get("/")
async def hello():
    try:
        name = environment_variables['NAME']
        age = environment_variables['AGE']
        return {"message": f"Hello, I'm {environment_variables['NAME']}. I'm {environment_variables['AGE']} years old."}
    except KeyError:
        return {"message": "Hello, I'm a FastAPI application."}

@app.get("/configmap")
async def configmap():
    with open(os.path.join('myfamily', 'family.txt'), 'r') as f:
        configmap = f.read()
    return {"message": f"My family: {configmap}"}

@app.get("/secret")
async def secret():
    try:
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        return {"message": f"User: {user}, Password: {password}"}
    except KeyError:
        return {"message": "No secret found."}

@app.get("/healthz", status_code=200)
async def healthz():
    duration = datetime.datetime.now() - startedAt
    if duration.seconds < 10:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_code=status_code, content=f"Application is not healthy. duration: {duration}")
    return {"message": f"Healthy application. duration: {duration}"}