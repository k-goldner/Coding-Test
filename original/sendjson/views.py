from django.http import JsonResponse
import json

def prepare_payload(json_data_list):
    payload = json_data_list["payload"]
    referencedata = json_data_list["referenceData"]

    for key, value in referencedata.items():
        payload = json.loads(json.dumps(payload).replace("{" + key + "}", value))
    return payload

def send_json(request):
    if request.method == "POST":
        json_data = request.read()

        if json_data:
            json_data_list = json.loads(json_data)
            payload = prepare_payload(json_data_list)
            
        else:
            payload = {"response" :" no payload present, please resend with payload"}

    if request.method == "GET":
        payload = {"response" : "This is a GET, Please POST payload"}
    
    return JsonResponse(payload, safe=False)


