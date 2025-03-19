import os
import boto3
import uuid
import logging
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from dotenv import load_dotenv

# Load the .env file from the current directory
load_dotenv()

# Get environment variables
aws_region = os.environ.get('AWS_REGION_NAME')
bedrock_agent_id = os.environ.get('AGENT_ID')
bedrock_agent_alias = os.environ.get('AGENT_ALIAS_ID')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BedrockAgentInput(BaseModel):
    """Input schema for BedrockAgentTool."""
    text: str = Field(..., description="The text query to send to the Bedrock Agent.")

class BedrockAgentTool(BaseTool):
    """Tool for interacting with Amazon Bedrock Agents."""
    
    name: str = "Bedrock Agent Tool"
    description: str = "Get responses from an Amazon Bedrock Agent. Useful for answering questions about specific domains or accessing knowledge bases."
    args_schema: Type[BaseModel] = BedrockAgentInput
    
    def _run(self, text: str) -> str:
        """
        Run the tool with the given input text.
        
        Args:
            text (str): The text query to send to the Bedrock Agent
            
        Returns:
            str: The response from the Bedrock Agent
        """
        if not text or not isinstance(text, str):
            return "Error: Invalid input text provided"
        
        try:
            logger.info(f"Sending query to Bedrock Agent: {text}")
             # Initialize the Bedrock Agent Runtime client
            client = boto3.client("bedrock-agent-runtime", region_name=aws_region)
            
            # Make the API call with a unique session ID
            response = client.invoke_agent(
                agentId=bedrock_agent_id,
                agentAliasId=bedrock_agent_alias,
                sessionId=str(uuid.uuid4()),
                inputText=text
            )
            
            # Process the streaming response
            full_response = ""
            for event in response.get('completion', []):
                if 'chunk' in event and 'bytes' in event['chunk']:
                    full_response += event['chunk']['bytes'].decode('utf-8')
            
            result = full_response.strip() if full_response else "Error: Empty response received"
            logger.info(f"Received response from Bedrock Agent (length: {len(result)})")
            return result
        
        except Exception as e:
            error_message = f"Error: {str(e)}"
            logger.error(error_message)
            return error_message

