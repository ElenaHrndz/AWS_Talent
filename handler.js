'use strict';
var AWS = require("aws-sdk");

module.exports.hello = async event => {
  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        message: 'Go Serverless v1.0! Your function executed successfully!',
        input: event,
      },
      null,
      2
    ),
  };

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};

module.exports.crearEvento = async event => {
  var docClient = new AWS.DynamoDB.DocumentClient();
  
  var table = "eventos";
  
  var banner="https://lh3.googleusercontent.com/NwK1izoFlfupQ1exwno-mW3taVEwgcsrL3N6fy89cc5GIWutaiZMUEyaxYLBFwVLueJEpJI3OzTqi7WfclGkFNKMgskomTd5f-dSCubswrzisJ0v9XZjn_TPsDOYVJaUBs-K1aNnVbJnyc8GcV5FBx4maa6dw0mRLewwIR5XfZUZZ3qyRPGK4KDHQuZVU4wRb5sYfLULHAuGL8DYW5PBMTYsygIMYC_bqTKQYfB5F96w8j4uxViWXMv1UhtOffX0R6Ff-NsX0UQUKa-L8eN2ZPuWG1aEi_PmdsiEvUjikq0Mr6LHhuUbSagMFDR9QQIrK3O8ea-xMLDJSr4PbR5mnjKm_nORnkBfXG4x3DCbppMm2qLcZEUxBHlLTcom1kCbOz5wBg8poUu3EmXQhEQ6QFINtTIPSo4TKqnKxy86Eb3q1wb_BqPoOwKnkiorur4XezJoj96QHtKteezAr3GtSwrFBecp-_nhdBcu2Rsx7mx9NStxRHczR6ldA2__XLDUDn2KidotlILixKmhfTv1BZwamMzIdEF4nbreYKY1808FEy5tdt2p7f50GroFkRqUSGncZMyMkwVay_Gf1pV3M84XMnAbMmcOy-z1mORBn89nTGmf-23hzpzMdWhqFvJUf9K8MPP3xL3eJAT4gRSWl7SpoUY2lYJzPFr-3fdOV5ZKIMQzQ2RJiozliG7JKiyN2O4iafT0rZ8-Kpz4jl3DHCbmVg=w1706-h831-no";
  var name = "Reto";
  var description = "Día de retos";
  // var agenda = {date, time, activity};
  var link = "https://serverless.com/framework/docs/providers/aws/guide/quick-start/";
  var prerequisites = "Computadora";
  var address = "insurgentes 122";
  var eventDate = "2 de agosto";
  var eventHour = "12:00";
  var capacity = "200";
  
  var params = {
      TableName:table,
      Item:{
        "banner":banner,
          "name": name,
          "description": description,
          // "agenda": {
          //   "date": date,
          //   "time": time,
          //   "activity": activity
          // },
          "assistenResgisterLink":link,
          "prerequisites": prerequisites,
          "address": address,
          "eventDate": eventDate,
          "eventHour": eventHour,
          "capacity": capacity
      },
  };
  
  console.log("Adding a new item...");
  
  docClient.put(params, function(err, data) {
      console.log("enter");
      if (err) {
          console.error("Unable to add item. Error JSON:", JSON.stringify(err, null, 2));
      } else {
          console.log("Added item:", JSON.stringify(data, null, 2));
           return {
            statusCode: 200,
            body: JSON.stringify(
              {
                message: 'Go Serverless v1.0! Your function executed successfully!',
                input: event,
              },
              null,
              2
            ),
          };
        }
    });
    
  //console.log(JSON.stringify(event));

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};
