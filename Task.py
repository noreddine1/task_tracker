from datetime import datetime

class Task:
    def __init__(self, id: int, description: str, status: str="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "create_at": self.create_at.isoformat(),
            "update_at": self.update_at.isoformat()
        }