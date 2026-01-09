def should_throttle(stats: dict) -> bool:
    return stats.get("429_rate", 0) > 0.1 or stats.get("403_rate", 0) > 0.3

