## Test Shop App

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bekich97/shop_app.git
   ```
2. Create virtual environment with:
   ```sh
   virtualenv venv
   ```
3. Select virtualenv which you created recently, with (in Ubuntu)
   ```sh
   source venv/bin/activate
   ```
4. Install  packages
   ```sh
   pip install -r requirements.txt
   ```
5. Make migrations
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create superuser
   ```sh
   python manage.py createsuperuser
   ```
7. Run server
   ```sh
   python manage.py runserver 8000
   ```

Admin panel: ```http://127.0.0.1:8000/admin```
