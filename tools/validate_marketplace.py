#!/usr/bin/env python3
"""Simple marketplace metadata validator for wClub

Checks app.json for required marketplace fields and basic asset presence.
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
APP_JSON = ROOT / "app.json"
PUBLIC_IMG = ROOT / "wclub" / "public" / "images"

REQUIRED_FIELDS = ["app_name", "app_title", "app_publisher", "app_description", "app_email", "app_license", "website", "support_url", "privacy_policy_url"]


def main():
    if not APP_JSON.exists():
        print("ERROR: app.json not found", file=sys.stderr)
        return 2

    data = json.loads(APP_JSON.read_text())
    missing = [f for f in REQUIRED_FIELDS if f not in data or not data.get(f)]
    if missing:
        print("ERROR: app.json is missing required fields:", ", ".join(missing), file=sys.stderr)
        return 3

    # Check logo and screenshots
    logo_candidates = [PUBLIC_IMG / "logo.svg", PUBLIC_IMG / "logo.png", PUBLIC_IMG / "app_logo.png", PUBLIC_IMG / "app_logo.svg"]
    if not any(p.exists() for p in logo_candidates):
        print("WARN: No logo file found in wclub/public/images/. Add a square >=200x200px logo.")

    screenshots = list(PUBLIC_IMG.glob("screenshot-*.svg")) + list(PUBLIC_IMG.glob("screenshot-*.png"))
    if len(screenshots) < 1:
        print("WARN: No screenshots found in wclub/public/images/. Add 3-6 screenshots for Marketplace listing.")

    print("Marketplace metadata validation: PASS (warnings may be present)")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
