# very-simple-animals

A simple python web app to get a animal and one image url from them.

## Install

This code support python 3.6, 3.7 or 3.8

```
 $ python3 -m venv venv
 $ source venv/bin/activate
 $ pip install -r requirements.txt
```

## Configure

In `animals.py` you can modify the list `ANIMALS` with a tuple of ("animal name", "url").

## Run

```
 $ export FLASK_APP=animals.py
 $ flask run
```

## View

Just go "localhost:5000" in a browser

## Nginx + Uwsgi

To run this app as standalone service:

```
$ sudo apt update
$ sudo apt install nginx python3 python3-venv
$ sudo apt-get install build-essential python3-dev git
$ pwd
/home/ubuntu
$ git clone https://github.com/ignacionf/very-simple-animals.git
$ cd very-simple-animals
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install uwsgi
```

Create the file '/etc/systemd/system/animals.service' with:

```
[Unit]
Description=Animal app
Requires=network.target
After=network.target

[Service]
TimeoutStartSec=0
RestartSec=10
Restart=always

WorkingDirectory=/home/ubuntu/very-simple-animals
User=www-data

KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

ExecStart=/home/ubuntu/very-simple-animals/venv/bin/uwsgi --socket localhost:8000 --manage-script-name --mount /=animals:app

[Install]
WantedBy=multi-user.target
```

And run:
```
$ sudo systemctl daemon-reload
$ sudo systemctl enable animals.service
$ sudo systemctl start animals.service
```

Then, in file '/etc/nginx/sites-enabled/default'
```
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	location / { try_files $uri @animalsapp; }
    location @animalsapp{
        include uwsgi_params;
        uwsgi_pass uwsgi://localhost:8000;
    }
}
```

And run:
```
$ sudo nginx -t     # test the config
$ sudo systemctl reload nginx
```

Test enter to the http://<ip>/
