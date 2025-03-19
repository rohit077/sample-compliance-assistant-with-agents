# sample-compliance-assistant-with-agents
### Automate Compliance With Bedrock and CrewAI

Welcome to the **sample-compliance-assistant-with-agents** project, powered by [Amazon Bedrock](https://aws.amazon.com/bedrock/) and [crewAI](https://crewai.com). This is a solution for automating some of the most tedious regulatory compliance processes using multi-agent AI systems. This solution serves as a practical starting point for organizations looking to enhance their compliance processes with AI capabilities, demonstrating how intelligent systems could complement and streamline existing compliance workflows.

## 📌 Table of Contents

- [sample-compliance-assistant-with-agents](#sample-compliance-assistant-with-agents)
    - [Automate Compliance With Bedrock and CrewAI](#automate-compliance-with-bedrock-and-crewai)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Background Information](#-background-information)
  - [🎯 What This Solution Does](#-what-this-solution-does)
    - [Key Technologies Used](#key-technologies-used)
  - [📋 Prerequisites](#-prerequisites)
    - [AWS Account Requirements](#aws-account-requirements)
    - [Technical Requirements](#technical-requirements)
  - [🚀 Installation](#-installation)
    - [Step 1: Install CrewAI](#step-1-install-crewai)
    - [Step 2: Install Dependencies](#step-2-install-dependencies)
  - [⚙️ Customization](#️-customization)
    - [Add Your LLM. Depending on the LLM usage you may need to provide API key for LLM](#add-your-llm-depending-on-the-llm-usage-you-may-need-to-provide-api-key-for-llm)
    - [Configure Agents and Tasks](#configure-agents-and-tasks)
  - [🏃 Running the Project](#-running-the-project)
  - [🤖 Understanding Your Crew](#-understanding-your-crew)
  - [📞 Support](#-support)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)


## 📚 Background Information

Financial institutions operate in an environment where regulatory compliance is both critical and increasingly complex. Traditional approaches to managing compliance requirements—such as manual review of regulations, policy creation, and implementation of controls—are time-consuming, prone to human error, and struggle to keep pace with rapidly evolving regulatory landscapes.

This solution leverages generative AI and multi-agent systems to transform compliance management, offering:
- Automated regulatory monitoring
- Intelligent policy creation 
- Streamlined control implementation
- Real-time compliance guidance

## 🎯 What This Solution Does

This solution demonstrates how to build an intelligent, automated compliance management system that leverages multiple AI agents working in concert to:

🏗️ Architecture

- ✅ Continuously monitor and analyze regulatory changes
- ✅ Transform regulatory requirements into organizational policies
- ✅ Design and implement technical controls
- ✅ Maintain compliance documentation 
- ✅ Provide real-time guidance on compliance matters

### Key Technologies Used

- **Amazon Bedrock**: Foundation models and RAG capabilities
- **CrewAI**: Multi-agent orchestration framework
- **Amazon Bedrock Knowledge Bases**: Current, authoritative compliance information
- **Amazon Bedrock Guardrails**: Safety controls for responsible AI use
- **Amazon Bedrock Agents**: Memory retention across interactions and integrates Knowledge Bases and Guardrails

## 📋 Prerequisites

### AWS Account Requirements
- Active AWS account with appropriate permissions
- Access to Amazon Bedrock models in your desired region

### Technical Requirements
- You will be executing the application form your local/shared Linux environment.
- Python 3.10 or later
- Access to Amazon Bedrock models enabled

Ensure you have **Python >=3.10 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

## 🚀 Installation

### Step 1: Install CrewAI

If you haven't already, install CrewAI and uv:

```bash
pip install uv crewai
```

### Step 2: Install Dependencies

Navigate to your project directory and install the dependencies:

```bash
crewai install
```

## ⚙️ Customization

### Add Your LLM. Depending on the LLM usage you may need to provide API key for LLM

Add your Preferred LLM Model into the `.env` file to enable API access.
We will be using LLMs via Amazon Bedrock

### Configure Agents and Tasks

- `config/agents.yaml` defines your agents.
- `config/tasks.yaml` defines your tasks.
- `tools/brAgentTool.py` custom tool to talk with Amazon Bedrock Knowledge Base
- `crew.py` Executes the Crew
- `main.py` starting point
- Modify `.env` file add custom arguments for your agents and tasks.

## 🏃 Running the Project

To kickstart your AI agents and begin task execution, run the following command from the root folder of your project:

```bash
crewai run
```

This initializes the **Automate Regulatory Compliance With Multi-Agents Crew**, assembling the agents and assigning them tasks as defined in your configuration. The default setup will generate a `report.md` file in the root folder with a research summary on LLMs.

## 🤖 Understanding Your Crew

The **Automate Regulatory Compliance With Multi-Agents Crew** consists of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on tasks defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## 📞 Support

For questions, support, or feedback regarding CrewAI:

- 📖 Check our [documentation](https://docs.crewai.com)
- 🤖 [Chat with our docs](https://chatg.pt/DWjSBZn)


## 🤝 Contributing
Contributions are welcome! Please read our [Contributing Guidelines](https://console.harmony.a2z.com/CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## 📄 License

This library is licensed under the MIT-0 License. See the LICENSE file.
