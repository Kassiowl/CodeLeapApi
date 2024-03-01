from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface


class GetAllContentsUseCase:
    def __init__(self, content_implementation: ContentInterface):
        self.content_implementation = content_implementation
    def run(self):
        return self.content_implementation.get_all_contents()