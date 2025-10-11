#!/usr/bin/env bash
echo "🚀 Starting all services..."

# --- Cleanup ---
trap 'echo "🧹 Shutting down all services..."; kill $(jobs -p) &>/dev/null' EXIT

# --- Backend Setup & Start ---
(
    echo "🐍 Initializing backend..."
    cd backend
    # Create venv only if it doesn't exist, using a specific Python version
    if [ ! -d "venv" ]; then
        python3.13 -m venv venv
    fi
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
) &

# --- Frontend Setup & Start ---
(
    echo "🎨 Initializing frontend..."
    cd frontend
    npm install
    npm run dev
) &

# --- Wait for processes ---
echo ""
echo "✅ App is running! Backend on http://localhost:8000, Frontend on http://localhost:3000"
echo "Press Ctrl+C to stop."

wait -n