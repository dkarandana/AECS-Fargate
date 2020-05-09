import logging

from django.db import models
from .fields.char import NullableCharField

class AbstractCategory(models.Model):

    title = NullableCharField(
        unique=True,
        max_length=255,
        help_text="Short descriptive name for this category.",
    )
    
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ("title",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    @property
    def is_parent(self):
        return True if self.parent is None else False

    @property
    def is_child(self):
        return True if self.parent is not None else False


class AbstractSetting(models.Model):

    '''

        @note if you change any choice field you need to migrate db

        copy this all model fields to subclass bcz it need choices
        - KEY_CHOICES
        - VALUE_TYPE_CHOICES
        - STRUCTURE
        please  add this field choices to child class

        # SAMPLE DATA STRUCTURES
        
        VALUE_TYPE_CHOICES = (
            (TYPE_INTEGER, TYPE_INTEGER),
            (TYPE_PRECENTAGE, TYPE_PRECENTAGE)
        )

        KEY_CHOICES = (
            ( KEY_PHOTOGRAPHER_PROFIT_MARGIN, KEY_PHOTOGRAPHER_PROFIT_MARGIN),
            ( KEY_APP_VERSION, KEY_APP_VERSION )
        )

        STRUCTURE = [
            {
                'FIELD_NAME': KEY_PHOTOGRAPHER_PROFIT_MARGIN,
                'FIELD_WIDGET': forms.NumberInput,
                'FIELD_TYPE': forms.CharField,
                'IS_REQUIRED': True,
                'IS_DISABLED': False,
                'VALUE_TYPE': TYPE_PRECENTAGE
            },
            {
                'FIELD_NAME': KEY_APP_VERSION,
                'FIELD_WIDGET': forms.NumberInput,
                'FIELD_TYPE': forms.CharField,
                'IS_REQUIRED': True,
                'IS_DISABLED': False,
                'VALUE_TYPE': TYPE_INTEGER
            }
        ]
    '''

    KEY_CHOICES = ()
    VALUE_TYPE_CHOICES = ()

    # THIS STRUCTURE NEED FOR CREATE FORM
    STRUCTURE = []


    key = models.CharField(choices=KEY_CHOICES, unique=True, max_length=255, verbose_name='Setting Name')
    value_type = models.CharField(choices=VALUE_TYPE_CHOICES, max_length=255, verbose_name='Value Type')
    value = models.CharField(max_length=255, verbose_name="Value")

    class Meta:
        abstract = True
        ordering = ("id",)
        verbose_name = "Setting"
        verbose_name_plural = "Settings"

    def __str__(self):
        return "{{ {}: {}  }}".format(self.key, self.value)


class AbstractLogging(models.Model):
    
    '''
        in sub class add log groups and log streams + log_group and log_stream field
    '''

    LOG_LEVELS = (
        (logging.NOTSET, 'NotSet'),
        (logging.INFO, 'Info'),
        (logging.WARNING, 'Warning'),
        (logging.DEBUG, 'Debug'),
        (logging.ERROR, 'Error'),
        (logging.FATAL, 'Fatal'),
    )

    LOG_GROUPS = ()
    LOG_STREAMS = ()

    log_group = models.CharField(max_length=255, choices=LOG_GROUPS)
    log_stream = models.CharField(max_length=255, choices=LOG_STREAMS)
    level = models.PositiveSmallIntegerField(choices=LOG_LEVELS, default=logging.ERROR, db_index=True)
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return "{} on {}".format(self.log_group, self.log_stream)

    class Meta:
        ordering = ('-create_datetime',)
        abstract = True
        verbose_name_plural = verbose_name = 'Logging'

        