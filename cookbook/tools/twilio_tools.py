from phi.agent import Agent
from phi.tools.twilio import TwilioTools

"""
Example showing how to use the Twilio Tools with Phi.

Requirements:
- Twilio Account SID and Auth Token (get from console.twilio.com)
- A Twilio phone number
- pip install twilio

Usage:
- Set the following environment variables:
    export TWILIO_ACCOUNT_SID="your_account_sid"
    export TWILIO_AUTH_TOKEN="your_auth_token"

- Or provide them when creating the TwilioTools instance
"""

twilio_tools = TwilioTools()

agent = Agent(
    instructions=[
        """You can help users by:
        - Sending SMS messages
        - Making phone calls
        - Checking message history
        - Generating TwiML responses using twilio_tools
        
        Always confirm before sending messages or making calls."""
    ],
    tools=[twilio_tools],
    show_tool_calls=True,
)

agent.print_response("Can you send an SMS saying 'Your package has arrived' to +1234567890?")