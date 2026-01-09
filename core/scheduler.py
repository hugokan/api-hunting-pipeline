from core.context import ExecutionContext
from utils.monitor import should_throttle

class PhaseScheduler:
    def __init__(self, config):
        self.config = config
        self.current_phase = "stealth"
        self.results = []

    def get_context(self):
        return ExecutionContext(self.current_phase, self.config)

    def can_promote(self, stats, findings):
        if should_throttle(stats):
            return False

        if len(findings) >= 3:
            return True

        return False

    def promote(self):
        if self.current_phase == "stealth":
            self.current_phase = "normal"
