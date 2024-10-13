import unittest
from script.backup import backup_database, load_db_config

class TestBackup(unittest.TestCase):

    def test_backup_database(self):
        """Test if the database backup works correctly."""
        db_config = load_db_config('config/db_config.yaml')
        backup_file = backup_database(db_config, 'backups')
        self.assertTrue(backup_file.endswith('_backup.sql'))
        
if __name__ == '__main__':
    unittest.main()
