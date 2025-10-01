
import os
from google.cloud import geminidataanalytics
from chat_utils import *

# Set variables
location = "global"
billing_project = os.environ.get('DEVSHELL_PROJECT_ID')
if not billing_project:
    billing_project = "bq-demos-469816" # Fallback to the project ID from the prompt
data_agent_id = "google_trends_analytics_agent"
conversation_id = "my_first_conversation"

def stream_chat_response(question: str):
    """
    Sends a chat request, processes the streaming response, and if a chart
    was generated, starts the preview server and waits for it to be closed.
    """
    data_chat_client = geminidataanalytics.DataChatServiceClient()
    chart_generated_flag = [False]
    messages = [
        geminidataanalytics.Message(
            user_message=geminidataanalytics.UserMessage(text=question)
        )
    ]
    conversation_reference = geminidataanalytics.ConversationReference(
        conversation=data_chat_client.conversation_path(
            billing_project, location, conversation_id
        ),
        data_agent_context=geminidataanalytics.DataAgentContext(
            data_agent=data_chat_client.data_agent_path(
                billing_project, location, data_agent_id
            ),
        ),
    )
    request = geminidataanalytics.ChatRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        messages=messages,
        conversation_reference=conversation_reference,
    )
    stream = data_chat_client.chat(request=request)
    for response in stream:
        show_message(response, chart_generated_flag)

# Question 3
question = "What was the percent gain in growth for these search terms from the week before?"
stream_chat_response(question=question)
