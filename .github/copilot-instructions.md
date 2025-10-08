## wClub — Copilot guidance (concise)

This is a Frappe app (wClub) targeting Frappe v15+ (see `pyproject.toml` / `requirements.txt`). Below are the key facts an AI coding agent needs to be immediately productive in this repository.

- Project type: Frappe app / Python package. Core dependency: `frappe>=15,<17` (see `pyproject.toml`, `setup.py`).
- App entry points: `wclub/hooks.py` (app metadata, `after_install`, `doc_events`) and `wclub/after_install.py` for post-install setup.

Important directories and conventions
- `wclub/doctype/<name>/` — each DocType has a JSON model (`<name>.json`) and optional server code in `<name>.py`. Example: `wclub/doctype/belt_upgrade/belt_upgrade.json` + `belt_upgrade.py`.
- `wclub/api.py` — whitelisted HTTP-accessible helpers. Functions annotated with `@frappe.whitelist()` are exposed to the client (see `apply_discount`).
- `wclub/public/` — public assets served at `/assets/wclub/` (hooks set `app_logo = "/assets/wclub/images/logo.svg"`).
- `wclub/tests/` — unit tests (currently placeholders). These are plain Python unittest files but many tests will require a running Frappe site.
- `wclub/fixtures/seed_data.json` — data fixtures included for initial installation.

Common patterns and examples (do NOT invent new app structure)
- DocEvents and hooks: `hooks.py` maps DocType events to handlers. Example: `"Belt Upgrade": { "on_submit": "wclub.belt_upgrade.on_submit" }` — handlers receive `(doc, method)` and use `frappe.get_doc()` and `doc.save(ignore_permissions=True)` when mutating other documents.
- Server-side helpers use Frappe utilities: `from frappe.utils import flt` for numeric conversions; use `frappe.get_doc(...)` and `frappe.whitelist()` for HTTP-exposed functions.
- When altering other documents in hooks, code commonly calls `save(ignore_permissions=True)` to bypass permission checks (follow existing pattern).

Integration points and developer workflows (assumptions clarified)
- This repository is a Frappe app and expects a bench / Frappe environment to perform full integration tests and install the app. I assume the usual Frappe workflow (bench commands) is available on developer machines; adapt if your environment differs.
- Quick test guidance (assumption: bench + site available): use bench to run integration tests or to install/reload doctypes. Example (not in repo but standard):
  - bench --site <site> install-app wclub
  - bench --site <site> run-tests --app wclub
  - To reload a changed DocType JSON: bench --site <site> reload-doc wclub doctype <doctype_name>

What to edit and where
- UI/business logic changes: edit the doctype's `.py` file next to its `.json` (e.g., update `wclub/doctype/belt_upgrade/belt_upgrade.py` when adding server logic for belt upgrades).
- Public assets: add under `wclub/public/` (they'll be served from `/assets/wclub/` after build). `hooks.py` references `/assets/wclub/images/logo.svg`.
- App-level APIs: add to `wclub/api.py` and mark with `@frappe.whitelist()` for client use.

Testing and safety notes
- Many unit/integration tests need a Frappe site and DB. The `wclub/tests` files are plain unittest modules; run them in a configured site or use `bench` for integration runs.
- Keep changes small and consistent with Frappe conventions (do not move DocType JSONs out of `doctype/<name>/`).

Examples from the repo to reference in PRs or edits
- Whitelisted API: `wclub/api.py::apply_discount` — demonstrates `@frappe.whitelist()` and `flt` usage.
- Hook handler: `wclub/belt_upgrade.py::on_submit` — shows updating another DocType (`Member`) and `save(ignore_permissions=True)`.
- Hooks mapping: `wclub/hooks.py` — place to add app-level event bindings.

Marketplace Checklist (Frappe Cloud)
- Ensure `app.json` contains `website`, `support_url`, and `privacy_policy_url`. This repo now sets `support_url` and `privacy_policy_url` (see `app.json`).
- Provide a privacy policy file at the `privacy_policy_url` (this repo includes `PRIVACY.md`).
- Add a square logo >=200x200px to `wclub/public/images/` and reference it from `hooks.py` via `app_logo` (currently `wclub/public/images/logo.svg`).
- Prepare 3-6 screenshots in `wclub/public/images/` and a short demo video describing core flows (membership, belt upgrade, payments).
- Short description (40-80 chars) and long description go in the Marketplace submission UI (use `README.md` long description and the `app_title`/`app_description` in `app.json`).

If something is unclear or requires environment-specific steps (bench path, site name, CI instructions), ask for the preferred developer environment and I will update these instructions accordingly.

End of concise guidance — request feedback for missing environment details or CI commands.
