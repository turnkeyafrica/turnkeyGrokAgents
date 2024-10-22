# Turnkey AI Agents

This project contains AI agents designed to automate email personalization and RFP (Request for Proposal) analysis. These agents assist with generating personalized emails, answering RFP-related questions, and processing RFP files. The solution uses the CrewAI framework and integrates language models provided by Groq for natural language tasks.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Agents](#agents)
- [Tasks](#tasks)
- [Configuration](#configuration)
- [File Structure](#file-structure)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/turnkeyafrica/turnkeyGrokAgents.git
    ```

2. Navigate into the project directory:

    ```bash
    cd ai_agents
    ```

3. Install the necessary dependencies using Poetry:

    ```bash
    poetry install
    ```

    Alternatively, if you prefer using `pip`, create a virtual environment and install the dependencies from the `requirements.txt`:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

4. Set up the `.env` file:

    Create a `.env` file in the project root and add your API key for Groq:

    ```
    GROQ_API_KEY=your_api_key_here
    ```

5. Create the required `output` directory (the project will save the generated files here):

    ```bash
    mkdir output
    ```

## Usage

To run the main script and kick off the AI agents, simply execute:

```bash
python main.py
