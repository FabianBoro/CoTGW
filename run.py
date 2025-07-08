#ECHO is on.
# run.py
import uvicorn
from app.database import Base, engine
from app import models

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
    Base.metadata.create_all(bind=engine)

