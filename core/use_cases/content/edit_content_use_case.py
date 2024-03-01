from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface


class EditContentUseCase:
    def __init__(self, content_implementation: ContentInterface):
        self.content_implementation = content_implementation
    def run(self, content: Content, content_id: int):
        return self.content_implementation.edit_content(content, content_id)