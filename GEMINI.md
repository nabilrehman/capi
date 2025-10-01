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
