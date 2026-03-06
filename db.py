import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

table = dynamodb.Table("projects")

def get_project(project_name):
    response = table.get_item(
        Key={"project_name": project_name}
    )
    return response.get("Item")