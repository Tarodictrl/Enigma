class Validator:
    @staticmethod
    def validate_plugboard(plugboard: list[str]):
        plugboard = "".join(plugboard)
        if len(plugboard) != len(set(plugboard)):
            raise ValueError("Pairs of letters to be swapped need to be unique!")
