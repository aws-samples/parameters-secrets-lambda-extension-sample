import pymysql
import urllib3
import os
import json

### Load in Lambda environment variables
port = os.environ['PARAMETERS_SECRETS_EXTENSION_HTTP_PORT']
aws_session_token = os.environ['AWS_SESSION_TOKEN']
env = os.environ['ENV']
app_config_path = os.environ['APP_CONFIG_PATH']
creds_path = os.environ['CREDS_PATH']
full_config_path = '/' + env + '/' + app_config_path

### Define function to retrieve values from extention local HTTP server cachce
def retrieve_extension_value(url): 
    http = urllib3.PoolManager()
    url = ('http://localhost:' + port + url)
    headers = { "X-Aws-Parameters-Secrets-Token": os.environ.get('AWS_SESSION_TOKEN') }
    response = http.request("GET", url, headers=headers)
    response = json.loads(response.data)   
    return response  

def lambda_handler(event, context):

    ### Load Parameter Store values from extension
    print("Loading AWS Systems Manager Parameter Store values from " + full_config_path)
    parameter_url = ('/systemsmanager/parameters/get/?name=' + full_config_path)
    config_values = retrieve_extension_value(parameter_url)['Parameter']['Value']
    print("Found config values: " + json.dumps(config_values))

    ### Load Secrets Manager values from extension
    print("Loading AWS Secrets Manager values from " + creds_path)
    secrets_url = ('/secretsmanager/get?secretId=' + creds_path)
    secret_string = json.loads(retrieve_extension_value(secrets_url)['SecretString'])
    #print("Found secret values: " + json.dumps(secret_string))

    rds_host =  secret_string['host']
    rds_db_name = secret_string['dbname']
    rds_username = secret_string['username']
    rds_password = secret_string['password']
    
    
    ### Connect to RDS MySQL database
    try:
        conn = pymysql.connect(host=rds_host, user=rds_username, passwd=rds_password, db=rds_db_name, connect_timeout=5)
    except:
        raise Exception("An error occurred when connecting to the database!")

    return "DemoApp sucessfully loaded config " + config_values + " and connected to RDS database " + rds_db_name + "!"
