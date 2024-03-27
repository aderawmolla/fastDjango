sudo service postgresql status
sudo service postgresql start
sudo systemctl stop postgresql
sudo -u postgres psql
CREATE USER <username> WITH PASSWORD '<password>';
CREATE DATABASE django_todo OWNER <username>;
deactivate
