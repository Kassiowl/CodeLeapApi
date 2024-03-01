import datetime
from pytest import fixture
import pytest
from core.use_cases.content.delete_content_use_case import DeleteContentUseCase
from core.use_cases.content.edit_content_use_case import EditContentUseCase
from core.use_cases.content.get_all_contents_use_case import GetAllContentsUseCase

from core.use_cases.content.get_content_use_case import GetContentUseCase
from core.entities.content import Content
from core.use_cases.content.send_content_use_case import SendContentUseCase

from core.implementation.ContentSqlLiteImpl import ContentSqlLiteImpl


@fixture
def content_implementation():
    content_implementation = ContentSqlLiteImpl()
    return content_implementation


def test_send_content(content_implementation):
    datetime_creation = datetime.datetime(2020, 5, 17)
    content_mock = Content('Content Title', 'Content paragraphs', 'Author name', datetime_creation)
    send_content = SendContentUseCase(content_implementation)
    is_content_send = send_content.run(content_mock)
    assert is_content_send == True

def test_get_content(content_implementation):
    get_content_use_case = GetContentUseCase(content_implementation)
    content = get_content_use_case.run(1)
    expected_datetime_creation = '2020-05-17 00:00:00'
    expected_content = Content('Content Title', 'Content paragraphs', 'Author name', expected_datetime_creation)
    assert content == expected_content

def test_get_all_contents(content_implementation):
    get_all_contents_use_case = GetAllContentsUseCase(content_implementation)
    all_contents = get_all_contents_use_case.run()
    assert(isinstance(all_contents, list))

def test_edit_content(content_implementation):
 expected_datetime_creation = '2020-05-17 00:00:00'
 content_modify_mock = Content('Content Title', 'Content paragraphs', 'Author name', expected_datetime_creation)
 edit_content_use_case = EditContentUseCase(content_implementation)
 is_content_edited = edit_content_use_case.run(content_modify_mock, 1)
 assert(is_content_edited == True)

def test_delete_content(content_implementation):
   delete_content_use_case = DeleteContentUseCase(content_implementation)
   is_content_deleted = delete_content_use_case.run(1)
   assert(is_content_deleted == True)