echo "Running migrate..."
python manage.py makemigrations && python manage.py migrate

echo "Creating superuser..."
export DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
export DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD
python manage.py createsuperuser --no-input

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000