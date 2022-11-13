
## Before to run the app, Please set up the database.


1. PostgreSQL
   - This app is only for MVP; Minimum Viable Product
   - Please create the database, user and password in your PostgreSQL database
   - postgresql+psycopg2://lw_dev:lionwolf@127.0.0.1:5432/lw_pos
  ```postgresql
  CREATE DATABASE lw_pos;

  CREATE USER lw_dev WITH PASSWORD 'lionwolf';

  GRANT ALL PRIVILEGES ON DATABASE lw_pos TO lw_dev;
  ```

2. Python
   - Create venv and download all the requirements packages
   - Then create tables and seed sample datas using CLI commands
   - In terminal, execute the following
```terminal
python3 -m venv .venv && source .venv/bin/activate

pip install -r requirements.txt

flask db drop && flask db create

flask db seed

flask run
```
