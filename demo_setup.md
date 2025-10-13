## Demo Setup

```bash
bench get-app https://github.com/ealnuman/wclub.git
bench --site your.site install-app wclub
bench --site your.site migrate
```
The patch `wclub.patches.v1.initial_seed` creates:
- Club: Demo Club
- Dojo: Main Dojo
- Members: Ali Saud, Noura Faisal
- Class Types: Kids Beginner, Adults Beginner
- Belt Levels: White, Yellow
- Two sessions for tomorrow

Routes to try: `/portal/my-bookings`, `/portal/book`, `/portal/certificates`, `/coach/dashboard`, `/kiosk/checkin`.
