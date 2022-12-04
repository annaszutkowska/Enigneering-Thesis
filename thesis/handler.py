import logging
from typing import Dict, Any

from src.event_handler.intent_request_handler import IntentRequestHandler
from src.event_handler.launch_request_handler import LaunchRequestHandler


def lambda_handler(event: Dict[str, Any], context: str) -> str:
    logging.Logger(context)
    request_type = event['request']['type']
    if request_type == "LaunchRequest":
        handler = LaunchRequestHandler(event['request'])
    elif request_type == "IntentRequest":
        handler = IntentRequestHandler(event['request'])
    else:
        handler = IntentRequestHandler(event['request'])
    return handler.get_response()
