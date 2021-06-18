import unittest
from Bulk import Bulk

class BulkTest(unittest.TestCase):
    #test case method should start with test

    def connect_test_org(self):
        username='devTest333@test.com'
        password='Summer2021'
        client_id='3MVG9cHH2bfKACZY.UdaiaV1iQkRaWvS0LsMHIMvtjQdnwxWH_NX0FOrcwQ.R9S33OqmL0OYmhhJ.cRRRVFpz'
        client_secret='131CC1A5899F0954DCEB043D73611F13C7C730888C2B4AAFD4EF0E386DC9FC42'
        blk=Bulk(client_id,client_secret,username,password,False)
        return blk

    def test_bulkQuery(self):
        bulk=self.connect_test_org()
        results=bulk.query('select id from account limit 2')
        print(results)
        lines=results.split('\n')
        self.assertEqual(len(lines),4)
    #def test_insert(self):
    #    bulk=self.connect_test_org()
    #    contact_data="""firstName,LastName
    #    Parker,Smith"""
    #    bulk.insert('contact',contact_data)
        


if __name__ == '__main__':
    unittest.main()

