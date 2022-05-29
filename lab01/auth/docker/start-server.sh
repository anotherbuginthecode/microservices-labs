echo "Running migrate..."
python manage.py migrate

# if superuser already exist the instruction failed warning about that
# whitout blocking the process
# echo "Creating superuser..."
# export DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-superadmin@email.com}
# export DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-supersecretpassword}
# python manage.py createsuperuser --no-input

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000