from django.forms import ValidationError


def validate_file_size(file : object) -> None:
    MAX_SIZE = 3 * 1024 * 1024

    if file.size > MAX_SIZE:
        raise ValidationError(f'File size cannot exceed {MAX_SIZE}KB')