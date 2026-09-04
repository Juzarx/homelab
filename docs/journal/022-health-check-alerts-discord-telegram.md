# Day 22 - Discord and Telegram alerts for health check

**Date:** 2026-09-03

**Objective:** Add automated alerts to the health check script and schedule it with cron

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 21](./021-persistent-control-panel-and-traefik-routing.md)
- [Discord webhooks docs](https://support.discord.com/hc/en-us/articles/228383668)
- [Telegram bot API docs](https://core.telegram.org/bots/api)

## Setting up Discord alerts
- Created a webhook in the discord channel settings under Integrations.
- Stored the webhook url in the [.env file](/scripts/.env.example), installed python-dotenv to read it.
- Updated the [Healthcheck script](/scripts/healthcheck.py) to collect down services in a list instead of just printing them.
- Added a send_discord_alert function that posts the down services list to the webhook url.
- Tested it stopping pihole on purpose, got the alert message on discord correctly.

## Setting up Telegram alerts
- Created a bot talking to @BotFather on telegram, got a bot token.
- Tried getting the chat id with the getUpdates endpoint, got an empty result at first.
- Realized i had to message the bot directly first, not just search it.
- Got the chat id correctly after messaging it and refreshing the getUpdates url.
- Added the token and chat id to the [.env file](/scripts/.env.example).
- Added a send_telegram_alert function, same idea as discord but posting to the telegram bot api endpoint instead.
- Called both alert functions in main so a service going down notifies both discord and telegram.

## Scheduling with cron
- Added a cron job with `crontab -e` to run the script every 15 minutes.
- Logs output to a health_check.log file for reference.

## Notes
- Took two days to finish this one, wasn't feeling well so had to spread it out more than usual.
- getUpdates on telegram only shows unconsumed messages, checking it again after already reading a message returns empty, needed a fresh message to the bot to see the chat id again.