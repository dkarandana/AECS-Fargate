from django.db.models import CharField

class NullableCharField(CharField):

    def from_db_value(self, value, expression, connection):
        
        # check is null
        if value is None:
            return None
        else:
        # if not null
            if value.strip() == "":
                return None
            else:
                return value
    
    def to_python(self, value):
        
        # check is null
        if value is None:
            return None
        
        # check is string
        elif isinstance(value, str):

            if value.strip() == "":
                return None
            else:
                return value

        return str(value)

