import subprocess
import logging
import yaml

def load_db_config(config_file):
    """Loads database configuration from a YAML file."""
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def backup_database(db_config, backup_dir):
    """Performs the database backup using mysqldump and stores it in the specified directory."""
    db_name = db_config['db_name']
    username = db_config['username']
    password = db_config['password']
    host = db_config.get('host', 'localhost')

    backup_file = f"{backup_dir}/{db_name}_backup.sql"

    try:
        # Perform database backup using mysqldump
        subprocess.run(
            f"mysqldump -h {host} -u {username} -p'{password}' {db_name} > {backup_file}", 
            shell=True, check=True
        )
        logging.info(f"Database backup successful: {backup_file}")
        return backup_file
    except subprocess.CalledProcessError as e:
        logging.error(f"Database backup failed: {e}")
        raise
