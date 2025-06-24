# Deploying to Vercel

This document provides instructions for deploying this Jekyll site to Vercel with password protection.

## Prerequisites

- A Vercel account (sign up at [vercel.com](https://vercel.com))
- Your GitHub repository connected to Vercel

## Deployment Steps

1. **Sign up or log in to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up or log in with your GitHub account

2. **Import your repository**
   - Click "Add New..." → "Project"
   - Select your GitHub repository
   - Authorize Vercel to access your repository if prompted

3. **Configure project settings**
   - Framework Preset: Select "Jekyll"
   - Build Command: `jekyll build` (should be auto-detected)
   - Output Directory: `_site` (should be auto-detected)
   - Root Directory: Leave as `.`
   - Click "Deploy"

4. **Add password protection (optional)**
   - After deployment, go to your project settings
   - Navigate to "Security" → "Password Protection"
   - Enable password protection
   - Set a password
   - Save changes

## Vercel Configuration

This repository includes a `vercel.json` file with basic configuration:

```json
{
  "build": {
    "env": {
      "JEKYLL_ENV": "production"
    }
  },
  "framework": "jekyll"
}
```

## Troubleshooting

If you encounter build issues:

1. Check the build logs in Vercel
2. Ensure your Jekyll dependencies are correctly specified in the Gemfile
3. Try adding a `.ruby-version` file if Vercel is using the wrong Ruby version

## Custom Domain (Optional)

To use a custom domain:

1. Go to your project settings in Vercel
2. Navigate to "Domains"
3. Add your custom domain
4. Follow the instructions to configure DNS settings
