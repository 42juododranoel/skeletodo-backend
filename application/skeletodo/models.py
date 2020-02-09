from django.db import models


class BaseModel(models.Model):
    """
    Inherit all models from this model.

    Store methods and stuff common for all models.
    """

    class Meta:
        abstract = True

    def update(self, **attributes):
        """
        Update self attributes and save.

        Use in tests to reduce code amount.
        """
        for name in attributes:
            setattr(self, name, attributes[name])
        else:
            self.save()
