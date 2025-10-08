# wClub (Frappe v15+)

Multi-tenant fighting club SaaS app.

Long description
----------------

wClub is a multi-tenant app for managing fighting clubs: members, belts, classes, coaches, offers and payments. It is implemented as a standard Frappe app (see `wclub/doctype/` for DocType models and `wclub/*.py` for server logic).

Screenshots / Demo
------------------

Place screenshots under `wclub/public/images/` and reference them in the Marketplace submission UI. Prepare a short demo video describing core flows for review.

Windows / PowerShell bench examples
----------------------------------

These are example commands for a typical Frappe bench environment on Windows (adjust paths and site name as needed):

```powershell
# Install the app on a site
bench --site yoursite.local install-app wclub

# Run the app's tests (integration tests require a configured site)
bench --site yoursite.local run-tests --app wclub

# Reload a DocType model after editing the JSON
bench --site yoursite.local reload-doc wclub doctype Belt\ Upgrade
```

Replace `yoursite.local` with your actual site name. If you use WSL or a Linux-based bench, use the equivalent shell commands.
