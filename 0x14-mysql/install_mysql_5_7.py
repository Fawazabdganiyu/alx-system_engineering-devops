#!/usr/bin/python3
# Install mysql 5.7 on web server
from fabric.api import env, put, run, cd

env.hosts = ['54.197.78.222', '18.210.16.208']
env.user = "ubuntu"


def install():
    """ Install mysql 5.7 """
    put("install_mysql_5_7.sh", "~/")
    with cd("~/"):
        run("chmod +x install_mysql_5_7.sh")
        run("./install_mysql_5_7.sh")


def version():
    """ Check mysql installed version """
    run("mysql --version")


def create_user():
    """ Create a new user """
    put("./create_holberton_user.sql", "~/")
    with cd("~/"):
        run("cat create_holberton_user.sql | mysql -hlocalhost -uroot -p")


def confirm_user():
    """ Confirm the created user and his privileges """
    run("mysql -uholberton_user -p -e \"SHOW GRANTS FOR 'holberton_user'@'localhost'\"")
