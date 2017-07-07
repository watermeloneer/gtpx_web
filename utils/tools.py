# -*- coding: utf-8 -*-
"""通用工具"""
import os
import uuid
from datetime import datetime


def get_file_path(instance, filename):
    folder = instance.__class__.__name__.lower()  + datetime.now().strftime("/%Y/%m/%d")
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(folder, filename)