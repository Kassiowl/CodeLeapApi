import dataclasses
import datetime
import json

from django.http import HttpResponse, JsonResponse, QueryDict
from core.use_cases.content.get_all_contents_use_case import GetAllContentsUseCase
from core.use_cases.content.get_content_use_case import GetContentUseCase
from core.use_cases.content.delete_content_use_case import DeleteContentUseCase
from core.use_cases.content.edit_content_use_case import EditContentUseCase
from core.entities.content import Content

from core.implementation.ContentSqlLiteImpl import ContentSqlLiteImpl
from core.use_cases.content.send_content_use_case import SendContentUseCase

from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
def get_all_contents(request):
   content_implementation = ContentSqlLiteImpl()
   get_all_content_use_case = GetAllContentsUseCase(content_implementation)
   content_list = get_all_content_use_case.run()
   content_dict_list = [dataclasses.asdict(content) for content in content_list]
   return JsonResponse({"data":content_dict_list}, status=200, json_dumps_params={'separators': (',', ':')})

@api_view(['GET'])
def get_content(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'BAD REQUEST'}, status=400)
    
    content_id = int(request.data['id'])
    content_implementation = ContentSqlLiteImpl()
    get_content_use_case = GetContentUseCase(content_implementation)
    content = get_content_use_case.run(content_id)
    if(content is None):
        return JsonResponse({'error': 'NOT FOUND'}, status=404)
    content_dict = dataclasses.asdict(content)

    
    return JsonResponse({"data":content_dict}, status=200, json_dumps_params={'separators': (',', ':')})



@csrf_exempt
@api_view(['DELETE'])
def delete_content(request):

    if request.method != 'DELETE':
        return JsonResponse({'error': 'BAD REQUEST'}, status=400)
    
    content_id = int(request.data['id'])

    if not content_id:
        return JsonResponse({'error': 'All fields must be filled'}, status=400)
    

    content_implementation = ContentSqlLiteImpl()
    delete_content_use_case = DeleteContentUseCase(content_implementation)
    
    is_content_deleted = delete_content_use_case.run(content_id)
    
    if(is_content_deleted):
        return JsonResponse({'content_deleted':'true'})
    return JsonResponse({'Server error': 'false'}, status=500)


@csrf_exempt
@api_view(['PATCH'])
def edit_content(request):

    if request.method != 'PATCH':
        return JsonResponse({'error': 'BAD REQUEST'}, status=400)
    
    title = request.data['title']
    author = request.data['username']
    content = request.data['content']
    content_id = int(request.data['id'])

    if not all([title, author, content]):
        return JsonResponse({'error': 'All fields must be filled'}, status=400)
    
    date_now = datetime.datetime.now()

    content = Content(title, content, author, date_now)
    content_implementation = ContentSqlLiteImpl()
    edit_content_use_case = EditContentUseCase(content_implementation)
    
    is_content_edited = edit_content_use_case.run(content, content_id)

    if(is_content_edited):
        return JsonResponse({'content_edit':'true'})
    return JsonResponse({'Server error': 'false'}, status=500)

@csrf_exempt 
def send_content(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'BAD REQUEST'}, status=400)
    
    post_body_json_request = json.loads(request.body)

    title = post_body_json_request['title']
    author =  post_body_json_request['username']
    content =  post_body_json_request['content']

    if not all([title, author, content]):
        return JsonResponse({'Server error': 'All fields must be filled'}, status=400)
    
    date_now = datetime.datetime.now()

    content = Content(title, content, author, date_now)
    content_implementation = ContentSqlLiteImpl()
    send_content_use_case = SendContentUseCase(content_implementation)
    
    content_send = send_content_use_case.run(content)

    
    if(content_send):
        return JsonResponse({'send_content':'true'})
    return JsonResponse({'send_content': 'false'}, status=500)