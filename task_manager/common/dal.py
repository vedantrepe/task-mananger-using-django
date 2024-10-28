def get_db_credential():
    return {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TASK_MANG_PROJECT',  
        'USER': 'root',  
        'PASSWORD': 'password',  
        'HOST': 'localhost',
        'PORT': '3306'
        }