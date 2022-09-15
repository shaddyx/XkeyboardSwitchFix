#!/bin/sh

pyinstaller --onefile main.py
cp ./xkblayout-state dist/xkblayout-state
cp ./runBinary.sh dist/run.sh
chmod +x dist/run.sh

