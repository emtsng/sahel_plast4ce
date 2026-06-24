#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)/.."
cd "$REPO_DIR"

MSG=""
DO_BUILD=1
DO_PUSH=1

usage() {
  cat <<EOF
Usage: $0 -m "commit message" [--no-build] [--no-push]

Options:
  -m MESSAGE     Commit message to use
  --no-build     Skip running build_static and copying media/static
  --no-push      Skip pushing to remote (only commit locally)
  -h, --help     Show this help
EOF
  exit 1
}

if [ "$#" -eq 0 ]; then
  usage
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    -m)
      shift
      MSG="$1"
      shift
      ;;
    --no-build)
      DO_BUILD=0
      shift
      ;;
    --no-push)
      DO_PUSH=0
      shift
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "Unknown arg: $1"
      usage
      ;;
  esac
done

if [ -z "$MSG" ]; then
  echo "Error: commit message is required (-m)"
  exit 2
fi

echo "Repository root: $REPO_DIR"

if [ "$DO_BUILD" -eq 1 ]; then
  echo "Running static build (try 'build' then 'build_static')..."
  if python manage.py build; then
    echo "Managed to run 'manage.py build'"
  elif python manage.py build_static; then
    echo "Managed to run 'manage.py build_static' (fallback)"
  else
    echo "Error: neither 'manage.py build' nor 'manage.py build_static' succeeded"
    exit 3
  fi

  echo "Copying media to build..."
  python manage.py copy_media_to_build

  echo "Collecting static files..."
  python manage.py collectstatic --noinput --clear

  echo "Copying static to build/"
  rm -rf build/static || true
  cp -r static build/ || true
fi

echo "Staging changes..."
git add .

echo "Committing..."
if git commit -m "$MSG"; then
  echo "Committed." 
else
  echo "No changes to commit." 
fi

if [ "$DO_PUSH" -eq 1 ]; then
  echo "Pushing to origin main..."
  git push origin main
fi

echo "Done."
