#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"
cp -n .env.example .env || true

echo "[1/4] Pulling container images..."
docker compose pull

echo "[2/4] Starting core stack..."
docker compose up -d postgres_odoo odoo ollama qdrant assistant_api scheduler

echo "[3/4] Pulling local AI model via Ollama..."
docker exec ollama ollama pull "${OLLAMA_MODEL:-qwen2.5:7b-instruct}"

echo "[4/4] Finished. Open http://localhost:8069"
