from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface


class GetContentUseCase:
    def __init__(self, content_implementation: ContentInterface):
        self.content_implementation = content_implementation
    def run(self, content_id: int):
        return self.content_implementation.get_content(content_id)