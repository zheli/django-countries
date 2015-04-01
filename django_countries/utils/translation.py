from django.utils.translation import get_language
from django.utils.translation import activate, deactivate, deactivate_all

class override(object):
    def __init__(self, language, deactivate=False):
        self.language = language
        self.deactivate = deactivate
        self.old_language = get_language()

    def __enter__(self):
        if self.language is not None:
            activate(self.language)
        else:
            deactivate_all()

    def __exit__(self, *args, **kwargs):
        if self.deactivate:
            deactivate()
        else:
            activate(self.old_language)
