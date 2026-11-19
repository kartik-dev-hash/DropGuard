@echo off
title DropGuard - Start All Services

echo =====================================================
echo   DropGuard - Student Dropout Prevention System
echo   Starting all services...
echo =====================================================
echo.

REM Start MongoDB
echo [1/3] Starting MongoDB...
start "MongoDB" "C:\Program Files\MongoDB\Server\8.2\bin\mongod.exe" --dbpath "d:\StudentDropout\data\db_store" --logpath "d:\StudentDropout\mongod.log" --logappend
timeout /t 3 /nobreak >nul
echo       MongoDB started on port 27017

REM Start Backend
echo [2/3] Starting Backend (Node.js)...
cd /d "d:\StudentDropout\studentDropout\Backend"
start "Backend API" node app.js
timeout /t 3 /nobreak >nul
echo       Backend started on port 5000

REM Start Frontend
echo [3/3] Starting Frontend (Vite)...
cd /d "d:\StudentDropout\studentDropout"
start "Frontend" npm run dev
timeout /t 3 /nobreak >nul
echo       Frontend started on port 5173

echo.
echo =====================================================
echo   All services started!
echo.
echo   Frontend:  http://localhost:5173
echo   Backend:   http://localhost:5000
echo   MongoDB:   mongodb://127.0.0.1:27017/studentDropout
echo.
echo   Accounts (all password: 1234)
echo   Platform Admin:  admin@platform.com
echo   Counselor:       counselor@demo.com
echo   Student:         student@demo.com
echo =====================================================
echo.
pause
