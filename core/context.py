class ExecutionContext:
    def __init__(self, mode, config):
        self.mode = mode
        self.rules = config["modes"][mode]

    def allow(self, feature):
        return self.rules["allow"].get(feature, False)
