import sys
import json
import subprocess
import time


def JenkinsCreateDeployJob(MasterFolder,domain):

    with open('input/admin.json') as adminjson:
        admindata = json.load(adminjson)

    targetserver = admindata[domain]['admin']
    drive = admindata[domain]['drive']

    with open('conf\SAPAdapterDeployEarTemplate.txt') as templatedeploy:
        data = templatedeploy.read()
    commanddeploy="paexec.exe \\\\"+targetserver+" "+drive+":\\tibco\\tra\\5.9\\bin\AppManage.exe --propFile "+drive+":\\tibco\\tra\\5.9\\bin\AppManage.tra -deploy -ear "+drive+":\Deploy_Check\\"+domain+"\SAMPLEAAR.ear -deployConfig "+drive+":\Deploy_Check\\"+domain+"\SAMPLEAAR_"+domain+".xml -app DEPLOY_CHECK/SAMPLEAAR -cred "+drive+":\Deploy_Check\\"+domain+"\\"+domain+"_cred.txt -domain "+domain+" -nostart"
    print(commanddeploy)
    data = data.replace("DEPLOYEARCOMMAND",commanddeploy)
    print(data)
    deployjobxml = "output/SAPAdapterDeploy_"+domain+".xml"
    with open(deployjobxml,'w') as writer:
        writer.write(data)

    CommandDeployJob = "java -jar Lib\jenkins-cli.jar -s http://xsnw50f525a:8080/ create-job Deploy_Check/"+MasterFolder+"/"+domain+"/SAPAdapterDeployEar --username admin --password admin <output/SAPAdapterDeploy_"+domain+".xml"
    print(CommandDeployJob)
    subprocess.Popen(CommandDeployJob,stdout=subprocess.PIPE, shell=True)



