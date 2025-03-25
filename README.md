# AI Use Case Generator & Resource Finder

This project is designed to generate AI and Generative AI use cases for various industries using a multi-agent system. The system conducts market research, analyzes industry trends, and provides relevant datasets and repositories. It is implemented using frameworks like OpenAGI, BeyondLLM, LangChain, LlamaIndex, Autogen, or CrewAI.

## Project Overview

The system consists of multiple agents, each responsible for a specific task:

1. **Research Agent (`agent_1.py`)**
   - Conducts market research based on company and industry data.
   - Collects relevant trends, reports, and insights from external sources.

2. **AI Use Case Generator (`agent_2.py`)**
   - Uses AI models like Gemini to generate use cases for specific industries.
   - Provides structured insights for AI implementation.

3. **Dataset Finder (`fetch_resources.py`)**
   - Fetches relevant datasets from Kaggle for the given AI use case.

4. **GitHub Repo Finder (`fetch_resources.py`)**
   - Finds related AI projects on GitHub to assist in implementation.

5. **Streamlit Frontend (`app.py`)**
   - Provides an interactive UI for inputting industry and company data.
   - Displays AI use cases, relevant datasets, and GitHub repositories.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-use-case-generator.git
cd ai-use-case-generator
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory and add the following API keys:

```bash
TAVILY_API_KEY=your_real_tavily_key
GEMINI_API_KEY=your_real_gemini_key
KAGGLE_USERNAME=your_real_kaggle_username
KAGGLE_KEY=your_real_kaggle_key


```

Replace `your_tavily_api_key`, `your_kaggle_username`, and `your_kaggle_api_key` with your actual API credentials.

### 5. Running the Application

```bash
streamlit run app.py
```

This will launch the web UI where you can input a company name and industry to generate AI use cases and find relevant datasets.
