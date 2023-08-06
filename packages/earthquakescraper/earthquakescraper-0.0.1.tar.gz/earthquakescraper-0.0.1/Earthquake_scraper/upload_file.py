from botocore.exceptions import ClientError
import logging
import boto3
import botocore


def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    Parameters
    ----------
    file_name : str
        Name of the file we want to upload
    bucket: str
        Name of the bucket
    object_name:
        Name of the object as we want it to appear in the bucket

    Returns
    -------
    bool
        False if the upload caused an error. True if the upload was successful

    This function is borrowed from Iván Ying Xuan.
    """
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


upload_file('df.csv', 'earthquakescraper')
