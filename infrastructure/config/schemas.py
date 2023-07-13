# infrastructure/config/schemas.py
TOKEN_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "usuario": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["usuario", "password"]
}

MATRIZ_SCHEMA = {
    "type": "object",
    "properties": {
        "sin clasificar": {
            "type": "array",
            "items": {"type": "number"}
        }
    },
    "required": ["sin clasificar"],
    "additionalProperties": False
}

BALANCE_SCHEMA = {
  "type": "object",
  "properties": {
    "Mes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "Ventas": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "Gastos": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  },
  "required": ["Mes", "Ventas", "Gastos"]
}

USER_SHEMA = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "correo": {"type": "string", "format": "email"},
        "rol_id": {"type": "integer"}
    },
    "required": ["nombre", "correo", "rol_id"]
}

USER_UPDATE_SHEMA = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "correo": {"type": "string", "format": "email"},
        "rol_id": {"type": "integer"}
    },
    "required": []
}

ROL_SHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "nombre": {"type": "string"}
    },
    "required": ["id", "nombre"]
}

PERMISO_SHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "nombre": {"type": "string"}
    },
    "required": ["id", "nombre"]
}
