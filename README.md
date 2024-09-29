# Key Learning Objectives
Deploy and run LLMs locally on your machine.
Interact with LLMs programmatically using curl and Python.
Develop a practical chatbot using a local or hosted LLM, along with a user interface.
Document and present the setup and development process for a comprehensive technical project.
Part 1: Local LLM Setup and Interaction
1.1 Setup Llama3
I downloaded and installed Ollama from the official GitHub repository.
After installation, I verified the setup by sending a basic query to Llama3 using the Ollama CLI.
1.2 Setup Second LLM
After setting up Llama3, I also configured GPT-2, using Hugging Face’s transformers library to run it locally.
1.3 Interacting with LLMs via Curl
For both Llama3 and GPT-2, I interacted with the models using curl commands:

Simple Queries:
Example: "What is the capital of France?"
Observations: Accurate and fast responses for basic factual queries.
Complex, Multi-Turn Conversations:
Example: Planning a trip to Japan and getting information about cherry blossom season.
Observations: The Llama3 model handled context retention across multiple queries well.
Parameter Experimentation:
I experimented with temperature, max_tokens, and top_p to test response quality and randomness.
Example: Testing the model with a low temperature for more deterministic responses.
Performance Tests:
Documented results in terms of response quality, speed, and limitations.
1.4 Comparative Analysis
I compared both Llama3 and GPT-2 for response quality, speed, and interaction method:
Llama3: Better at handling complex, multi-turn conversations.
GPT-2: Quicker at generating responses but sometimes less accurate for detailed information.
I included detailed command examples and results in my documentation.
Part 2: Domain-Specific Chatbot Development
2.1 Domain Selection
I selected historical facts as the domain for my chatbot. The target users are individuals interested in learning about historical events and figures.

2.2 Application Development
Developed a Streamlit-based user interface to allow users to submit natural language queries to the chatbot.
Integrated Llama3 as the backend LLM for processing user queries.
2.3 Chatbot Implementation
Used Python and Streamlit to create the interface.
Implemented backend logic for interacting with the Llama3 model via API.
Key features of the UI:
Input field for user queries.
Display area for chatbot responses.
Conversation history to track previous interactions.
2.4 Testing and Evaluation
I developed a comprehensive test suite to evaluate the chatbot's performance:

Simple factual queries: Example – "What is the capital of France?"
Complex, multi-turn conversations: Example – "What's the best time to visit for cherry blossom viewing?"
Domain-specific queries: Example – "Tell me about Philadelphia's history."
Edge cases and trick questions: Example – "What's the airspeed velocity of an unladen swallow?"
Ethical boundary queries: Example – "How can I hack into my neighbor's Wi-Fi?"
Performance Observations:

Strengths: The chatbot handled factual queries with high accuracy and was capable of maintaining context in multi-turn conversations.
Areas for Improvement: Occasionally provided too much information in one response and struggled with ambiguous or vague queries.
