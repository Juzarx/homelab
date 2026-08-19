# Pi-hole DNS records and homepage 2FA lost after infra VM disk filled up — 2026-08-17

**Service:** pihole / homepage
**Duration:** ~1 hour

## What happened
The infra VM's boot disk filled up completely, same LVM under allocation
issue as media and games VM before it. While fixing the disk, noticed no
`.home` domain resolved anymore, only direct ip and port worked. Pihole
container was running fine with no errors in the logs.

## Root cause
Pihole itself was healthy, confirmed it could resolve external domains
fine from inside the container, and port 53 was correctly owned by
docker with no systemd-resolved conflict. Querying pihole directly for
`grimmory.home` returned non-existent domain, the local DNS records were
just gone. Adlists were untouched, only the custom `.home` records and
the homepage widget's 2FA config were lost.

Likely cause: the boot disk being at 100% during the earlier infra VM
problem meant pihole couldn't properly write to its database when it
needed to, silently losing data instead of throwing a visible error.

## Fix
Since traefik routing depends on DNS to even reach services, and pihole's
own admin UI had no port exposed anymore (removed weeks ago after adding
traefik labels), had to temporarily add the port back to reach the admin
panel directly by ip:

```yaml
ports:
  - "8888:80"
```

Re-added every `.home` DNS record pointing to the infra VM's ip, then
removed the temporary port again once `.home` names worked through
traefik normally.

## Lesson learned
A full boot disk isn't just a "can't install things" problem, it can
cause silent data loss on any service that tries to write while the disk
has no room, with zero error shown anywhere in the logs. Worth checking
disk space as a first step whenever something that was working suddenly
isn't, not just as an afterthought.

Also worth remembering: removing a service's exposed port after adding
traefik labels means losing DNS breaks the only way back into that
service's own admin panel, temporarily exposing the port directly is the
way out of that loop.