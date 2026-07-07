# main.py
# import sys
# from Frontend.login_ui import main as run_app

# if __name__ == "__main__":
#     print("Starting Edulite Graphical Interface...")
#     run_app()


from fastapi import FastAPI
from database.initialize_db import initialize_database
from Backend.routes.user import router as user_router
from Backend.routes.student import router as student_router

app = FastAPI()


@app.on_event("startup")
def startup():
    initialize_database()

app.include_router(user_router)
app.include_router(student_router)


@app.get("/")
def home():
    return {"message": "EDULite API is running"}