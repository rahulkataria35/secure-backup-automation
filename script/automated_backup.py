import logging
from backup import backup_database, load_db_config
from encryption import encrypt_file
from upload import upload_to_s3, load_aws_config
import os

# Logging setup
logging.basicConfig(filename='logs/backup_log.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    """Main function to coordinate the backup, encryption, and upload process."""
    try:
        # Load configurations
        db_config = load_db_config('config/db_config.yaml')
        aws_config = load_aws_config('config/aws_config.yaml')
        encryption_key_file = 'config/encryption_key.key'

        # Perform database backup
        backup_file = backup_database(db_config, 'backups')

        # Encrypt the backup file
        encrypted_file = encrypt_file(backup_file, encryption_key_file)

        # Upload the encrypted backup to S3
        upload_to_s3(encrypted_file, aws_config)

        # Clean up backup files
        os.remove(backup_file)
        logging.info("Backup file removed after encryption and upload.")
        
    except Exception as e:
        logging.error(f"An error occurred during the backup process: {e}")
        raise

if __name__ == "__main__":
    main()
