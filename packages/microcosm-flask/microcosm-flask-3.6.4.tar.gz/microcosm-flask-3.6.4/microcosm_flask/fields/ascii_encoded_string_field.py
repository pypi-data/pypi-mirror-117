from marshmallow import fields


"""
AsciiEncodedStringField Marshmallow field
An extension of the marshmallow fields.String that removes unicode
characters on deserialization
"""


class AsciiEncodedStringField(fields.String):
    def _deserialize(self, value, *args, **kwargs):
        if value is not None:
            value_encoded = value.encode("ascii", "ignore")
            value = value_encoded.decode()
        return super()._deserialize(value, *args, **kwargs)
