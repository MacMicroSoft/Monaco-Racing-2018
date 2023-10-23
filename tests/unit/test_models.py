import unittest
from peewee import SqliteDatabase
from monaco_racing.models import Start, End, Abbr
import os

db_path = os.path.join(os.path.dirname(__file__), 'database.db')


class TestModels(unittest.TestCase):

    def setUp(self):
        self.db = SqliteDatabase(db_path, pragmas={'journal_mode': 'wal'})
        self.db.connect()
        self.db.create_tables([Start])
        self.db.create_tables([End])
        self.db.create_tables([Abbr])

    def tearDown(self):
        self.db.drop_tables([Start])
        self.db.drop_tables([End])
        self.db.drop_tables([Abbr])

        self.db.close()

    def test_create_and_save_start(self):
        start = Start.create(name_id="test_start", date="2023-10-12", time="12:00:00")

        self.assertIsNotNone(start.id)
        self.assertEqual(start.name_id, "test_start")
        self.assertEqual(start.date, "2023-10-12")
        self.assertEqual(start.time, "12:00:00")

    def test_create_and_save_end(self):
        end = End.create(name_id="test_end", date="2023-10-12", time="12:00:00")

        self.assertIsNotNone(end.id)
        self.assertEqual(end.name_id, "test_end")
        self.assertEqual(end.date, "2023-10-12")
        self.assertEqual(end.time, "12:00:00")

    def test_create_and_save_abbr(self):
        abbr = Abbr.create(name_id="test_abbr", person="William Json", car="Ferrari")

        self.assertIsNotNone(abbr.id)
        self.assertEqual(abbr.name_id, "test_abbr")
        self.assertEqual(abbr.person, "William Json")
        self.assertEqual(abbr.car, "Ferrari")


if __name__ == '__main__':
    unittest.main()
