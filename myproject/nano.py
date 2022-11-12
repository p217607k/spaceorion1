# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/genorion1_firebase_notification
# ExecStart=/home/ubuntu/pkenv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           myproject.wsgi:application

# [Install]
# WantedBy=multi-user.target



# ##### proj
# # server {
# #     listen 80;
# #     server_name   3.110.204.181;

# #     location = /favicon.ico { access_log off; log_not_found off; }


# #     location / {
# #         include proxy_params;
# #         proxy_pass http://unix:/run/gunicorn.sock;
# #     }
# # }






