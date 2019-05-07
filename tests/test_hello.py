from flask import Flask
from flask_testing import TestCase
from flask_testing import LiveServerTestCase
import urllib2
import requests

class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True

        # Set to 0 to have the OS pick the port.
        app.config['LIVESERVER_PORT'] = 0
        return app

    def test_server_is_up_and_running(self):
        r = requests.get("http://www.baidu.com")
        self.assertEqual(r.status_code, 200)