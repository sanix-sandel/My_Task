import os
import json
from jsonschema import validate

if __name__=='__main__':
        

        path1=os.listdir('event')          
       # print(path1)
        path2=os.listdir('schema')
       # print(path2)  
        errors=0
        for filename in path1:
                with open('event/{}'.format(filename)) as file:
                        files=json.load(file)
                        for schema_file in path2:
                                with open('schema/{}'.format(schema_file)) as file_schema:
                                        schema=json.load(file_schema)
                                        try:
                                                validate(instance=files, schema=schema)
                                        except Exception as e:
                                                print("error occured")
                                                #print(e) //To see all the errors occured remove #
                                                errors+=1        
                                                                      

        print("Total number of errors ",errors)       
        print("В итоге ",errors," ошибок")                                 