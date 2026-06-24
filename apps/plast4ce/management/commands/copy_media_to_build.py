import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Copy media files to build directory for static export'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        build_dir = settings.BUILD_DIR
        build_media_dir = build_dir / 'media'

        self.stdout.write(f'Copying media files from {media_root} to {build_media_dir}')

        # Create build media directory if it doesn't exist
        os.makedirs(build_media_dir, exist_ok=True)

        # Copy all media files
        if media_root.exists():
            for item in media_root.iterdir():
                if item.is_dir():
                    dest_dir = build_media_dir / item.name
                    if dest_dir.exists():
                        shutil.rmtree(dest_dir)
                    shutil.copytree(item, dest_dir)
                    self.stdout.write(f'Copied directory: {item.name}')
                elif item.is_file():
                    shutil.copy2(item, build_media_dir / item.name)
                    self.stdout.write(f'Copied file: {item.name}')
        else:
            self.stdout.write(self.style.WARNING(f'Media directory {media_root} does not exist'))

        self.stdout.write(self.style.SUCCESS('Media files copied successfully'))
