from .abstract_intent import AbstractIntent


class HelpIntent(AbstractIntent):

    def generate_response(self) -> str:
        return f"You can ask me about the state of any hydroponics module. How can I help you?"
