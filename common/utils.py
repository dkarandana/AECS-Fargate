import json
import decimal

def parse_int(value):

    """
        parse value and convert it to integer
    """

    try:
        return_value = int(value)
    except Exception:
        return None
    else:
        return return_value

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)
