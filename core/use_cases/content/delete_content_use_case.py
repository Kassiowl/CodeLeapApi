from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface


class DeleteContentUseCase:
    def __init__(self, content_implementation: ContentInterface):
        self.content_implementation = content_implementation
    def run(self, content_id):
        return self.content_implementation.delete_content(content_id)