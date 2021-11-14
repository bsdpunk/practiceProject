#!/bin/bash - 
#===============================================================================
#
#          FILE: clear.sh
# 
#         USAGE: ./clear.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 11/13/21 23:55
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
#rm -rf alembic
#rm -rf alembic.ini
mysql --user='root' --password='Qapla1999' -h 192.168.1.94 --execute "DROP USER 'dusty'@'%' ;"
mysql --user='root' --password='Qapla1999' -h 192.168.1.94 --execute "DROP DATABASE government ;"
