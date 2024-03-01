from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface
import requests

class ContentToServerImpl(ContentInterface):
    def send_content(content: Content):
        try:
            url = 'https://dev.codeleap.co.uk/careers/'
            json_request = {"username": content.author,"title": content.author, 
                            "content": content.content }
            print(requests.post(url, json = json_request))
            return True
        except:
            return False

    def edit_content(content: Content, content_id):
        try:
            url = f'https://dev.codeleap.co.uk/careers/{content_id}'
            json_request = {"username": content.author,"title": content.author, 
                            "content": content.content }
            print(requests.patch(url, json = json_request))
            return True
        except:
            return False

    def delete_content(self, content_id):
        try:
            url = f'https://dev.codeleap.co.uk/careers/{content_id}'
            json_request = {""}
            print(requests.delete(url, json = json_request))
            return True
        except:
            return False

    def get_contents(self, content_id):
        try:
            url = f'https://dev.codeleap.co.uk/careers/'
            print(requests.get(url))
            return True
        except:
            return False

