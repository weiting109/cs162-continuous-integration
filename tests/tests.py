"""
1. POST an HTTP request with a valid expression to the server.
Examine the response and confirm that the correct answer is returned.
2. Establish a connection to the database directly and verify
that the string you sent has been correctly stored in the database.
For this step, you can use SQLAlchemy, or write the SQL directly if you prefer,
however note that this is a postgres database which does have subtly different
syntax from sqlite.  (For simple queries this shouldn't be a big issue.)
3. POST an HTTP request with an invalid expression to the server.
Examine the response and confirm that an error is raised.
4. Confirm that no more rows have been added to the database since the last
valid expression was sent to the server. (For the purposes of this class, you
can assume that no-one else is accessing the database while the tests are
running.)
5. If any of the tests fail, then your program should raise an exception, and
stop running.  Your program should only complete successfully if all tests pass.
"""

import unittest
import requests
from app import Expression
import app

class ComputationServerTest(unittest.TestCase):
    def make_request(self,url,data):
        requests.post(url,data=data)
        return val = Expression.query(value).last()

    def test_HTTPreq(self):
        """Tests for correct value returned"""
        url = "http://{}:8000/add/".format(self.get_docker_host())
        data = {'expression'='5*5'}
        self.assertEqual(make_request(url,data),25)

    def test_invalidHTTPreq(self):
        """Checks for InvalidExpressionError when invalid expression entered"""
        url = "http://{}:8000/add/".format(self.get_docker_host())
        data = {'expression'='5-'}
        self.assertRaises(app.InvalidExpressionError,make_request(url,data))

    def test_dbRows(self):
        """Checks no more rows have been added since the last valid expression"""
        self.assertEqual(Expression.query(id).count(),1)
