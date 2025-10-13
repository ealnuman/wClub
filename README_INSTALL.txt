wClub – Direct Install Package (v1.0.0)

Quick setup
-----------
1) bench get-app /path/to/wclub_install.zip
2) bench --site your.site install-app wclub
3) bench --site your.site migrate
4) Login and open /portal/my-bookings or /coach/dashboard

Post-install validation
-----------------------
bench --site your.site execute "frappe.get_all('Member', fields=['name','first_name','club'])"
If empty, run:
bench --site your.site execute "wclub.wclub.patches.v1.initial_seed.execute"
