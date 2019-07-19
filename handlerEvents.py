import json
import boto3
import os
import time
import random

#Create Event
def createEvent(event, context):
  print(json.dumps(event))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": event
  }

  data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")
  response = dynamodb_client.put_item(
      TableName="eventos",
      Item={
          'id_evento': {
              'S': str(int(time.time()))+str(int(random.random()))
          },
          'name': {
              'S': data["name"]
          },
          'link': {
              'S': data["link"]
          },
          'description': {
              'S': data["description"]
          },
          'prerequisites': {
              'S': data["prerequisites"]
          },
          'address': {
              'S': data["address"]
          },
          'eventDate': {
              'S': data["eventDate"]
          },
          'eventHour': {
              'S': data["eventHour"]
          },
          'capacity': {
              'N': str(data["capacity"]),
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


#Delete Event
def deleteEvent(event, context):
  print(json.dumps(event))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": event
  }

  data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.delete_item(
      TableName='eventos',
      Key={
          'id_evento': {
              'S': data["id_evento"]
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
  
  
#Update Event
def updateEvent(event, context):
  print(json.dumps(event))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": event
  }

  data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.update_item(
      TableName='eventos',
      Key={
          'id_evento': {
              'S': data["id_evento"]
          }
      },
      
      AttributeUpdates={

          'name': {
              "Value":{'S': data["name"]},
              "Action": "PUT"
          },
          'link': {
              "Value":{'S': data["link"]},
              "Action":"PUT"
          },
          'description': {
              "Value":{'S': data["description"]},
               "Action":"PUT"
          },
          'prerequisites': {
              "Value":{'S': data["prerequisites"]},
               "Action":"PUT"
          },
          'address': {
              "Value":{'S': data["address"]},
               "Action":"PUT"
          },
          'eventDate': {
              "Value":{'S': data["eventDate"]},
               "Action":"PUT"
          },
          'eventHour': {
              "Value":{'S': data["eventHour"]},
               "Action":"PUT"
          },
          'capacity': {
              "Value":{'N': str(data["capacity"])},
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
  
#List Events
def listEvents(event, context):
  print(json.dumps(event))
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": event
  }

  #data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.scan(
     
      TableName='eventos',
      AttributesToGet=[
        "id_evento",
        "name",
        "eventHour",
        "eventDate",
        "link",
        "prerequisites",
        "address",
        "capacity"
        
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
  
#Get Events
def getEvent(event, context):
  print(json.dumps(event))
  id_event = event['pathParameters']['id']
  body = {
      "message": "Go Serverless v1.0! Your function executed successfully!",
      "input": event
  }

  #data = json.loads(event["body"])

  dynamodb_client = boto3.client("dynamodb")

  response = dynamodb_client.get_item(
      TableName='eventos',
      Key={
          'id_evento': {
              'S': id_event
          }
      }
     
  )


  response = {
      "statusCode": 200,
      "body": json.dumps(response),
      
  }
  return response