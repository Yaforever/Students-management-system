# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import connection
from django.core.urlresolvers import resolve
import string



class TimeAndSqlMiddleware(object):
	def process_request(self, request):
		request.request_time = datetime.now()

	def process_response(self, request, response):
		if 'groupsAPI' in request.path_info and request.user.is_authenticated() == False \
		or 'studentsAPI' in request.path_info and request.user.is_authenticated() == False:
			response.content = '<div style="font-size: 20px"> \
			Only loged in users have access to the API</div>'
			return response
		
		else:
			time = request.request_time
			q = connection.queries
			count = 0
			for i in q:
				if i: count += 1
			response_time = datetime.now() - request.request_time
			response.content = response.content.replace('</body>', 
				'<p>Time of sql requests execution: {0}:{1}:{2}</p> <p>Duration of sql requests execution: \
				{3} sec</p> <p>Amount of sql requests: {4}</p> \
				</body>'.format(time.hour, time.minute, time.second, response_time.total_seconds(), count))
			return response




