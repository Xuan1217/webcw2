import unittest
from app import app, db
from app.models import *
from config import DB_URI
import json


class LoginCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_login(self):
        client = app.test_client()
        ret = client.post("/Login", data={
            "Lus": "a",
            "Lpw": "a"
        })
        ret2 = client.post("/Login", data={
            "Lus": "a",
            "Lpw": "b"
        })
        resp = ret.data
        resp2 = ret2.data
        resp_j = json.loads(resp)
        resp2_j = json.loads(resp2)
        self.assertIn("code", resp_j)
        self.assertEqual(resp_j["code"], 2)
        self.assertIn("code", resp2_j)
        self.assertEqual(resp2_j["code"], 3)

    def test_empty(self):
        client = app.test_client()
        ret = client.post("/Login", data={
            "Lus": "",
            "Lpw": ""
        })
        resp = ret.data
        resp_j = json.loads(resp)
        self.assertIn("code", resp_j)
        self.assertEqual(resp_j["code"], 1)


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add(self):
        user = User(Username="testing", Password="1234")
        dish = Dishes(dish="testing", price=12, inventory=2)
        db.session.add(user)
        db.session.add(dish)
        db.session.commit()
        t1 = User.query.filter_by(Username="testing").first()
        t2 = Dishes.query.filter_by(dish="testing").first()
        self.assertIsNotNone(t1)
        self.assertIsNotNone(t2)


if __name__ == '__main__':
    unittest.main()
