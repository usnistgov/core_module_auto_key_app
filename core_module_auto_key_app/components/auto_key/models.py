"""
AutoKey models
"""
from django_mongoengine import fields, Document
from mongoengine import errors as mongoengine_errors
from mongoengine.queryset.base import CASCADE

from core_main_app.commons import exceptions
from core_parser_app.components.data_structure_element.models import (
    DataStructureElement,
)


class AutoKey(Document):
    """Auto Key keeps track of keys"""

    root = fields.ReferenceField(
        DataStructureElement, reverse_delete_rule=CASCADE, unique=True
    )
    keys = fields.DictField(default={}, blank=True)

    @staticmethod
    def get_by_root(root):
        """Return the object with the given root.

        Args:
            root:

        Returns:
            Data (obj): Data object with the given id

        """
        try:
            return AutoKey.objects.get(root=root)
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))
