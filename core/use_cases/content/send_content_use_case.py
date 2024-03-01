from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface


class SendContentUseCase:
    def __init__(self, content_implementation: ContentInterface):
        self.content_implementation = content_implementation
    def run(self, content: Content, content_id):
        return self.content_implementation.send_content(content, content_id)