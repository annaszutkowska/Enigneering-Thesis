from src.custom_intent_handler.abstract_intent import AbstractIntent


class FallbackIntent(AbstractIntent):

    def generate_response(self) -> str:
        return f"Sorry, I don't recognise your question."
