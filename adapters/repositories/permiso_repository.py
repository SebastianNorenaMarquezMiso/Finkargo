from infrastructure.persistence.database import Database


class PermisoRepository:
    def __init__(self, db: Database):
        self.db = db

    def add_permiso(self, permiso):
        self.db.execute(
            "INSERT INTO Permisos (nombre, rol_id) VALUES (?, ?)",
            (permiso.nombre, permiso.rol_id)
        )

    def get_permiso(self, id):
        return self.db.fetch_one("SELECT * FROM Permisos WHERE id = ?", (id,))

    def update_permiso(self, permiso):
        self.db.execute(
            "UPDATE Permisos SET nombre = ?, rol_id = ? WHERE id = ?",
            (permiso.nombre, permiso.rol_id, permiso.id)
        )

    def delete_permiso(self, id):
        self.db.execute("DELETE FROM Permisos WHERE id = ?", (id,))
