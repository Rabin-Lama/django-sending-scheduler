# django-sending-scheduler
Implements a sending scheduler that sends emails at scheduled times.

### **Local setup**
#### **Prerequisite**:
1. Redis should be installed and running on `127.0.0.1:6379`


#### **Follow the steps below to locally set up the project.**

Also, note that commands below are not guaranteed to work in all scenarios. These are just to give you a picture of what you should be doing.
1. Clone the project (`git clone git@github.com:Rabin-Lama/django-sending-scheduler.git`)
2. Change directory (`cd django-sending-scheduler`)
3. Create virtual enviroenment (`virtualenv venv`)
4. Activate the virtual environment (`source venv/bin/activate`)
5. Install dependencies (`pip install -r requirements.txt`)
6. Migrate db (`python manage.py migrate`)
7. Load data from fixtures (`python manage.py loaddata baz/fixtures/*.json`)
8. Create django superuser (`python manage.py createsuperuser`)
9. Run server (`python manage.py runserver`)
10. Start celery in a new terminal (`celery -A sending_scheduler worker -l info`)
11. Start celery beat in a new terminal (`celery -A sending_scheduler beat -l info`)


#### **Config**
1. In the settings file, set `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to your gmail username and password. 
2. Make sure that you enable `Acess for less secure apps` option in your gmail account settings. Visit https://www.google.com/settings/security/lesssecureapps to change it.

### **Run scheduler**
To run a scheduler, go to django admin and add an entry in `Schedule bazingas` table.
