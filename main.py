"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence to /output/entry.txt: a pitch that would convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun. Deterministic, standard library only, no network.
"""

import os

PITCH = (
    "Describe that app idea you've been carrying around for months to an "
    "AI agent on make.fun and it'll build you a working first version; "
    "you just describe it, it does the building."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
