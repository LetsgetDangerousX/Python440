# ruff: noqa: INP001
import json
import sys

# the fork this lab is allowed to write to
FORK = "LetsgetDangerousX/Python440"

# commands that change something on GitHub. reading is always allowed.
WRITE_COMMANDS = [
    "git push",
    "gh pr create",
    "gh pr merge",
    "gh issue create",
    "gh issue comment",
]

tool_call = json.load(sys.stdin)
command = tool_call.get("tool_input", {}).get("command", "").lower()

if any(write in command for write in WRITE_COMMANDS):
    if "thealgorithms" in command or "upstream" in command:
        print("Blocked: never write to TheAlgorithms/Python.", file=sys.stderr)
        sys.exit(2)
    if command.startswith("gh") and FORK not in command:
        print(
            "Blocked: add --repo LetsgetDangerousX/Python440 so this goes to the fork.",
            file=sys.stderr,
        )
        sys.exit(2)
