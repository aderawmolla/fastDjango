
sudo -u postgres psql
CREATE USER <username> WITH PASSWORD '<password>';
CREATE DATABASE django_todo OWNER <username>;
