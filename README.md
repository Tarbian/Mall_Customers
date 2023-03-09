# Description of the project
This project is an API service for predicting a cluster of store customers using a trained clustering model.

## Installation and launch of the project
1. Clone the repository to your computer: `git clone https://github.com/Tarbian/Mall_Customers.git`
2. Go to the project folder: `cd Mall_Customers`
3. Install all necessary dependencies: `pip install -r requirements.txt`
4. Run the main.py file: `python main.py`
5. Enter the required data and perform a POST request to the `/predict` path
6. Get the result from the service API

## Usage
The API service supports POST requests to the `/predict` path with mandatory data input in the form of a JSON object with the following fields (examples in the folder `tests`):

* male: gender of the client (male - 1, female - 0);
* age: age of the client (18 - 80);
* income: the client's income level;
* score: evaluation of the client's purchases (0 - 100).

Example request:

```json
{
   "male": 1,
   "age": 25,
   "income": 50000,
   "score": 80
}
```
The API service will return a JSON object with one field. Example answer:

```json
{
   "cluster": 2
}
```

### Process
You can view the model creation process, some graphs, or make your changes in the Jupiter-notebook in the `notebooks` folder.

### License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
