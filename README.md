# maSell

# Tutorial
install virtualenv

open terminal in project


# create venv 
# WIINDOWS
python -m venv venv


.\venv\Scripts\activate


# Linux


virtualenv venv


source venv/bin/activate


# Install the requirements:
pip install -r requirements.txt

# Configure the location of your mysql database on config/db.py:
engine = create_engine("mysql+pymysql://[username]:[password]@[host]:[port]/[schema/dbname]")

# Start the service:
uvicorn main:app --reload
```
