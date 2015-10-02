# andractor
Django app to extract any Android App's permission from the AndroidManifest.xml file

Ever wanted to reverse engineer an Android App to get the User's permission from the AndroidManifest.xml file?  Well, you could
do it using Andractor!

Installation guidelines:

1) Please install androguard, django_rq and other dependencies listed in the requirements.txt file.

    Example: pip install androguard


2)  Once you've cloned the app, open the settings.py file in djandroid folder.
    Edit the database settings as per your requirements. 
    Example(MySQL):
    
    Just use the following settings
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
              }
                }
                
    Do not forget to edit the NAME and USER/PASSWORD, which is the DB NAME when you use MySQL
    
3)  As this app uses Django_rq to run the apk decompiler as a background task, just open a new terminal and type:
    
    python manage.py rqworker low
    
    "low" is the name of the worker defined in the RQ_QUEUES 
    (Remember to start your redis server before running this app, using the $ redis-server command)
    
4)  I have provided a supervisor file called droid.conf to automate the task of running the workers on the system start.
    Just copy the file into the /etc/supervisor/conf.d/ folder to run it.
    
5)  Lastly, just run the following command in a new terminal
    
    python manage.py runserver
    
    
Just upload the .apk file of any app and view the app's permissions easily!

Have fun!
    

    
