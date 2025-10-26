#!/usr/bin/env bash
set -e
echo "🚀 Starting all services..."

# --- Cleanup existing backend Docker container ---
echo "🧹 Cleaning up any existing backend containers..."
if [ "$(docker ps -aq -f name=backend_container)" ]; then
    docker rm -f backend_container
fi

# --- Backend ---
echo "🐍 Building and starting backend in Docker..."
docker build -t backend_image -f Dockerfile .
docker run -d --name backend_container -p 8000:8000 --restart unless-stopped backend_image

# --- Frontend ---
echo "🎨 Starting frontend with PM2..."
cd frontend

# Install dependencies if missing
npm install

# Remove existing PM2 frontend process if any
if pm2 list | grep -q "frontend"; then
    pm2 delete frontend
fi

# Start frontend via PM2
pm2 start npm --name "frontend" -- run dev
pm2 save
