
<div align="center">
  <h1>Passport Task</h1>
</div>

- **Clone**: `git clone https://gitlab.com/bakuelectronics/saleor-app.git`
- **After Clone**: `cd task_travel`

- **Create and Activate virtualenv**: `python3 -m venv venv`  **after** `source /venv/bin/activate`

- **Install requiremets**: `pip3 install -r requirements.txt`

- **Create Database** : `docker-compose up --build -d 
`

- **Migrate Database** : `python manage.py makemigrations` **after** `python manage.py migrate`

- **Run Project** : `python manage.py runserver`


