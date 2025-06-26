# Deploying Your Jekyll Site to PythonAnywhere as a Subpath

This guide explains how to deploy your Jekyll site to PythonAnywhere as a subpath of your existing Flask application with password protection.

## Prerequisites

- A PythonAnywhere account with an existing Flask web app
- Access to your PythonAnywhere dashboard
- Your Jekyll site repository

## Step 1: Build Your Jekyll Site on PythonAnywhere

1. Open a Bash console on PythonAnywhere (Dashboard > Consoles > Bash)

2. Install Ruby and Jekyll:
   ```bash
   pip install --user ruby
   export PATH=$PATH:$HOME/.local/bin
   gem install jekyll bundler
   ```

3. Clone your repository:
   ```bash
   cd ~
   git clone https://github.com/yourusername/risk-mapping.git
   cd risk-mapping
   ```

4. Make sure your `_config.yml` has the correct baseurl:
   ```yaml
   baseurl: "/risk-mapping"
   ```

5. Build your Jekyll site:
   ```bash
   bundle install
   bundle exec jekyll build
   ```
   This will generate the `_site` directory with all your static files.

## Step 2: Set Up Your Jekyll Site on PythonAnywhere

1. Create a directory for your Jekyll site in your Flask app directory:
   ```bash
   mkdir -p /home/matthewderiv/tick-majority/risk-mapping
   ```

2. Copy the built files to your Flask app directory:
   ```bash
   cp -r ~/risk-mapping/_site/* /home/matthewderiv/tick-majority/risk-mapping/
   ```

## Step 3: Update Your Flask Application

1. Replace your existing `app.py` with the modified version that includes the risk-mapping route and password protection:
   - Upload `app_with_risk_mapping.py` to your PythonAnywhere directory
   - Rename it to `app.py` (or update your WSGI file to point to the new file)

2. **Important**: Change the default username and password in the app.py file:
   ```python
   USERNAME = 'your_chosen_username'
   PASSWORD = 'your_secure_password'
   ```

## Step 4: Reload Your Web App

1. Go to the Web tab in your PythonAnywhere dashboard
2. Click the "Reload" button for your web app

## Step 5: Test Your Setup

1. Visit your main site: `https://matthewderiv.pythonanywhere.com/`
   - This should work as before, with no password protection

2. Visit your Jekyll site: `https://matthewderiv.pythonanywhere.com/risk-mapping/`
   - You should be prompted for a username and password
   - After authentication, you should see your Jekyll site

## Troubleshooting

If you encounter issues:

1. **404 errors**: Make sure the `risk-mapping` directory exists and contains your Jekyll site files

2. **Authentication issues**: Check that the username and password in app.py are correct

3. **Path issues**: Ensure your Jekyll site was built with the correct baseurl

4. **Permission issues**: Make sure the files in the risk-mapping directory are readable by the web app

5. **Check the error logs**: In PythonAnywhere, go to the Web tab and check the error logs

## Security Considerations

- The current implementation uses HTTP Basic Authentication, which is simple but sends credentials with each request
- Make sure your PythonAnywhere site uses HTTPS (they provide this by default)
- For better security, consider storing credentials in environment variables rather than in the code
