

from simple_salesforce import Salesforce
import logging

def salesforce_login(creds :list):

  try:
    sf = Salesforce(instance=creds[0], username=creds[1], password=creds[2], consumer_key=creds[3], consumer_secret=creds[4])
    return sf
  
  except Exception as e:
    logging.error(e)
    return None
    
