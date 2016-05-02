from django.test import TestCase
from rest_framework.test import APIClient
from stud.models import Student, Group



class TestStud():
	client = APIClient()
	g = client.post('/groupsAPI/', {'groupname': 'lrk3h5f4'}, format='json') 
	group = Group.objects.all().last().id	
	e = client.put('/groupsAPI/' + str(group) + '/', {'groupname': 'lr4k5f3h'}, format='json')
	c = client.post('/studentsAPI/', {'name': 'lrk3h5f4', 
		'date': '1996-2-29', 'num': '3737', 'group': group}, format='json')
	stud = Student.objects.all().last().id
	p = client.put('/studentsAPI/' + str(stud) + '/', {'name': 'h5fk34lr', 
		'date': '1993-8-12', 'num': '7373', 'group': group}, format='json')
	d = client.delete('/studentsAPI/' + str(stud) + '/', format='json')
	r = client.delete('/groupsAPI/' + str(group) + '/', format='json')


class Group_Student_Test(TestCase):
	def test_add_group_form(self):
		g = TestStud().g
		self.assertEqual(g.status_code, 201) 
	def test_edit_group_form(self):
		e = TestStud().e
		self.assertEqual(e.status_code, 200) 
	def test_add_student_form(self):
		c = TestStud().c
		self.assertEqual(c.status_code, 201)
	def test_edit_student_form(self):
		p = TestStud().p
		self.assertEqual(p.status_code, 200)
	def test_del_student(self):
		d = TestStud().d
		self.assertEqual(d.status_code, 204)
	def test_del_group(self):
		r = TestStud().r
		self.assertEqual(r.status_code, 204)      


class Auth_Test(TestCase):
    def test_auth(self):
        response = self.client.post('/', {'username': 'admin', 'password': '5t5t5t5t'})
        self.assertEqual(response.status_code, 200) 