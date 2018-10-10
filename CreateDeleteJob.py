import sys
import json
import subprocess



def JenkinsCreateDeleteJob(MasterFolder,domain):

    with open('input/admin.json') as adminjson:
        admindata = json.load(adminjson)

    targetserver = admindata[domain]['admin']
    drive = admindata[domain]['drive']

    with open("conf\SAPAdapterDeleteEarTemplate.txt") as templatedelete:
        data = templatedelete.read()
    commanddelete="paexec.exe \\\\"+targetserver+" "+drive+":\\tibco\\tra\\5.9\\bin\AppManage.exe --propFile "+drive+":\\tibco\\tra\\5.9\\bin\AppManage.tra -delete -app DEPLOY_CHECK/SAMPLEAAR -cred "+drive+":\Deploy_Check\\"+domain+"\\"+domain+"_cred.txt -domain "+domain
    print(commanddelete)
    data = data.replace("DELETEEARCOMMAND",commanddelete)
    print(data)
    deletejobxml = "output/SAPAdapterDelete_"+domain+".xml"
    with open(deletejobxml,'w') as writer:
        writer.write(data)

    Commanddeletejob = "java -jar Lib\jenkins-cli.jar -s http://xsnw50f525a:8080/ create-job Deploy_Check/"+MasterFolder+"/"+domain+"/SAPAdapterDeleteEar --username admin --password admin <output/SAPAdapterDelete_"+domain+".xml"
    print(Commanddeletejob)
    subprocess.Popen(Commanddeletejob,stdout=subprocess.PIPE, shell=True)



