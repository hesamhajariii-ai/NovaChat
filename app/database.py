/storage/emulated/0 $ ls -l /storage/emulated/0/NovaChat
total 51966
drwxrwx---   11 root     everybod      3488 Jul 17 17:26 app-rw-rw----    1 root     everybod  35738612 Jul 17 16:46 cloudflared
drwxrwx---    2 root     everybod      3488 Jul 17 17:17 database
-rw-rw----    1 root     everybod     20480 Jul 17 15:20 novachat.db
-rw-rw----    1 root     everybod  17364019 Jul 17 17:04 novachat.tar.gz
-rw-rw----    1 root     everybod        40 Jul 17 15:15 requirements.txt
-rw-rw----    1 root     everybod        48 Jul 17 15:15 start.sh
drwxrwx---    4 root     everybod      3488 Jul 17 13:01 static
drwxrwx---    2 root     everybod      3488 Jul 17 14:22 templates
-rw-rw----    1 root     everybod       104 Jul 17 15:31 tunnel.py
/storage/emulated/0 $ ls -l /storage/emulated/0/NovaChat/apptotal 60
-rw-rw----    1 root     everybod         0 Jul 17 15:19 __init__.py
drwxrwx---    2 root     everybod      3488 Jul 17 15:19 __pycache__
drwxrwx---    2 root     everybod      3488 Jul 17 12:24 apidrwxrwx---    3 root     everybod      3488 Jul 17 15:18 database
drwxrwx---    3 root     everybod      3488 Jul 17 17:26 database.py
-rw-rw----    1 root     everybod      1929 Jul 17 15:19 main.py
drwxrwx---    2 root     everybod      3488 Jul 17 12:24 models
-rw-rw----    1 root     everybod     20480 Jul 17 14:46 novachat.db
-rw-rw----    1 root     everybod      1441 Jul 17 15:14 requirements.txt
drwxrwx---    3 root     everybod      3488 Jul 17 15:20 routes
drwxrwx---    2 root     everybod      3488 Jul 17 12:59 static
drwxrwx---    2 root     everybod      3488 Jul 17 12:58 templates
drwxrwx---    2 root     everybod      3488 Jul 17 12:24 websocket
/storage/emulated/0 $ cat /storage/emulated/0/NovaChat/app/database.py
cat: read error: Is a directory
/storage/emulated/0 $ ls -l /storage/emulated/0/NovaChat/app/database.py
total 4
drwxrwx---    2 root     everybod      3488 Jul 17 17:26 New folder
/storage/emulated/0 $ rm -rf /storage/emulated/0/NovaChat/app/database.py
/storage/emulated/0 $ ls -l /storage/emulated/0/NovaChat/apptotal 56
-rw-rw----    1 root     everybod         0 Jul 17 15:19 __init__.py
drwxrwx---    2 root     everybod      3488 Jul 17 15:19 __pycache__
drwxrwx---    2 root     everybod      3488 Jul 17 12:24 apidrwxrwx---    3 root     everybod      3488 Jul 17 15:18 database
-rw-rw----    1 root     everybod      1929 Jul 17 15:19 main.py
drwxrwx---    2 root     everybod      3488 Jul 17 12:24 models
-rw-rw----    1 root     everybod     20480 Jul 17 14:46 novachat.db
-rw-rw----    1 root     everybod      1441 Jul 17 15:14 requirements.txt
drwxrwx---    3 root     everybod      3488 Jul 17 15:20 routes
drwxrwx---    2 root     everybod      3488 Jul 17 12:59 static
drwxrwx---    2 root     everybod      3488 Jul 17 12:58 templates
drwxrwx---    2 root     everybod      3488 Jul 17 12:24 websocket
/storage/emulated/0 $ touch /storage/emulated/0/NovaChat/app/database.py
/storage/emulated/0 $ from sqlalchemy import create_engine
.orm import sessionmaker

DATABASE_URL = "sqlite:///./novachat.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)sh: from: not found
/storage/emulated/0 $ from sqlalchemy.orm import sessionmaker
sh: from: not found
/storage/emulated/0 $
/storage/emulated/0 $ DATABASE_URL = "sqlite:///./novachat.db"
sh: DATABASE_URL: not found
/storage/emulated/0 $
/storage/emulated/0 $ engine = create_engine(
sh: syntax error: unexpected "("
/storage/emulated/0 $     DATABASE_URL,
sh: DATABASE_URL,: not found
/storage/emulated/0 $     connect_args={"check_same_thread": False}
sh: False}: not found
/storage/emulated/0 $ )
sh: syntax error: unexpected ")"
/storage/emulated/0 $
/storage/emulated/0 $ SessionLocal = sessionmaker(
sh: syntax error: unexpected "("
/storage/emulated/0 $     autocommit=False,
/storage/emulated/0 $     autoflush=False,
/storage/emulated/0 $     bind=engine
/storage/emulated/0 $ )
sh: syntax error: unexpected ")"
/storage/emulated/0 $