from django.test import TestCase


class Login_Test(TestCase):
	def test_login(self):
		response = self.client.post('/', {'username': 'someuser1', 'password': '55555'})
		self.assertEqual(response.status_code, 200) 

class Add_Group_Test(TestCase):
	def test_add_group_form(self):
		response = self.client.post('/edit/',{'groupname': 'newgroup1'}) 
		self.assertEqual(response.status_code, 302) 
        
class Add_Student_Test(TestCase):
	def test_add_student_form(self):
		response = self.client.post('/edit/',{'name': 'Studenko Student Studentovich',
		'date': '1996-2-29','num': '3737','group': 'newgroup1'})
		self.assertEqual(response.status_code, 302)
