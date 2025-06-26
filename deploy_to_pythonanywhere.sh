#!/bin/bash
# Script to deploy Jekyll site to PythonAnywhere

# Exit on error
set -e

echo "=== Jekyll Site Deployment to PythonAnywhere ==="
echo "This script will build your Jekyll site and deploy it to your Flask app"

# Step 1: Install Ruby and Jekyll if not already installed
echo "=== Step 1: Installing Ruby and Jekyll ==="
if ! command -v ruby &> /dev/null; then
    echo "Installing Ruby..."
    pip install --user ruby
    export PATH=$PATH:$HOME/.local/bin
fi

if ! command -v jekyll &> /dev/null; then
    echo "Installing Jekyll and Bundler..."
    gem install jekyll bundler
fi

# Step 2: Update repository
echo "=== Step 2: Updating repository ==="
if [ -d "~/risk-mapping" ]; then
    echo "Updating existing repository..."
    cd ~/risk-mapping
    git pull
else
    echo "Cloning repository..."
    cd ~
    git clone https://github.com/yourusername/risk-mapping.git
    cd risk-mapping
fi

# Step 3: Build Jekyll site
echo "=== Step 3: Building Jekyll site ==="
bundle install
bundle exec jekyll build

# Step 4: Create target directory if it doesn't exist
echo "=== Step 4: Setting up target directory ==="
mkdir -p ~/tick-majority/risk-mapping

# Step 5: Copy built files to Flask app directory
echo "=== Step 5: Copying files to Flask app directory ==="
cp -r _site/* ~/tick-majority/risk-mapping/

# Step 6: Update Flask app if app_with_risk_mapping.py exists
echo "=== Step 6: Updating Flask app ==="
if [ -f "tick-majority/app_with_risk_mapping.py" ]; then
    echo "Copying modified Flask app..."
    cp tick-majority/app_with_risk_mapping.py ~/tick-majority/app.py
    echo "IMPORTANT: Remember to update the username and password in app.py"
else
    echo "Modified Flask app not found. Please update your Flask app manually."
fi

echo "=== Deployment Complete ==="
echo "Don't forget to:"
echo "1. Update the username and password in app.py"
echo "2. Reload your web app from the PythonAnywhere dashboard"
echo "3. Test your site at https://matthewderiv.pythonanywhere.com/risk-mapping/"
