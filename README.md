# To start mongoDB

docker-compose up -d

## To start the API

python -m venv venv

source venv/bin/activate

pip3 install -re requierments.txt

uvicorn app.main:app --reload

## To start scrapping

python -m venv venv

source venv/bin/activate

pip3 install -re requierments.txt

python3 app/scrap_most_wanted.py
