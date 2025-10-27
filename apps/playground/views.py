from rest_framework.views import APIView
from django.core.mail import BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from templated_mail.mail import BaseEmailMessage
import logging
import requests


logger = logging.getLogger(__name__) #playground.views


class HelloView(APIView):
    def get(self, request : HttpRequest) -> HttpResponse:
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Got response from httpbin')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('Could not connect to httpbin')
        return render(request, 'hello.html', {'name' : 'Django'})

# # emails with templates
# def say_hello(request : HttpRequest) -> HttpResponse:
#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={
#                 'name' : 'Django'
#             }
#         )
#         message.send(['a11A@example.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name' : 'Django'})