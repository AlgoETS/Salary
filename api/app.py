from fastapi import FastAPI, Request, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import pandas as pd
import json

# Initialize FastAPI and Jinja2
app = FastAPI(docs_url="/docs", redoc_url=None)

current_directory = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(current_directory, "templates"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(request: Request):
    return "Salary API"

@app.get("/load_pickle/2023")
async def salary_2023():
    # Path to the pickle file
    pickle_path = os.path.join("..", "data", "pickle", "salary_guide_2023.pkl")
    
    try:
        # Load the pickle file into a pandas DataFrame
        df = pd.read_pickle(pickle_path)
        
        # Convert the DataFrame to JSON
        return json.loads(df.to_json(orient="split"))
    except Exception as e:
        return {"error": str(e)}

@app.get("/salary/2024")
async def salary_2024():
    # Corrected the typo here
    pickle_path = os.path.join("..", "data", "pickle", "salary_guide_2024_1.pkl")
    
    try:
        # Load the pickle file into a pandas DataFrame
        df = pd.read_pickle(pickle_path)
        
        # Convert the DataFrame to JSON
        return json.loads(df.to_json(orient="split"))
    except Exception as e:
        return {"error": str(e)}
