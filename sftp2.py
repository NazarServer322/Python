from bcrypt import re
import pysftp as sftp
import os
FTP_HOST = "www.sftp.com"
FTP_USER = "user"
FTP_PASS = "superpass"

cnopts = sftp.CnOpts()
cnopts.hostkeys = None
dirs = os.chdir("C:\\")
listdir = os.listdir(dirs)
for x in listdir:
    if x.startswith("sql"):
        path = os.path.join(x)
with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
   print("Connection succesfully stablished ... ")
   x = sftp.listdir('/PositionEngine/')
   putthere = sftp.put_r(path, '/PositionEngine/', preserve_mtime=True)
