import requests
import json

class GetRequester:
    

    def __init__(self, url):
        self.url = url
        

    def get_response_body(self):
        response = request.get(self.url)
        return response.text

    def load_json(self):
        python_list = []
        list_members = json.loads(self.get_response_body())
        for list_member in list_members:
            python_list.append(list_member['name'])

        return python_list 
        
        
        