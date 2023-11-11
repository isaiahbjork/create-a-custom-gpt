# Create A Custom GPT in Under 10 Minutes - Build Your Own GPT

# Video Tutorial: [Click Here](https://youtu.be/OSvnGAYTAVE)

Welcome to the README file for the "Create A Custom GPT in Under 10 Minutes - Build Your Own GPT" tutorial. This guide is designed to accompany the YouTube tutorial video where I demonstrate how to create a custom GPT using OpenAI's technology. The focus is on building a JSON data analyst GPT and integrating it with various APIs for enhanced functionality.

## Overview

This tutorial walks you through the process of creating a custom version of ChatGPT 4. The aim is to develop a GPT model that can analyze data from APIs, leveraging capabilities such as web browsing, DALL·E image generation, and code interpretation.

## Prerequisites

- OpenAI ChatGPT Account
- Basic understanding of GPTs and AI
- AWS Account
- Basic knowledge of Python programming

## Setup

### 1. Set up a lambda function

1. Create a new lambda function
2. Select Python & use the same environment your computer is to make it easier in the future.

### 2. Setup an API Gateway

1. Create a new HTTP API
2. Add the lambda function integration to the API Gateway
3. Create a GET route
4. Connect the lambda function to the GET route.

### 3. Add the Lambda Code to AWS

1. Copy & Paste the lambda function in <code>lambda_handler.py</code>
2. Click on "Deploy"
3. Visit the configuration tab and copy the API Gateway Link 

### 4. Create the Custom GPT

1. Visit [chat.openai.com](chat.openai.com)
2. Go to explore
3. Click on create a GPT
4. Go to configure
5. Give your custom GPT a name, instructions, upload important documents for additional knowledge.
6. Enable necessary tools
7. Click on Add Actions
8. Give it a name and description
9. Add the API route from AWS as the root url
10. Create an action for the GET route
11. Give it a name and description
12. If your routes require parameters like path, query, or body those can also be added under parameters.
13. Authentication can be setup via API key or OAuth

### Prompt

As a skilled assistant, your role is to analyze the JSON data provided and execute tasks based on that data. You should consider the structure, contents, and any patterns within the JSON. Then, take appropriate actions as requested, such as summarizing the data, extracting specific information, making calculations, or even generating code to manipulate the data further. Always ensure accuracy, provide clear explanations or outputs, and adhere to any specified constraints.

## Additional Resources

- **Further Learning**:
  - Explore more about GPTs, AI, AWS, and Python through [OpenAI's Documentation](https://openai.com/) and [AWS Training and Resources](https://aws.amazon.com/training/). I will also be creating more videos around these topics to help you learn more.

## License

- This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE.md](LICENSE.md) file for details.