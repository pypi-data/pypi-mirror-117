import json
import pandas as pd
from sqlalchemy import create_engine


def get_sqs_messages(context):
    messages = context['task_instance'].xcom_pull(key='messages', task_ids='listen_to_s3')['Messages']
    for message in messages:
        receipt_handle = message['ReceiptHandle']
        records = json.loads(message['Body'])['Records']
        for record in records:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            print(f"ReceiptHandle: {receipt_handle}  Bucket: {bucket}  Key: {key}")
            yield receipt_handle, bucket, key


def migrate_table(
    source_conn: str,
    target_conn: str,
    source_schema: str,
    source_table_name: str,
    target_schema: str,
    target_table_name: str,
    table_definition: dict
):
    """Copy postgres table from 

    :param source_conn: connection string of source postgres
    :type source_conn: str
    :param target_conn: connection string of target postgres
    :type target_conn: str
    :param source_schema: schema name of source postgres db
    :type source_schema: str
    :param source_table_name: table name of source postgres db
    :type source_table_name: str
    :param target_schema: schema name of target postgres db
    :type target_schema: str
    :param target_table_name: table name of target postgres db
    :type target_table_name: str
    :param table_definition: a mapping which key is the column name and value is the column type in sqlalchemy language
    :type schema: dict
    """
    data = pd.read_sql(
        sql=f"select * from {source_schema}.{source_table_name}",
        con=create_engine(source_conn.get_uri())
    )
    dtypes = table_definition
    # define data type
    data.to_sql(
        target_table_name,
        schema=target_schema,
        con=create_engine(target_conn.get_uri()),
        if_exists='replace',
        dtype=dtypes,
        index=False
    )
