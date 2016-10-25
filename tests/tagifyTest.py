import unittest
from tagify import Stats
from tagify import Tagger


class StatTest(unittest.TestCase):
    def setUp(self):
        self.stats = Stats();

    def tearDown(self):
        self.stats = None

    def test_increase_tag_counter_1(self):
        self.stats.increase_tag_counter_by(-1)
        self.assertEqual(self.stats.tag_counter, -1)

    def test_increase_tag_counter_2(self):
        self.stats.increase_tag_counter_by(9999)
        self.assertEqual(self.stats.tag_counter, 9999)

    def test_increase_tag_counter(self):
        self.stats.increase_tag_counter()
        self.assertEqual(self.stats.tag_counter, 1)

    def test_increase_file_counter(self):
        self.stats.increase_file_counter()
        self.assertEqual(self.stats.file_counter, 1)


class TaggerTest(unittest.TestCase):
    def setUp(self):
        self.stats = Stats();
        self.tagger = Tagger(self.stats);

    def tearDown(self):
        self.stats = None
        self.tagger = None

    def test_wrap_as_xml_1(self):
        tags = ["a", "b", "c"]
        self.assertEqual(self.tagger.wrap_as_xml(tags), "<string>a</string><string>b</string><string>c</string>")

    def test_wrap_as_xml_2(self):
        tags = ["ö'ö", "b,b"]
        self.assertEqual(self.tagger.wrap_as_xml(tags), "<string>ö'ö</string><string>b,b</string>")


if __name__ == '__main__':
    unittest.main()