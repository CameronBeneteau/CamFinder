import boto3

from Enums.RegionEnum import RegionEnum
from Models.PofileInfo import ProfileInfo
from Utils.DateTime import DateTime


class DynamoDb:
    def __init__(self, client_id: str, table_name: str, region: RegionEnum) -> None:
        self.client_id: str = client_id
        self.table_name: str = table_name
        self.dynamodb_client = boto3.client("dynamodb", region_name=region.value)

    def put_item(self, item: ProfileInfo, status: str, notes: str):
        self.dynamodb_client.put_item(
            TableName=self.table_name,
            Item={
                "Id": {"S": self.client_id},
                "Time": {"S": DateTime().get_time_formatted()},
                "Name": {"S": item.name},
                "ServiceType": {"S": item.service_type},
                "Location": {"S": item.location},
                "ProfileDescription": {"S": item.profile_description},
                "ProfileLink": {"S": item.profile_link},
                "Status": {"S": status},
                "Notes": {"S": notes},
            },
        )
