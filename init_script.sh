#!/bin/sh
cd src
mysql -h "localhost" -u "root" "-proot" "dat210_statistics" < "db_init.sql"
python db/db_filler.py