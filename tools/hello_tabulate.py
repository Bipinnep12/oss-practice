
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(
    description="Display a small introduction to Nepal."
)

parser.add_argument("--name", default="World")
args = parser.parse_args()

rows = [
    ["Welcome", f"Namaste, {args.name}!"],
    ["Country", "Nepal"],
    ["Capital", "Kathmandu"],
    ["Open-source tool", "tabulate"],
    ["My goal", "Learn Python and contribute to open source"],
]

print("\nMy Python and Open Source Journey")
print(tabulate(
    rows,
    headers=["Topic", "My Information"],
    tablefmt="grid"
))
