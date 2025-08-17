import requests
import json
from datetime import datetime, timedelta

def get_user_contributions(username):
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)
    response.raise_for_status()
    events = response.json()

    contributions = {}
    for event in events:
        if event["type"] == "PushEvent":
            date = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()
            contributions[date] = contributions.get(date, 0) + len(event["payload"]["commits"])
    return contributions

def generate_heatmap_markdown(contributions):
    today = datetime.now().date()
    start_date = today - timedelta(days=365) # Last 365 days

    heatmap_md = """<p align="center">
  <img src="https://ghchart.rshah.org/" alt="GitHub Contribution Chart" />
</p>

```text
"""

    # This is a placeholder. A real heatmap would require more complex rendering.
    # For now, we'll just list recent contributions.
    recent_contributions = []
    for i in range(30):
        date = today - timedelta(days=i)
        if date in contributions:
            recent_contributions.append(f"{date}: {contributions[date]} commits")

    if recent_contributions:
        heatmap_md += "Recent Contributions:\n"
        for entry in recent_contributions:
            heatmap_md += f"- {entry}\n"
    else:
        heatmap_md += "No recent contributions to display.\n"

    heatmap_md += """
```
"""
    return heatmap_md

if __name__ == "__main__":
    username = "MOATAZQ24"
    contributions = get_user_contributions(username)
    heatmap_md = generate_heatmap_markdown(contributions)

    with open("README.md", "r+") as f:
        content = f.read()
        # Replace the placeholder with the generated heatmap
        new_content = content.replace(
            "## Contribution Heatmap Overlay\n\n(This section will be dynamically updated by GitHub Actions.)",
            f"## Contribution Heatmap Overlay\n\n{heatmap_md}"
        )
        f.seek(0)
        f.write(new_content)
        f.truncate()


