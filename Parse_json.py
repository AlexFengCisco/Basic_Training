'''
Created on Jun 6, 2016

@author: AlexFeng
'''

import json
text='''{"limits":{"mem":512,"disk":1024,"fds":16384},"application_version":"5f835b02-2f2e-4ad7-8c7b-5e833e478e53","application_name":"ciscotest","application_uris":["ciscotest.cisco.mopaas.com"],"version":"5f835b02-2f2e-4ad7-8c7b-5e833e478e53","name":"ciscotest","space_name":"Default Space","space_id":"2ad2df7f-effe-410a-be26-ff285df75431","uris":["ciscotest.cisco.mopaas.com"],"users":null,"instance_id":"a561d7254ff44db2bd5b94bc9e916ff8","instance_index":0,"host":"0.0.0.0","port":61032,"started_at":"2016-06-05 15:18:00 -0700","started_at_timestamp":1465165080,"start":"2016-06-05 15:18:00 -0700","state_timestamp":1465165080}'''
text1='''{"MySQL-5.5":[
              {"name":"MYSQL",
               "label":"MySQL-5.5",
               "tags":["Database",
               "relation","MySQL"],
               "plan":"MySQL free",
               "credentials":{"port":"3306",
                              "username":"494c2c47-96f1",
                              "host":"188.168.10.120",
                              "name":"d5c71c15f684c44819834f1b32ab73f5e",
                              "hostname":"188.168.10.120",
                              "user":"494c2c47-96f1",
                              "password":"d24d9143-3a8e",
                              "uri":"mysql://494c2c47-96f1:d24d9143-3a8e@188.168.10.120:3306/d5c71c15f684c44819834f1b32ab73f5e"
                             }
              }
             ]
}'''

textjson=json.loads(text1)

#print type(str(type(textjson)))
#print textjson
print textjson['MySQL-5.5'][0]['credentials']
print textjson['MySQL-5.5'][0]['credentials']['host']
print textjson['MySQL-5.5'][0]['credentials']['user']
print textjson['MySQL-5.5'][0]['credentials']['password']
print textjson['MySQL-5.5'][0]['credentials']['name']
print type(textjson['MySQL-5.5'][0])