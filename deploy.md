# Deployment Guide for SAHEL Plast4CE Static Site

This guide explains how to deploy the Django site as a static site to GitHub Pages.

## Overview

The site is converted to static HTML using `django-bakery`. When you push changes to GitHub, GitHub Actions automatically builds and deploys the static site.

## Making Content Updates

### Step 1: Start the Django Development Server

```bash
cd /home/haruna-tijjani-zango/Projects/sahelplast4ce/sahel_plast4ce
source .virtualenv/bin/activate
python manage.py runserver
```

### Step 2: Access Django Admin

Open your browser and go to: `http://127.0.0.1:8000/admin/`

Log in with your admin credentials.

### Step 3: Update Content

Use the Django Admin to:
- **Add/Update Projects**: Go to Plast4ce → Projects
- **Add/Update Gallery Images**: Go to Plast4ce → Gallery Images

### Step 4: Test Locally

# After making changes, test them locally by visiting:
- Home: `http://127.0.0.1:8000/`
- Projects: `http://127.0.0.1:8000/projects/`
- Gallery: `http://127.0.0.1:8000/gallery/`

### Step 5: Build Static Site

Stop the server (Ctrl+C) and run the static build and copy steps.

Prefer the django-bakery command:

```bash
python manage.py build
# fallback if your project used a custom command name
python manage.py build_static || true
python manage.py copy_media_to_build
python manage.py collectstatic --noinput --clear
cp -r static build/
```

### Step 6: Test Static Build

Open `build/index.html` in your browser to verify the static site works correctly.

### Step 7: Commit and Push

```bash
git add .
git commit -m "Update content: [describe your changes]"
git push origin main
```

### Step 8: Automatic Deployment

GitHub Actions will automatically:
1. Build the static site
2. Copy media files
3. Deploy to GitHub Pages

Wait 2-5 minutes for the deployment to complete. Your site will be live at:
`https://[your-username].github.io/[repository-name]/`

## Quick Reference Commands

### Development
```bash
# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate
```

### Building Static Site
```bash
# Build static HTML (django-bakery)
python manage.py build
# fallback for older/custom setups
python manage.py build_static || true

# Copy media files to build directory
python manage.py copy_media_to_build

# Collect static files
python manage.py collectstatic --noinput --clear

# Copy static files to build
cp -r static build/
```

### Deployment
```bash
# Add all changes
git add .

# Commit changes
git commit -m "Update content"

# Push to GitHub
git push origin main
```

## One-command Deployment Script

You can use the helper script `scripts/deploy.sh` to run the build steps, stage, commit and push in one command.

1. Make the script executable (first time):

```bash
chmod +x scripts/deploy.sh
```

2. Run the script from the `sahel_plast4ce` project root with a commit message:

```bash
./scripts/deploy.sh -m "Update content: add projects and images"
```

Flags:
- `--no-build` : skip building static files and copying media/static
- `--no-push`  : only commit locally, do not push to remote

The script executes the sequence:
- `python manage.py build_static` (unless `--no-build`)
- `python manage.py copy_media_to_build`
- `python manage.py collectstatic --noinput --clear`
- copy `static/` into `build/`
- `git add . && git commit -m "..." && git push origin main` (unless `--no-push`)

Use this for a repeatable local workflow before relying on the GitHub Actions automated deployment.

## Important Notes

### Media Files
- Media files (uploaded images) are stored in `/media/` directory
- These files are automatically copied to the build directory during deployment
- Ensure media files are committed to git if you want them deployed

### Static Files
- Static files (CSS, JS, images) are in `/static/` directory
- These are automatically copied to the build directory

### Database
- The database (`db.sqlite3`) is used only for local development
- During GitHub Actions build, migrations are run and demo content is loaded
- Any database changes must be reflected in migrations

### URL Structure
- Static site uses absolute paths (e.g., `/about/`, `/projects/`)
- No Django URL routing in the deployed static site

### Limitations
- **No Admin Panel**: The deployed static site has no admin panel
- **No Forms**: Contact forms and other dynamic features won't work
- **No Authentication**: User authentication is not available
- **Content Updates**: Require rebuilding and redeploying

## Troubleshooting

### Build Fails
- Check that `django-bakery` is installed: `pip install django-bakery`
- Verify bakery views are correctly configured in `settings.py`
- Check for template errors

### Media Files Not Showing
- Ensure media files exist in `/media/` directory
- Run `python manage.py copy_media_to_build` manually
- Verify media files are in the build directory

### GitHub Actions Fails
- Check the Actions tab in GitHub for error logs
- Ensure `requirements.txt` is up to date
- Verify all bakery views are correctly implemented

### Links Not Working
- Ensure all links use absolute paths (e.g., `/about/`)
- Check that breadcrumb templates use static paths
- Verify header navigation uses static paths

## File Structure

```
sahel_plast4ce/
├── apps/
│   └── plast4ce/
│       ├── bakery_views.py      # Bakery view classes for static export
│       ├── management/
│       │   └── commands/
│       │       └── copy_media_to_build.py  # Media file export command
│       └── ...
├── config/
│   └── settings.py             # Bakery configuration
├── static/                     # Static assets (CSS, JS, images)
├── media/                      # Uploaded media files
├── templates/                  # Django templates
├── build/                      # Generated static site (gitignored)
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── requirements.txt            # Python dependencies
└── deploy.md                   # This file
```

## Support

For issues or questions:
1. Check the GitHub Actions logs for deployment errors
2. Review the bakery views in `apps/plast4ce/bakery_views.py`
3. Verify template paths are correct
4. Ensure all media files are properly uploaded
