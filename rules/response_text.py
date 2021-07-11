#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela

class ResponseText:
    @staticmethod
    def hello():
        return "Hello!! What is your name?"

    @staticmethod
    def whats_your_name(name: str):
        return f"What you need {name}"

    @staticmethod
    def welcome_back(name: str):
        return f"Hello back {name}!"

    @staticmethod
    def list_options_basic():
        return """
        1) Products List
        2) Help
        """

    @staticmethod
    def list_options_advanced():
        return """
                1) Products List
                2) Help
                3) Checkout
                4) Payment
                """