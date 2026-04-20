import time
from datetime import UTC, datetime


def tick() -> None:
    print(f"[scheduler] heartbeat={datetime.now(UTC).isoformat()}", flush=True)


if __name__ == "__main__":
    while True:
        tick()
        time.sleep(60)
