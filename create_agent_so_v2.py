
import os
from google.cloud import geminidataanalytics

# 1. Set variables
data_agent_client = geminidataanalytics.DataAgentServiceClient()

location = "global"
billing_project = os.environ.get('DEVSHELL_PROJECT_ID')
if not billing_project:
    billing_project = "bq-demos-469816" # Fallback to the project ID from the prompt
data_agent_id = "stackoverflow_agent_v2"

# 2. Set system instructions for the agent
system_instruction = """
system_instruction:
  - You are a data analyst specializing in the Stack Overflow dataset.
  - You have access to three tables: `posts_questions`, `users`, and `comments`.
  - `posts_questions` contains questions from Stack Overflow.
  - `users` contains information about the users who post questions and answers.
  - `comments` contains comments on posts.
  - The `id` in the `users` table corresponds to the `owner_user_id` in the `posts_questions` table and the `user_id` in the `comments` table.
  - The `id` in the `posts_questions` table corresponds to the `post_id` in the `comments` table.
tables:
  posts_questions:
    description: "Contains questions from Stack Overflow."
    fields:
      id: "The unique ID of the question."
      title: "The title of the question."
      body: "The body of the question."
      answer_count: "The number of answers to the question."
      comment_count: "The number of comments on the question."
      creation_date: "The date the question was created."
      owner_user_id: "The ID of the user who asked the question."
      score: "The score of the question."
      tags: "The tags associated with the question."
  users:
    description: "Contains information about Stack Overflow users."
    fields:
      id: "The unique ID of the user."
      display_name: "The display name of the user."
      reputation: "The reputation of the user."
  comments:
    description: "Contains comments on Stack Overflow posts."
    fields:
      id: "The unique ID of the comment."
      text: "The text of the comment."
      creation_date: "The date the comment was created."
      post_id: "The ID of the post the comment is on."
      user_id: "The ID of the user who wrote the comment."
      score: "The score of the comment."
join_instructions:
  - goal: "Find the user who asked a specific question."
    method: "INNER JOIN posts_questions and users on their common key."
    keys:
      - "owner_user_id"
      - "id"
  - goal: "Find the comments on a specific question."
    method: "INNER JOIN posts_questions and comments on their common key."
    keys:
      - "id"
      - "post_id"
golden_queries:
  - natural_language_query: "Who asked the question with the title 'How to iterate over rows in a Pandas DataFrame'?"
    sql_query: |
      SELECT
          u.display_name
      FROM
          `bq-demos-469816.stackoverflow2.users` AS u
      INNER JOIN
          `bq-demos-469816.stackoverflow2.posts_questions` AS q
      ON
          u.id = q.owner_user_id
      WHERE
          q.title = 'How to iterate over rows in a Pandas DataFrame'
"""

# 3. Set BigQuery Table Data sources
bq_questions = geminidataanalytics.BigQueryTableReference(
    project_id="bq-demos-469816", dataset_id="stackoverflow2", table_id="posts_questions"
)
bq_users = geminidataanalytics.BigQueryTableReference(
    project_id="bq-demos-469816", dataset_id="stackoverflow2", table_id="users"
)
bq_comments = geminidataanalytics.BigQueryTableReference(
    project_id="bq-demos-469816", dataset_id="stackoverflow2", table_id="comments"
)
datasource_references = geminidataanalytics.DatasourceReferences(
    bq=geminidataanalytics.BigQueryTableReferences(table_references=[bq_questions, bq_users, bq_comments]))

# 4. Set context for stateful chat
published_context = geminidataanalytics.Context(
    system_instruction=system_instruction,
    datasource_references=datasource_references,
    options=geminidataanalytics.ConversationOptions(
        analysis=geminidataanalytics.AnalysisOptions(
            python=geminidataanalytics.AnalysisOptions.Python(
                enabled=False
            )
        )
    ),
)

data_agent = geminidataanalytics.DataAgent(
    data_analytics_agent=geminidataanalytics.DataAnalyticsAgent(
        published_context=published_context
    ),
)

# Create the agent
try:
    data_agent_client.create_data_agent(request=geminidataanalytics.CreateDataAgentRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        data_agent_id=data_agent_id,
        data_agent=data_agent,
    ))
except Exception as e:
    print(f"Agent already exists: {e}")


# 5. Get the Agent
request = geminidataanalytics.GetDataAgentRequest(
    name=data_agent_client.data_agent_path(
        billing_project, location, data_agent_id)
)
response = data_agent_client.get_data_agent(request=request)
print(response)
