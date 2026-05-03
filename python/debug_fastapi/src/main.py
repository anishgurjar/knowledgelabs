from fastapi import FastAPI
from src.routers.customers import customer_router
from src.routers.payments import payments_route
import uvicorn

app = FastAPI()

app.include_router(customer_router)
app.include_router(payments_route)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)