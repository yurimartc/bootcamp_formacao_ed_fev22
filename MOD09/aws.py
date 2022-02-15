#%%
import boto3
from botocore import exceptions
from botocore.exceptions import ClientError
import logging
from dotenv import load_dotenv
from os import getenv

import dotenv

# %%
load_dotenv('C:\\Users\\yurim\\OneDrive\\Documentos\\bootcamp_formacao_ed_fev22\\.env')


# %%
def criar_bucket(nome, region=None):
    try:
        if region==None:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=getenv("AWS_ID"),
                aws_secret_access_key=getenv("AWS_KEY")
            )
            s3_client.create_bucket(Bucket=nome)
        else:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=getenv("AWS_ID"),
                aws_secret_access_key=getenv("AWS_KEY"),
                region_name=region
            )
            s3_client.create_bucket(Bucket=nome)

    except ClientError as e:
        logging.error(e)
        return False
    return True


# %%
criar_bucket('yuri-s3-bucket-do-dicaprio')
# %%
getenv('AWS_KEY')
# %%
