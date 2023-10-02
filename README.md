# SummaRex - Your Personalized Chatbot

### User Interface
<img width="960" alt="image" src="https://github.com/SHOCKWAVE07/SummarRex/assets/74625124/6bf6c8b4-db19-4d41-81df-e936ab52a49e">

## Overview
SummaRex is an intelligent chatbot powered by the OpenAI GPT-3.5 Turbo model, fine-tuned to provide personalized financial advice and handle your personal information with care. In the era of big data, information overload has become a significant challenge. SummaRex aims to solve the information overload problem, making it easier for individuals and professionals to stay informed, make informed decisions, and access relevant content quickly.

## Problem Statement
In the era of big data, information overload has become a significant challenge. Solving the information overload problem, making it easier for individuals and professionals to stay informed, make informed decisions, and access relevant content quickly.

## Objective
The objective of the SummaRex project is as follows:
- Create a personalized AI Assistant with an intuitive interface using the OpenAI API and fine-tuning it to adapt responses based on the user's selected profile.
- Ensure a seamless user experience with clear instructions and user-friendly navigation.
- Generate contextually relevant, concise, and accurate responses to users' questions.
- Allow dynamic profile selection during conversations for varied interests.
- Continuously improve responses based on user feedback.
- Integrate OpenAI's GPT-3.5 Turbo model for natural language understanding.

## Features
- **Personalized Financial Advice:** SummaRex leverages a fine-tuned financial advisor model to provide tailored financial recommendations and insights.
- **Profile Selection:** Choose from various roles, including Programmer, Lawyer, Medical Student, Financial Advisor, Default, and Personalized, to receive context-specific responses.
- **Data Privacy:** Your personal information is handled with the utmost care. SummaRex ensures the security and confidentiality of your data.
- **Conversational AI:** Engage in natural and informative conversations with SummaRex to get answers to your financial questions and more.
- **User-Friendly Interface:** SummaRex's user interface is built using Gradio, ensuring a seamless and intuitive user experience.

## Technologies Used
- **OpenAI GPT-3.5 Turbo:** SummaRex is powered by the advanced GPT-3.5 Turbo model for natural language understanding and generation.
- **Fine-Tuned Models:** We've fine-tuned the GPT-3.5 Turbo with specialized models for financial advice and personal information handling.
- **Secure Data Handling:** SummaRex prioritizes data security and follows best practices to protect your personal information.
- **Gradio User Interface:** The chatbot's user interface is created using Gradio for a user-friendly and interactive experience.
- **Continuous Learning:** SummaRex continuously learns and improves to provide better assistance over time.

## Approaches

### Embedding based Approach:
Our first approach is to add embedding to the prompts we are passing to the API, so it can remember the context and where results are ranked by relevance to a query string.
This approach is mostly valid on all the major distinct profiles such as Medical Student, Programmer, Lawyer, and Financial Analyst.

### Fine Tuning based Approach:
As we have access to Open Ai API, we decided to Fine-tune our model on particular profiles. The result of this approach was to get a significant boost in relevant information with embedding being used.

## Process:

- **Step 1:** We grabbed the Yahoo Finance Dataset. As we know a large dataset is required to fine-tune the LLMs, so we generated an ample amount of Prompt and outputs using the GPT 4.0 Model.

- **Step 2:** We restructured the data in the format of the given OpenAi API request format.

- **Step 3:** We parsed the data to the API with given constraints of MAX_TOKEN Length, discarding non-unique prompts, etc.

- **Step 4:** Training the GPT-3.5-Turbo on our datasets.

- **Step 5:** We integrated the new model into our application.

  ![WhatsApp Image 2023-10-02 at 16 19 01](https://github.com/SHOCKWAVE07/SummarRex/assets/74625124/bf7c19c7-8436-468d-9c8f-260feab00696)

## Note:
We have a special feature in which we have a fine-tuned model trained on the LinkedIn Profile of one of our teammates (Pranjal Paira).
This was done to take personalization one step ahead. You can test this feature by selecting the Personalised Profile from the Down Menu.

## Getting Started
To get started with DigiBonds, follow these steps:
1. Clone the repository: `git clone https://github.com/SHOCKWAVE07/SummarRex.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Launch the application: `python main.py`

   


