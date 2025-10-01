
import os
from google.cloud import geminidataanalytics

# 1. Set variables
data_agent_client = geminidataanalytics.DataAgentServiceClient()
data_chat_client = geminidataanalytics.DataChatServiceClient()


location = "global"
billing_project = os.environ.get('DEVSHELL_PROJECT_ID')
if not billing_project:
    billing_project = "bq-demos-469816" # Fallback to the project ID from the prompt
data_agent_id = "stackoverflow_agent_v2"

def setup_conversation(conversation_id: str):
    data_chat_client = geminidataanalytics.DataChatServiceClient()
    conversation = geminidataanalytics.Conversation(
        agents=[data_agent_client.data_agent_path(
            billing_project, location, data_agent_id)],
    )
    request = geminidataanalytics.CreateConversationRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        conversation_id=conversation_id,
        conversation=conversation,
    )
    try:
        data_chat_client.get_conversation(name=data_chat_client.conversation_path(
            billing_project, location, conversation_id))
        print(f"Conversation '{conversation_id}' already exists.")
    except Exception:
        response = data_chat_client.create_conversation(request=request)
        print("Conversation created successfully:")
        print(response)


conversation_id = "so_conversation_v2"
setup_conversation(conversation_id=conversation_id)
