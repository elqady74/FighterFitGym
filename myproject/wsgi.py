<<<<<<< HEAD
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

=======
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

>>>>>>> b60a3d5ebed84a802da2556ecaa12a22dfff3aea
application = get_wsgi_application()