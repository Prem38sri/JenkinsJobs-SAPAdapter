import sys
import json
import subprocess



def JenkinsCreateUndeployJob(MasterFolder,domain):

    with open('input/admin.json') as adminjson:
        admindata = json.load(adminjson)

    targetserver = admindata[domain]['admin']
    drive = admindata[domain]['drive']

    with open("conf\SAPAdapterundeployEarTemplate.txt") as templateundeploy:
        data = templateundeploy.read()
    commandundeploy="paexec.exe \\\\"+targetserver+" "+drive+":\\tibco\\tra\\5.9\\bin\AppManage.exe --propFile "+drive+":\\tibco\\tra\\5.9\\bin\AppManage.tra -undeploy -app DEPLOY_CHECK/SAMPLEAAR -cred "+drive+":\Deploy_Check\\"+domain+"\\"+domain+"_cred.txt -domain "+domain
    print(commandundeploy)
    data = data.replace("UNDEPLOYEARCOMMAND",commandundeploy)
    print(data)
    undeployjobxml = "output/SAPAdapterUndeploy_"+domain+".xml"
    with open(undeployjobxml,'w') as writer:
        writer.write(data)

    CommandUneployJob = "java -jar Lib\jenkins-cli.jar -s http://xsnw50f525a:8080/ create-job Deploy_Check/"+MasterFolder+"/"+domain+"/SAPAdapterUndeploy --username admin --password admin <output/SAPAdapterUndeploy_"+domain+".xml"
    print(CommandUneployJob)
    subprocess.Popen(CommandUneployJob,stdout=subprocess.PIPE, shell=True)



