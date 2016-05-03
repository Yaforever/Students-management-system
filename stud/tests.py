from django.test import TestCase
from rest_framework.test import APIClient
from stud.models import Student, Group



class TestStud():

	client = APIClient()
	addgroup = client.post('/groupsAPI/', {'groupname': 'lrk3h5f4'}, format='json') 
	group = Group.objects.all().last().id	
	editgroup = client.put('/groupsAPI/' + str(group) + '/', {'groupname': 'lr4k5f3h'}, format='json')
	addstudent = client.post('/studentsAPI/', {'name': 'lrk3h5f4', 
		'date': '1996-2-29', 'num': '3737', 'group': group}, format='json')
	stud = Student.objects.all().last().id
	editstudent = client.put('/studentsAPI/' + str(stud) + '/', {'name': 'h5fk34lr', 
		'date': '1993-8-12', 'num': '7373', 'group': group}, format='json')
	delstudent = client.delete('/studentsAPI/' + str(stud) + '/', format='json')
	delgroup = client.delete('/groupsAPI/' + str(group) + '/', format='json')


class Group_Student_Test(TestCase):

	def test_add_group(self):
		addgroup = TestStud().addgroup
		self.assertEqual(addgroup.status_code, 201) 

	def test_edit_group(self):
		editgroup = TestStud().editgroup
		self.assertEqual(editgroup.status_code, 200) 

	def test_add_student(self):
		addstudent = TestStud().addstudent
		self.assertEqual(addstudent.status_code, 201)

	def test_edit_student(self):
		editstudent = TestStud().editstudent
		self.assertEqual(editstudent.status_code, 200)

	def test_del_student(self):
		delstudent = TestStud().delstudent
		self.assertEqual(delstudent.status_code, 204)

	def test_del_group(self):
		delgroup = TestStud().delgroup
		self.assertEqual(delgroup.status_code, 204)      


class Templates_Test(TestCase):

	def test_template_edit(self):
		response = self.client.get('/edit/')
		self.assertTemplateUsed(response, 'edit.html')

	def test_template_base(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'base.html')
