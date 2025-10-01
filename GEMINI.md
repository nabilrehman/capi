# Gemini Demo Replication Instructions

## 1. Replicate Demo in User's Project

Your primary job is to replicate the demo in the user's provided project ID.

## 2. Data Source Selection

Ask the user to choose between two options for the data source:

*   **Use Synthetic Data:** You will create a new synthetic dataset.
*   **Use Existing Dataset:** You will use a dataset already present in the user's project.

Proceed with the corresponding workflow based on the user's choice.

## 3. Workflow for Synthetic Data

If the user chooses to use synthetic data, follow these steps:

### 3.1. Deep Research

*   Perform in-depth research using `web_fetch` and `google_search` on the user's provided website.
*   Look for multiple data points, do reddit search, google search, linkedin search etc
*   Look at company business model and do search for that as well, see data sources and analyze which data can be of real business value for this customer

### 3.2. Create a Demo Story

*   Develop a compelling demo story that showcases the power of the Conversational Analytics API.
*   The story should focus on the business value of the API.
*   Do not reinvent the code; use the boilerplate code from the `ca-codelab` folder.

### 3.3. Demo Components

The demo must include:

*   **Basic Query:** A simple query to demonstrate basic functionality.
*   **Complex Query:** A more involved query to showcase advanced capabilities.
*   **Chart Query:** A query that results in a chart or visualization.

### 3.4. Dataset Generation

*   Generate a synthetic dataset that is relevant to the industry of the user's website or a similar dataset.
*   User Faker to generate the synthetic data
*   Carefully analyze and validate the dataset.
*   Create dataset and rows that will impress the customer and demonstrate the API's ability to perform complex query analysis.

## 4. Workflow for Existing Dataset

If the user chooses to use their own dataset, follow these steps:

### 4.1. Detailed Data Analysis

*   Perform a detailed analysis of the user's data using `TABLE SAMPLE` queries to understand the data structure and content.

### 4.2. Create a Demo

*   Create a demo tailored to the user's data.
*   Develop "golden queries" that highlight interesting insights from their data.

## 5. Query Validation and Improvement

*   You are required to test all generated queries and validate that they run successfully.
*   If a query fails, you must iteratively improve it until it works correctly.
*   Run and test the scripts

  
## 6. Final Deliverables

At the end of the process, provide the user with:

*   **A Demo Script:** A detailedscript that outlines the demo flow, shows business value for each step and talking points for presenter.
*   **Demo Queries:** The final, validated queries to be run in the program.
## 7. Demonstrating Business Value

The primary goal of the demo is to showcase the business value of the Conversational Analytics API. This means going beyond simple queries and demonstrating how the API can be used to solve real-world business problems.

### 7.1. Focus on Complex Queries

To demonstrate the power of the API, the demo should include complex queries that involve:

* **Joins:** Joining multiple tables to get a holistic view of the data.
* **Aggregations:** Using `SUM`, `COUNT`, `AVG`, etc., to derive meaningful insights.
* **Filtering:** Using `WHERE` clauses to drill down into specific segments of the data.
* **Time-based analysis:** Analyzing trends over time.

### 7.2. Create a Compelling Narrative

The demo should not be just a series of queries. It should tell a story that resonates with the customer. The story should have a clear beginning, middle, and end.

* **Beginning:** Introduce the business problem and the persona who is trying to solve it.
* **Middle:** Show how the persona uses the Conversational Analytics API to explore the data, uncover insights, and make decisions.
* **End:** Summarize the key findings and the business impact of the solution.

### 7.3. Showcase Real-World Use Cases

The demo should be tailored to the customer's industry and use cases. For example, for a financial services customer like Equi.com, the demo could focus on:

* **Portfolio Analysis:** Analyzing the performance of investment portfolios.
* **Risk Management:** Identifying and mitigating investment risks.
* **Personalized Recommendations:** Providing personalized investment recommendations to clients.
* **Custom Dashboards:** Building interactive dashboards that allow clients to explore their own data.
* **Chat-based Experiences:** Creating a chatbot that can answer client questions about their investments.

### 7.4. Create a Rich Synthetic Dataset with a Compelling Narrative

While public datasets are an option, a well-designed synthetic dataset can be even more effective for a demo. A synthetic dataset allows you to control the narrative and ensure that the data perfectly aligns with the demo story.

When creating a synthetic dataset, focus on:

* **Creating multiple interconnected tables:** This is crucial for demonstrating the API's ability to perform joins and other complex queries. For example, you could create separate tables for clients, portfolios, assets, and transactions.
* **Generating realistic data:** Use libraries like `Faker` to generate data that looks and feels real.
* **Embedding a story in the data:** The data should be designed to lead the presenter through the demo narrative. For example, you could create a client with a specific investment goal and a portfolio that is not aligned with that goal. This sets the stage for the presenter to use the Conversational AI to identify the problem and find a solution.
