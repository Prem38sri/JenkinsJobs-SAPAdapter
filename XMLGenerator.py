import sys

def XMLGenerate(domain):

        dcxml = open('conf/deployaar.xml','r')
        inp = open('input/machineaar.cfg','r')
        i = 0
        dcxmldata = dcxml.read()
        for aarmachine in inp:
                aarmachinename = aarmachine.rstrip()
                i = i + 1
                bind = open('conf/bindingaar.xml','r')
                binddata = bind.read()
                binddata = binddata.replace("AARMACHINE",aarmachinename)
                binddata = binddata.replace("AARNUMBER",str(i))
                dcxmldata = dcxmldata.replace('<!-- AARREPLACER -->',binddata)

        finalxml = "output/SAMPLEAAR_"+domain+".xml"
        outputfile = open(finalxml,'w')
        outputfile.write(dcxmldata)
        outputfile.close


        dcxml.close()
        bind.close()
        inp.close()
