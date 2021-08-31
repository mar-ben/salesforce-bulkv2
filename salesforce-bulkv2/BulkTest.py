import unittest
from Bulk import Bulk
import uuid


class BulkTest(unittest.TestCase):
    # test case method should start with test

    def connect_test_org(self):
        username = 'devTest333@test.com'
        password = 'Summer2021'
        client_id = '3MVG9cHH2bfKACZY.UdaiaV1iQkRaWvS0LsMHIMvtjQdnwxWH_NX0FOrcwQ.R9S33OqmL0OYmhhJ.cRRRVFpz'
        client_secret = '131CC1A5899F0954DCEB043D73611F13C7C730888C2B4AAFD4EF0E386DC9FC42'

        blk = Bulk(client_id, client_secret, username, password, False)
        return blk

    def clear_test_data(self):
        bulk = self.connect_test_org()
        testDataToDelete = bulk.query(
            """select id from contact where lastName like '%test%'""")
        bulk.delete('contact', testDataToDelete)
        print('test data deleted')

    def test_bulkQuery(self):
        bulk = self.connect_test_org()
        results = bulk.query('select id from account limit 2')
        print(results)
        lines = results.split('\n')
        self.assertEqual(len(lines), 4)

    def test_insert(self):
        bulk = self.connect_test_org()
        contactLastName = uuid.uuid4()
        content = """firstName,LastName
        john,{}""".format(contactLastName)
        bulk.insert('contact', content)
        print(content)
        results = bulk.query(
            """select id from contact where name like'%{}%'""".format(contactLastName))
        lines = results.split('\n')
        self.assertEqual(len(lines), 3)

    def test_upsert(self):
        # clear test data
        self.clear_test_data()
        # insert a contact record
        bulk = self.connect_test_org()
        content = """firstName,LastName,Customer_ID__c
        smith,test,X9999998
        """
        bulk.insert('contact', content)
        # upsert the contact record.
        upsertData = """firstName,LastName,Customer_ID__c
        smith,test,X9999998
        will,test,X9999999
        """
        bulk.upsert('contact', 'Customer_ID__c', upsertData)
        # get the count and verify
        query = """select id,name from contact where lastName like '%test%'"""
        result = bulk.query(query)
        print(result)
        lines = result.split('\n')
        print(lines)
        self.assertEqual(len(lines), 4)

    def test_delete(self):
        bulk = self.connect_test_org()
        # Create the test contact record
        testContactLastName = uuid.uuid4()
        content = """firstName,LastName
        smith,{}""".format(testContactLastName)
        bulk.insert('contact', content)

        # Query the test contact record
        query = """select id from contact where lastName='{}'""".format(
            testContactLastName)
        result = bulk.query(query)
        print(result)
        bulk.delete('contact', result)

        result = bulk.query(query)
        lines = result.split('\n')
        print(len(lines))
        # Delete the test contact record
        self.assertEqual(len(lines), 2)


# python3 -m unittest BulkTest.py
if __name__ == '__main__':
    unittest.main()
