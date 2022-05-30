#!/bin/bash

# bash script to prepare your django environment
# - verify you have a running Python3 version on your computer
# - if virtual environment not exists in the project, it will created and requirements dependencies installed
echo "Verify if Python 3 is installed..."
command -v python3 >/dev/null 2>&1 && echo Python 3 is installed
if [ $? -eq 1 ] 
then
    echo "You need a running Python3 in your computer to run this project."
    exit 1
fi

echo "Creating virtual environment (venv)..."
if [ ! -d 'venv' ];
then
    python3 -m venv venv
    if [ $? -eq 1 ] 
    then
        echo "Vritual environment created."
    fi
else
    echo "Virtual environment already exsists."
fi

echo "Activate virtual environment"
activate () {
  . ./venv/bin/activate
}

activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Bootstrap completed!"
echo "To run the server type 'make local-run'."

exit 0