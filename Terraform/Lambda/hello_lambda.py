import os
import math

def lambda_handler(event, context):
    return "{} from Lambda!".format(os.environ['greeting'])