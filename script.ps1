# Crear un entorno virtual
virtualenv venv

# Activar el entorno virtual
.\venv\Scripts\activate

# Instalar Django
pip install django

# Instalar Django REST framework
pip install djangorestframework

# Instalar Django CORS headers
pip install django-cors-headers

# Instalar dnspython
pip install dnspython

# Instalar Djongo
pip install djongo

# Instalar pytz
pip install pytz

# Instalar pymongo
pip install pymongo==3.12.1

# Instalar sqlparse
pip install sqlparse==0.2.4

# Crear un proyecto Django
django-admin startproject coreAPI .

# Crear una aplicación Django
python manage.py startapp API
