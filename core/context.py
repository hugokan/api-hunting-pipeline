class ExecutionContext:
    def __init__(self, mode: str, config: dict):
        self.mode = mode
        self.rules = config["modes"][mode]

    def allow(self, feature: str) -> bool:
        return self.rules["allow"].get(feature, False)

