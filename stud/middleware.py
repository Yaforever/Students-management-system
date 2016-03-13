# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import connection


class TimeAndSqlMiddleware(object):
	def process_request(self, request):
		request.request_time = datetime.now()

	def process_response(self, request, response):
		time = request.request_time
		q = connection.queries
		count = 0
		for i in q:
			if i: count += 1
		response_time = datetime.now() - request.request_time
		response.content = response.content.replace('</body>', 
			'<p>время выполнения запроса: {0}:{1}:{2}</p> <p>длительность выполнения запроса: \
			{3} sec</p> <p>sql-запросов: {4}</p> \
			</body>'.format(time.hour, time.minute, time.second, response_time.total_seconds(), count))
		return response




