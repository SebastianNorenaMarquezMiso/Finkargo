from infrastructure.persistence.database import Database


class RolRepository:
    def __init__(self, db: Database):
        self.db = db

    def rol_exists(self, rol_id):
        return self.db.fetch_one("SELECT * FROM Roles WHERE id = :rol_id", {"rol_id": rol_id}) is not None

    def add_rol(self, rol):
        self.db.execute(
            "INSERT INTO Roles (nombre) VALUES (?)",
            (rol.nombre,)
        )

    def get_rol(self, id):
        return self.db.fetch_one("SELECT * FROM Roles WHERE id = "+str(id))

    def update_rol(self, rol):
        self.db.execute(
            "UPDATE Roles SET nombre = ? WHERE id = ?",
            (rol.nombre, rol.id)
        )

    def delete_rol(self, id):
        self.db.execute("DELETE FROM Roles WHERE id = ?", (id,))
