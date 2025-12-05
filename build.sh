#!/bin/bash

echo "=========================================="
echo "Building Wedding Website (Frontend + Backend)"
echo "=========================================="
echo ""

# Build Frontend
echo "[1/3] Building frontend..."
cd frontend
npm install
npm run build
cd ..

# Check if build was successful
if [ ! -d "backend/frontend_dist" ]; then
    echo "ERROR: Frontend build failed!"
    exit 1
fi

echo ""
echo "[2/3] Frontend built successfully!"
echo ""

# Install backend dependencies
echo "[3/3] Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

echo ""
echo "=========================================="
echo "Build completed successfully!"
echo "=========================================="
echo ""
echo "Frontend files are in: backend/frontend_dist"
echo "You can now run the backend with:"
echo "  cd backend && uvicorn app.main:app --reload"
echo ""

