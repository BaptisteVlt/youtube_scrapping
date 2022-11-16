import unittest

from function_scrapping_bva import *

class testInfo(unittest.TestCase):
    def test_info_scrap(self):
        data = {'titre' : ['TikTok vous manipule, voici pourquoi.'],'chaine' : ['Defend Intelligence'], 'description' : [''], 'videos_id' : ['IXxRtYhALRk'], 'external_link' : [''], 'likes' : ['']}
        result = scrapping_ytb(['IXxRtYhALRk&t=10s'])
        self.assertEqual(result['titre'], data['titre'])
        self.assertEqual(result['chaine'], data['chaine'])
        # self.assertEqual(result['description'], data['description'])
        self.assertEqual(result['videos_id'], data['videos_id'])
        # self.assertEqual(result['external_link'], data['external_link'])
        # self.assertEqual(result['likes'], data['likes'])


if __name__ == '__main__':
    unittest.main()