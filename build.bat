@echo off
echo ==========================================
echo Building Wedding Website (Frontend + Backend)
echo ==========================================
echo.

REM Build Frontend
echo [1/3] Building frontend...
cd frontend
call npm install
if errorlevel 1 (
    echo ERROR: npm install failed!
    exit /b 1
)

call npm run build
if errorlevel 1 (
    echo ERROR: Frontend build failed!
    exit /b 1
)
cd ..

REM Check if build was successful
if not exist "backend\frontend_dist" (
    echo ERROR: Frontend build directory not found!
    exit /b 1
)

echo.
echo [2/3] Frontend built successfully!
echo.

REM Install backend dependencies
echo [3/3] Installing backend dependencies...
cd backend
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: pip install failed!
    exit /b 1
)
cd ..

echo.
echo ==========================================
echo Build completed successfully!
echo ==========================================
echo.
echo Frontend files are in: backend\frontend_dist
echo You can now run the backend with:
echo   cd backend ^&^& uvicorn app.main:app --reload
echo.
pause

