
import os
from google.cloud import geminidataanalytics

data_chat_client = geminidataanalytics.DataChatServiceClient()

location = "global"
billing_project = os.environ.get('DEVSHELL_PROJECT_ID')
if not billing_project:
    billing_project = "bq-demos-469816"
data_agent_id = "google_trends_analytics_agent"

agent_path = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"

# Create a message
messages = [
    geminidataanalytics.Message(
        user_message=geminidataanalytics.UserMessage(
            text="Find all terms in the 'New York NY' area that were in both the top 25 and top 25 rising lists for the week of July 6th, 2025, and show their ranks and percent gain."
        )
    )
]

# Send the query to the agent
request = geminidataanalytics.ChatRequest(
    parent=f"projects/{billing_project}/locations/{location}",
    messages=messages,
    data_agent_context=geminidataanalytics.DataAgentContext(
        data_agent=agent_path
    )
)

response_stream = data_chat_client.chat(request=request)

for response in response_stream:
    print(response)
