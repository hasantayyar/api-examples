# Sample Python Application
This is a sample python application for Bitwala rest API.

### Requirements

This app will only work for python 3.x. 
The required pip packages listed in `requirements.txt`

### Configuration

You should set an environment variable name `APP_ENV`. This application will load the configuration file named the value of `APP_ENV`. If there is no `APP_ENV` then `development.conf` will be the default configuration file. 

You have to update the configuration file by adding your api credentials. 

### Run

```
$ export APP_ENV=production
$ python3 app.py
```

By default the application will listen 5000 port. You can test the application at localhost:5000. 
