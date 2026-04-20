# Pupstertech Offline Command Center Stack

This repository contains a starter blueprint for a portable offline-first business stack:

- Odoo Community (`odoo`) + PostgreSQL (`postgres_odoo`)
- Local assistant service backed by Ollama (`assistant_api` + `ollama`)
- Long-term memory store (`qdrant`)
- Odoo addon skeleton for unified launcher + planning/reminders (`command_center`)
- Systemd unit for auto-start on bootable external media

## Quickstart

1. Install Docker + Docker Compose.
2. Copy `.env.example` to `.env` and adjust values.
3. Run:
   ```bash
   ./scripts/bootstrap_offline.sh
   ```
4. Open Odoo at `http://localhost:8069`.
5. In Odoo, install the `Command Center` app (from extra addons path).

## Boot on External SSD/USB

- Install Ubuntu Server to the external drive.
- Clone this repository to `/opt/pupstertech-stack`.
- Enable the service:
  ```bash
  sudo cp deploy/systemd/odoo-stack.service /etc/systemd/system/
  sudo systemctl daemon-reload
  sudo systemctl enable odoo-stack.service
  sudo systemctl start odoo-stack.service
  ```

## What this starter includes

### Odoo command_center addon (skeleton)

- `cc.external.app` model for app tiles/links
- `cc.plan.note` model for planning summaries
- `cc.reminder` model for reminders
- Basic menu + tree/form for external apps

### Assistant API (starter endpoints)

- `GET /health`
- `POST /chat`
- `POST /reminders/create`
- `GET /briefing/daily`

## Next implementation steps

- Add Odoo web client integration button for assistant chat.
- Persist reminders/notes in Postgres from `assistant_api`.
- Add scheduler delivery channels (Odoo inbox, email, desktop notifications).
- Add enterprise app replacement catalog and ranking pipeline.
