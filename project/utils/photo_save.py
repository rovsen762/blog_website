import os
import uuid
from django.db import models


def logo_dir_path(instance, filename):
    extension = filename.split('.')[-1]
    model_name = instance.__class__._meta.model_name  
    unique_filename = f"{model_name}_{uuid.uuid4()}.{extension}"
    return os.path.join(model_name, unique_filename)