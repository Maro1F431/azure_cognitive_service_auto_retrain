import logging

import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '.venv/Lib/site-packages')))

import azure.functions as func
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import *
from msrest.authentication import ApiKeyCredentials 

# Setup credentials and ENDPOINT for the related service.
ENDPOINT = # set your own
training_key = # set your own
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
project_id = # set your own
ressource_id = # set your own


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    publish_last_iteration()
    return func.HttpResponse(f"Hello. This HTTP triggered function executed successfully.")


def publish_last_iteration():
    # Create the training client.
    trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
    # Get the last iteration
    iterations = trainer.get_iterations(project_id)
    it_to_publish = iterations[0].id

    # Unpublish second last iteration
    if len(iterations) > 1:
        if iterations[1].status == "succeeded":
            trainer.unpublish_iteration(project_id, iterations[1].id)
    
    publish_name = "iteration 1"
    if len(iterations) > 0:
        second_last_name = iterations[1].name
        last_num = int(second_last_name.split(" ")[1])
        publish_name = "iteration " + str(last_num + 1)

    trainer.publish_iteration(project_id, it_to_publish, publish_name, ressource_id)