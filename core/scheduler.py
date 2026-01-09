from core.context import ExecutionContext
from utils.monitor import should_throttle

class PhaseScheduler:
    def __init__(self, config):
        self.config = config
        self.current_phase = "stealth"

    def get_context(self):
        return ExecutionContext(self.current_phase, self.config)

    def can_promote(self, stats: dict, findings: list) -> bool:
        if should_throttle(stats):
            return False
        return len(findings) >= 1

    def promote(self):
        if self.current_phase == "stealth":
            self.current_phase = "normal"

