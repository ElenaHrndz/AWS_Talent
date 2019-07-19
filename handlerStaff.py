import json
import boto3
import os
import time
import random

#Create Staff
def createStaff(staff, context):
  print(json.dumps(staff))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": staff
  }

  data = json.loads(staff["body"])

  dynamodb_client = boto3.client("dynamodb")
  response = dynamodb_client.put_item(
      TableName="staff",
      Item={
          'id_staff': {
              'S': str(int(time.time()))+str(int(random.random()))
          },
          'id_event': {
              'S': str(int(time.time()))+str(int(random.random()))
          },
          
          'name': {
              'S': data["name"]
          },
          'rol': {
              'S': data["rol"]
          },
          'position': {
              'S': data["position"]
          }
          
      }
  )
  response = {
      "statusCode": 200,
      "body": "ok",
      "headers": {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 1
    }
  }
  return response
  
#Delete Staff  
def deleteStaff(staff, context):
  print(json.dumps(staff))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": staff
  }

  data = json.loads(staff["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.delete_item(
      TableName='staff',
      Key={
          'id_staff': {
              'S': data["id_staff"]
          }
      }
  )


  response = {
      "statusCode": 200,
      "body": "ok",
      "headers": {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 1
    }
  }
  return response  
  
  
#Update Staff
def updateStaff(staff, context):
  print(json.dumps(staff))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": staff
  }

  data = json.loads(staff["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.update_item(
      TableName='staff',
      Key={
          'id_staff': {
              'S': data["id_staff"]
          }
      },
      
      AttributeUpdates={
          
          "name":{
              "Value": { 'S': data["name"] },
              "Action": "PUT"
          },
          'rol': {
              "Value":{'S': data["rol"]},
              "Action": "PUT"
          },
          'position': {
              "Value":{'S': data["position"]},
              "Action":"PUT"
          }
      }
  )


  response = {
      "statusCode": 200,
      "body": "ok",
      "headers": {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 1
    }
  }
  return response
  
  
#List Staff
def listStaff(staff, context):
  print(json.dumps(staff))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": staff
  }

  #data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.scan(
      TableName='staff',
      AttributesToGet=[
        "id_staff",
        "name",
        "rol",
        "position"
    ]
     
  )


  response = {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 1
    }
  }
  return response