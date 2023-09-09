import json
import logging
import random

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

     # Set CORS headers to allow requests from any origin
    headers  = {
        'Access-Control-Allow-Origin': 'http://localhost:5173,*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        'Content-Type': 'application/json'
    }
    if req.method == "OPTIONS":
        # Handle preflight requests (OPTIONS) with a 200 OK response
        return func.HttpResponse(
            status_code=200,
            headers=headers
        )
    else:
        cost = req.params.get('cost')
        if not cost:
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                cost = req_body.get('cost')

        if cost:
            msrp = generate_price(cost=cost)
            # Create a dictionary to represent your JSON response
            response_data = {
                'msrp': msrp
            }

            # Serialize the dictionary to a JSON string
            json_response = json.dumps(response_data)

            return func.HttpResponse(json_response, headers=headers)
        else:
            return func.HttpResponse(
                "Didn't recieve HSRP and Cost of the item",
                status_code=422
            )
    
def generate_price(cost):
    return (round(float(random.uniform(cost * 1.2, cost * 1.8)) / 10) * 10 ) - 0.01