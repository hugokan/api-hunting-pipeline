def should_throttle(stats):
    if stats.get("429_rate", 0) > 0.1:
        return True
    if stats.get("403_rate", 0) > 0.3:
        return True
    return False
