
import re
import jenkins
def getbulidnumber(number):
    server = jenkins.Jenkins('https://jenkins58080', username='user', password='das7')
    user = server.get_whoami()
    version = server.get_version():
    last_build_number = server.get_job_info(f'{number}')['lastCompletedBuild']['number']
    numberreturn = last_build_number
    return numberreturn
 
    