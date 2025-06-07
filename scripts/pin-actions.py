#!/usr/bin/env python3
"""
pin-actions.py
---------------
Traverse a repo, find GitHub workflow files, and replace
un-pinned `@v*` refs with the commit SHA of the latest tag.
"""
import sys, subprocess, yaml, pathlib, re, requests

GITHUB_API = "https://api.github.com/repos/{owner}/{repo}/commits?sha={ref}&per_page=1"
_CACHE = {}

def latest_sha(action_ref):
    """Return SHA for actions/checkout@v4 etc."""
    if action_ref in _CACHE:
        return _CACHE[action_ref]
    try:
        owner_repo, ref = action_ref.split("@")
        owner, repo = owner_repo.split("/")
    except ValueError:
        raise ValueError(f"Unexpected format in action reference: {action_ref}")
    url = GITHUB_API.format(owner=owner, repo=repo, ref=ref)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"No commits found for {action_ref} using URL: {url}")
    sha = data[0]["sha"]
    pinned = f"{owner_repo}@{sha}"
    _CACHE[action_ref] = pinned
    return pinned

def pin_file(path: pathlib.Path):
    data = yaml.safe_load(path.read_text())
    changed = False
    for job in data.get("jobs", {}).values():
        for step in job.get("steps", []):
            if "uses" in step and re.match(r".+@v\d+", step["uses"]):
                pinned = latest_sha(step["uses"])
                step["uses"] = pinned
                changed = True
    if changed:
        path.write_text(yaml.dump(data))
        print(f"Pinned -> {path}")

if __name__ == "__main__":
    root = pathlib.Path(".")
    for wf in root.rglob("*.yml"):
        if ".github/workflows" in wf.parts:
            pin_file(wf)
