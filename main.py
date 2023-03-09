from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from uvicorn import run
from warnings import filterwarnings

# filter out the warning message
filterwarnings("ignore", message="X does not have valid feature names, but StandardScaler was fitted with feature names")

app = FastAPI()

# load the model and scaler
kmeans = load('models/kmeans_model.pkl')
scaler = load('models/scaler.pkl')

# define input data model
class DataInput(BaseModel):
    male: int
    age: int
    income: int
    score: int

# define output data model
class DataOutput(BaseModel):
    cluster: int

# define predict endpoint
@app.post('/predict', response_model=DataOutput)
def predict(data: DataInput):
    scaled_data = scaler.transform([[data.male, data.age, data.income, data.score]])
    cluster = kmeans.predict(scaled_data)
    #print(f'\nCluster № {cluster[0]}\n')
    return {'cluster': cluster}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)