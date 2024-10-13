# Secure Backup Automation
This project automates the secure backup of database files, encrypts them using a symmetric encryption method, and uploads the encrypted backups to a cloud provider (e.g., AWS S3). It is designed to help organizations securely manage their data backups, ensuring compliance with data privacy standards and preventing unauthorized access to sensitive information.

# Features
- Automated Database Backup: Backs up databases (e.g., MySQL, PostgreSQL) and stores the backups locally.
- Encryption: Encrypts backup files using AES encryption with a securely generated encryption key.
- Cloud Upload: Uploads the encrypted files to AWS S3 for long-term storage.
- Modular Design: Each functionality (backup, encryption, upload) is modular, making the code reusable and extensible.
- Logging: Logs all actions for auditing and troubleshooting.
- Secure Key Management: Handles encryption keys securely.

# Directory Structure

```
secure-backup-automation/
│
├── backups/                        # Directory to store temporary backup files
├── config/                         # Configuration directory for DB, AWS, encryption keys, etc.
│   ├── db_config.yaml              # Database connection configurations
│   ├── aws_config.yaml             # AWS S3 configuration settings
│   └── encryption_key.key          # Encryption key (generated and stored securely)
│
├── logs/                           # Log files for backup processes
│   └── backup_log.log              # Log for backup process execution
│
├── scripts/                        # Python scripts for backup, encryption, and upload
│   ├── __init__.py                 # Initializes the scripts as a package
│   ├── backup.py                   # Script for database backup
│   ├── encryption.py               # Encryption and decryption functionalities
│   ├── upload.py                   # Handles file uploads to S3 or any cloud provider
│   └── automated_backup.py         # Main script to coordinate backup, encryption, and upload
│
├── tests/                          # Test suite for unit testing the functionalities
│   ├── test_backup.py              # Test cases for backup process
│   ├── test_encryption.py          # Test cases for encryption/decryption
│   ├── test_upload.py              # Test cases for uploading to S3
│   └── __init__.py                 # Initializes the tests as a package
│
├── .gitignore                      # Git ignore file for sensitive data, logs, and compiled code
├── LICENSE                         # License for open source (if applicable)
├── README.md                       # Project description and instructions for setting up
└── requirements.txt                # Dependencies for Python modules (e.g., boto3, cryptography, etc.)

```

# Requirements
Make sure to install the required dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

# AWS S3 Configuration
Set up your AWS credentials either through aws_config.yaml or by using AWS CLI environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, etc.).

# Database Configuration
In config/db_config.yaml, provide your database connection details:

```
database:
  host: "localhost"
  user: "db_user"
  password: "db_password"
  name: "db_name"

```

# Encryption Key
To generate an encryption key, run:

```
from cryptography.fernet import Fernet

# Generate and store the key
key = Fernet.generate_key()
with open('config/encryption_key.key', 'wb') as key_file:
    key_file.write(key)

```
- This key will be used to encrypt and decrypt backup files.

# Step-by-Step Execution

1. Database Backup:
    - Run the backup script to create a database backup:
    ```
    python3 scripts/automated_backup.py

    ```
    The script reads the database configuration from config/db_config.yaml and performs the backup using the backup_database() function from backup.py. The backup file is saved in the backups/ directory (e.g., backups/db_backup.sql).

    - Result: A SQL dump file will be saved to the backups/ directory.

    Example backup:

    ```
    backups/db_backup.sql

    ```

2. Encrypt the Backup:

    - The backup file is then encrypted using the encryption key stored in config/encryption_key.key. This is done using the encrypt_file() function from encryption.py.
    - Result: The encrypted backup file will be saved with the .enc extension.

    Example encrypted file:

    ```
    backups/db_backup.sql.enc
    ```

3. Upload to AWS S3:

    - After encryption, the file is uploaded to the specified S3 bucket using the upload_to_s3() function from upload.py. AWS configuration is read from config/aws_config.yaml.
    - Result: The encrypted backup file is uploaded to the S3 bucket.

    Example S3 path:

    ```
    s3://your-bucket-name/backups/db_backup.sql.enc

    ```
4. Logging:

    - Each step is logged in logs/backup_log.log. This log file helps you track the process, including any errors encountered during backup, encryption, or upload.
    
    Example log output:
    ```
    2024-09-01 18:45:12,357 INFO: Backup completed successfully.
    2024-09-01 18:45:13,021 INFO: Backup file encrypted successfully.
    2024-09-01 18:45:14,085 INFO: Encrypted backup uploaded to S3 successfully.

    ```

    
# Testing
Unit tests are provided for each component of the project. To run the test suite:

```
python3 -m unittest discover tests/

```
The tests cover the following:

- test_backup.py: Tests the database backup process.
- test_encryption.py: Tests encryption and decryption functions.
- test_upload.py: Tests the S3 upload functionality.


Example:

>>> python3 tests/test_backup.py

# Example

1. Run Automated Backup:
```
python3 scripts/automated_backup.py

```
Expected output (logged in backup_log.log):

```
Backup completed successfully.
Backup file encrypted successfully.
Encrypted backup uploaded to S3 successfully.

```
2. View Backups on S3:
Log into your AWS S3 console and verify that the encrypted backup file is stored in your specified bucket.

# Security Best Practices
- Encryption Key Management: Store your encryption key securely and limit access. For production, consider using AWS KMS or HashiCorp Vault.
- Access Controls: Limit access to S3 buckets and ensure that only authorized users can access the backups.
- Log Management: Rotate and securely store log files. Do not log sensitive information such as database credentials or encryption keys.
