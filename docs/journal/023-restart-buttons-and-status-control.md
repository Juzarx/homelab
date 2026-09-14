# Day 23 - Restart buttons and status column in control panel

**Date:** 2026-09-10

**Objective:** Update the roadmap and add restart buttons with live status to the control panel

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 22](./022-health-check-alerts-discord-telegram.md)
- [Flask docs](https://flask.palletsprojects.com/)

## Updating the roadmap
- Marked health checks and the minecraft control panel as done in phase 6.
- Dropped the backup scripts item, proxmox already handles vm level backups so no need to duplicate that.
- Restart scripts stayed as the only thing left in phase 6.

## Adding restart buttons
- Updated the [app.py file](/scripts/app.py) with a generic restart route using vm and container as url parameters instead of one route per service.
- Added a VM_HOSTS dictionary mapping each vm to its ssh host, infra uses localhost directly since the control panel runs there.
- Updated the [index.html file](/scripts/templates/index.html) with a table for the restart buttons.
- Updated the [app.js file](/scripts/static/app.js) to build the table dynamically from a services list instead of hardcoding rows.
- Tested restarting homepage first since it's low stakes, worked correctly.

## Adding live status to the table
- Imported the check_http and check_tcp functions directly from [health_check.py](/scripts/health_check.py) into app.py instead of duplicating the logic.
- Added a `/api/services/status` route reusing those functions.
- Updated the table to show each service's status colored green or red next to the restart button.
- Table refreshes itself after a restart so you can see right away if it worked.

## Notes
- Flask route parameters like `<vm>/<container>` let one route handle many services instead of writing a route per service, whatever matches gets passed into the function as arguments.
- Python can import functions from one script into another as long as they're in the same folder, no need to duplicate the health check logic in app.py.