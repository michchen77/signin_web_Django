from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User

# Create your tests here.
class ModelTest(TestCase):
    def stUp(self):
        Event.objects.create(id=1,name='oneplus 3 event',status=True,limit=2000,address='shenzhen',start_time='2020-11-11 05:11:22',)
        Guest.objects.create(id=1,event_id=1,realname='ellen',phone='1333333333',email='ellen@qq.com',sign=False)

        def test_event_models(self):
            result = Event.objects.get(name='oneplus 3 event')
            self.assertEqual(result.address,'shenzhen')
            self.assertTrue(result.status)

        def test_guest_models(self):
            result = Guest.objects.get(phone='1333333333')
            self.assertEqual(result.realname,'ellen')
            self.assertFalse(result.sign)


class IndexPageTest(TestCase):
    def test_index_page_renders_index_template(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin2','admin@qq.com','123456')

    def test_add_admin(self):
        # add user
        user = User.objects.get(username='admin2')
        self.assertEqual(user.username,'admin2')
        self.assertEqual(user.email,'admin@qq.com')

    def test_login_action_username_password_null(self):
        test_data = {'username':'','password':''}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'username or password error',response.content)

    def test_login_action_username_password_error(self):
        test_data = {'username':'abc','password':'123'}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error', response.content)

    def test_login_action_success(self):
        test_data = {'username':'admin2','password':'123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code,302)

