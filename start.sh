#!/usr/bin/env bash
echo "🚀 Starting all services..."

# --- Backend ---
echo "🐍 Starting backend in Docker..."
docker build -t backend_image -f Dockerfile .
docker run -d --name backend_container -p 8000:8000 --restart unless-stopped backend_image

# --- Frontend ---
echo "🎨 Starting frontend with PM2..."
cd frontend
npm install
pm2 start npm --name "frontend" -- run dev
pm2 save