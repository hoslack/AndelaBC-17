import urllib2
import json

urlData = 'https://gis.ers.usda.gov/arcgis/rest/services/?f=pjson'

webUrl = urllib2.urlopen(urlData)
if webUrl.getcode() == 200:
    data = webUrl.read()
    json_format = json.loads(data)
    print "THE KIND OF SERVICES OFFERED BY THE ECONOMIC RESEARCH SERVICES"
    print "="*62
    print "Name =>  Type"
    print "-" * 62
    for i in json_format['services']:
        for n in range(0, len(json_format['services'])):
            print json_format['services'][n]['name'], " => ", json_format['services'][n]['type']

else:
    print"No Results. Error Code" + str(webUrl.getcode())
