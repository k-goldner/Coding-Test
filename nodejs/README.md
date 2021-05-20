### Created by Kent Goldner
### 20/05/2021

### Navigate to the folder location
### run docker-compose. (built with Docker Version 20.10.05 Build 55c4c88)

### using postman send a POST request to http://127.0.0.1:3000/
### raw body of json type. 
### app also checks for GET Request http://127.0.0.1:3000/ping and will receieve a Pong. Also attached are the postman Get and Request calls within an importable collection. 

### I have also written a unit test to check the function to replace REF_* is working correctly. The docker container will run the test, and will not launch the api application until the test passes. 
### this can be tested by modifying a record within the output_payload variable within /test/payload.test.js

```{
  "payload": {
    "name": "subscriber",
    "valueType": "array",
    "value": [
      {
        "name": "MN",
        "valueType": "string",
        "value": "{REF_MSISDN}"
      },
      {
        "name": "IM",
        "valueType": "string",
        "value": "{REF_IMSI}"
      },
      {
        "name": "NT",
        "valueType": "string",
        "value": "G"
      },
      {
        "name": "privateUser",
        "valueType": "array",
        "value": [
          {
            "name": "privateUserId",
            "valueType": "string",
            "value": "{REF_IMSI}@ims.mnc001.mcc505.3gppnetwork.org"
          },
          {
            "name": "roamingAllowed",
            "valueType": "string",
            "value": "false"
          },
          {
            "name": "publicUser",
            "valueType": "array",
            "value": [
              {
                "name": "publicIdValue",
                "valueType": "string",
                "value": "sip:{REF_IMSI}@ims.mnc001.mcc505.3gppnetwork.org"
              },
              {
                "name": "implicitRegSet",
                "valueType": "string",
                "value": "1"
              },
              {
                "name": "serviceProfileId",
                "valueType": "string",
                "value": "{REF_SERVPROFID}"
              },
              {
                "name": "testUser",
                "valueType": "array",
                "value": [
                  {
                    "name": "testIdValue",
                    "valueType": "string",
                    "value": "sip:{REF_IMSI}@ims.mod-connect.com"
                  },
                  {
                    "name": "implicitRegSet",
                    "valueType": "string",
                    "value": "2"
                  }
                ]
              }
            ]
          },
          {
            "name": "userImsi",
            "valueType": "string",
            "value": "{REF_IMSI}"
          }
        ]
      },
      {
        "name": "PO",
        "valueType": "string",
        "value": "0"
      }
    ]
  },
  "referenceData": {
    "REF_MSISDN": "0406679321",
    "REF_IMSI": "50002312344314",
    "REF_SERVPROFID": "2"
  }
}
```
