
import os
from google.cloud import geminidataanalytics

# 1. Set variables
data_agent_client = geminidataanalytics.DataAgentServiceClient()

location = "global"
billing_project = os.environ.get('DEVSHELL_PROJECT_ID')
if not billing_project:
    billing_project = "bq-demos-469816" # Fallback to the project ID from the prompt
data_agent_id = "google_trends_analytics_agent"

# 2. Get the Agent
request = geminidataanalytics.GetDataAgentRequest(
    name=data_agent_client.data_agent_path(
        billing_project, location, data_agent_id)
)
response = data_agent_client.get_data_agent(request=request)
print(response)
