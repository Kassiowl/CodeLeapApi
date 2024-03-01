from abc import ABC, abstractmethod

from core.entities.content import Content


class ContentInterface(ABC):
    @abstractmethod
    def send_content(content: Content) -> bool:
        pass
    def edit_content(content: Content, content_id: int) -> bool:
        pass
    def delete_content(content_id: int) -> bool:
        pass
    def get_content(content_id: int) -> Content:
        pass