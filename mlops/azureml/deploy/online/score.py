import os
import logging
import json
import numpy
import joblib


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """

global model

model_path = os.path.join(
  os.getenv("AZUREML_MODEL_DIR"), "used-cars-price-model/model.pkl"
)

model = joblib.load(model_path)
logging.info("Init Complete")


def run(raw_data):


  logging.info("model 1: request received.")
  data = json.loads(raw_data)["data"]
  data = numpy.array(data)
  result = model.predict(data)
  logging.info("Request Processed")
  return result.tolist()
