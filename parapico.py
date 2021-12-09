import paramiko
hostname = '13.49.240.128' 
myuser   = 'ubuntu'
mySSHK   = 'C:\\Users\\Admin\\Desktop\\IT_STEP\\Laptop.pem'
sshcon   = paramiko.SSHClient()  
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
try:
    sshcon.connect(hostname, username=myuser, key_filename=mySSHK)
except Exception as error:
    print(error) 
stdin, stdout, stderr = sshcon.exec_command("cd ~/Nazar && pwd && mkdir testdir && cd /testdir && ls")
result = stdout.read().splitlines()
print(result)

