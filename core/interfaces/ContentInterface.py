from abc import ABC, abstractmethod

from core.entities.content import Content


class ContentInterface(ABC):
    @abstractmethod
    def send_content(content: Content) -> bool:
        pass
    @abstractmethod
    def edit_content(content: Content, content_id: int) -> bool:
        pass
    @abstractmethod
    def delete_content(content_id: int) -> bool:
        pass
    @abstractmethod
    def get_content(content_id: int) -> Content:
        pass
    @abstractmethod
    def get_all_contents() -> list[Content]:
        pass