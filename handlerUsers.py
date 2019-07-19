import json
import boto3
import os
import time
import random

#Create Users
def createUsers(users, context):
  print(json.dumps(users))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": users
  }

  data = json.loads(users["body"])
  print('data: ', data)
  dynamodb_client = boto3.client("dynamodb")
  response = dynamodb_client.put_item(
      TableName="asistentes",
      Item={
          'id_users': {
              'S': data["email"],
          },
          'id_event': {
              'S': data["id_evento"]
          },
          'name': {
              'S': data["name"]
          },
          'company': {
              'S': data["company"],
          },
          'puesto': {
              'S': data["puesto"],
          },
          'email': {
              'S': data["email"],
          },
          'phone': {
              'S': data["phone"],
          },
          'select': {
              'S': data["select"],
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
  
#Delete Users 
def deleteUsers(users, context):
  print(json.dumps(users))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": users
  }

  data = json.loads(users["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.delete_item(
      TableName='asistentes',
      Key={
          'id_users': {
              'S': data["id_users"]
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
  
#Update Users
def updateUsers(users, context):
  print(json.dumps(users))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": users
  }

  data = json.loads(users["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.update_item(
      TableName='asistentes',
      Key={
          'id_users': {
              'S': data["id_users"]
          }
      },
      
      AttributeUpdates={
          
          "name":{
              "Value": { 'S': data["name"] },
              "Action": "PUT"
          },
          'company': {
              "Value":{'S': data["company"]},
              "Action": "PUT"
          },
          'puesto': {
              "Value":{'S': data["puesto"]},
              "Action":"PUT"
          },
          'email': {
              "Value":{'S': data["email"]},
              "Action":"PUT"
          },
          'phone': {
              "Value":{'S': data["phone"]},
              "Action":"PUT"
          },
          'select': {
              "Value":{'S': data["select"]},
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
  
  
#List Users
def listUsers(users, context):
  print(json.dumps(users))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": users
  }

  #data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.scan(
      TableName='asistentes',
      AttributesToGet=[
        "id_users",
        "name",
        "company",
        "participants"
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
  
  
#Get User
def getUser(users, context):
  print(json.dumps(users))
  id_users = users['pathParameters']['id']
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": users
  }

  #data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.get_item(
      TableName='asistentes',
      Key={
          'id_users': {
              'S': id_users
          }
      }
     
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