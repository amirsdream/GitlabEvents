import requests
import json

class TestApp:
    endpoint = None
    token = None

    def __init__(self, url, projectId, token):
        self.endpoint = f"http://{url}/api/v4/projects/{projectId}/variables"
        self.token = token

    def readVariable(self, variable):
        print (f"{self.endpoint}/{variable}")
        try:
            response = requests.get(url=f"{self.endpoint}/{variable}",headers={"PRIVATE-TOKEN":f"{self.token}"})
            result = response.json()
            return result["value"]
        except:
            raise Exception("gitlab endpoint is not available")

    def updateVariable(self, variable, value):
        response = requests.put(url=f"{self.endpoint}/{variable}",data={"value":value},headers={"PRIVATE-TOKEN":f"{self.token}"})
        return response.json()

def main():
    testapp = TestApp(url="192.168.0.73", projectId=1, token="8guZLimJTpQ1racFZ5SC" )
    list = testapp.readVariable(variable="test")
    list = json.loads(list)

    sorted_list= {k: v for k, v in sorted(list.items(), key=lambda item: item[1])}

    updated_list = json.dumps(list)
    print(testapp.updateVariable(variable="test",value=updated_list))
    print(testapp.readVariable(variable="test"))

main()