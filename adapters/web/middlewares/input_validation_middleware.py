from flask import abort
from jsonschema import validate, exceptions


class InputValidationMiddleware:
    @staticmethod
    def validate(data, schema):
        # Validar la estructura
        try:
            validate(data, schema)
        except exceptions.ValidationError:
            abort(400)
