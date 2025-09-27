#!/bin/bash

# Healthcare Policy Compliance Auditor - Start Script
echo "🚀 Starting Healthcare Policy Compliance Auditor..."

# --- Configuration ---
FRONTEND_DIR="frontend"
BACKEND_DIR="backend"

# --- Function to check if a command exists ---
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# --- Backend Setup ---
echo "🐍 Setting up backend..."
cd "$BACKEND_DIR"

# Check for virtual environment
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/upgrade Python dependencies every time to ensure they are up to date
echo "Installing/updating Python dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Start backend server in the background
echo "🔥 Firing up backend server..."
uvicorn main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# --- Frontend Setup ---
echo "🚀 Setting up frontend..."
cd "$FRONTEND_DIR"

# Check and install Node.js dependencies
if [ -d "node_modules" ]; then
    echo "Node.js dependencies are already installed."
else
    echo "Installing Node.js dependencies with npm..."
    npm install
fi

# Start frontend server
echo "🎨 Launching frontend..."
npm run dev &
FRONTEND_PID=$!
cd ..

# --- Cleanup ---
cleanup() {
    echo "🧹 Shutting down servers..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    # Deactivate virtual environment
    if command_exists deactivate; then
        deactivate
    fi
    exit
}

# Trap signals to run cleanup function
trap cleanup SIGINT SIGTERM

# --- Wait for processes to finish ---
echo "✅ App is running! Backend on http://localhost:8000, Frontend on http://localhost:3000"
echo "Press Ctrl+C to stop."
wait $BACKEND_PID
wait $FRONTEND_PID
