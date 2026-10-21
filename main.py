from fastapi import FastAPI

app = FastAPI()  # This must be named "app"


from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)



#para rodar o código, executar no terminal: uvicorn main:app --reload