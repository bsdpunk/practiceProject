#!/bin/bash - 
#===============================================================================
#
#          FILE: start.sh
# 
#         USAGE: ./start.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 11/13/2021 17:16
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
mysql --user='root' --password='Qapla1999' -h 192.168.1.94 --execute "CREATE USER 'dusty'@'%' IDENTIFIED BY 'Qapla1984';"
mysql --user='root' --password='Qapla1999' -h 192.168.1.94 --execute "GRANT ALL PRIVILEGES ON government.* TO 'dusty'@'%';"
mysql --user='root' --password='Qapla1999' -h 192.168.1.94 --execute "FLUSH PRIVILEGES;"
mysql --user='root' --password='Qapla1999' -h 192.168.1.94 --execute "CREATE DATABASE government;"
python table.py
#alembic init alembic
#sed -i 's/driver:\/\/user:pass@localhost\/dbname/mysql+pymysql:\/\/root:Qapla1999@192\.168\.1\.94\/government/' alembic.ini
#BASELINE=$( alembic revision -m "baseline" | grep -o "[A-z0-9]\+_baseline" | sed 's/_baseline//' )
#echo $BASELINE
#cat ctable.txt > alembic/versions/${BASELINE}_baseline.py
