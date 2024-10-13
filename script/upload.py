import boto3
import logging
import yaml

def load_aws_config(config_file):
    """Loads AWS configuration from a YAML file."""
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def upload_to_s3(file_path, aws_config):
    """Uploads the specified file to an AWS S3 bucket."""
    s3 = boto3.client('s3', 
                      aws_access_key_id=aws_config['access_key'], 
                      aws_secret_access_key=aws_config['secret_key'],
                      region_name=aws_config['region'])

    try:
        # Upload file to S3 bucket
        s3.upload_file(file_path, aws_config['bucket_name'], file_path.split('/')[-1])
        logging.info(f"File successfully uploaded to S3: {file_path}")
    except Exception as e:
        logging.error(f"Failed to upload file to S3: {e}")
        raise
