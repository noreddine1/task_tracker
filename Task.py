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
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        try:
            id = data.get('id')
            if id is None:
                raise ValueError("Missing 'id' in data.")
            id = int(id)
            description = data.get('description', '')
            status = data.get('status', 'todo')
            created_at_str = data.get('created_at')
            updated_at_str = data.get('updated_at')
            created_at = datetime.fromisoformat(created_at_str) if created_at_str else datetime.now()
            updated_at = datetime.fromisoformat(updated_at_str) if updated_at_str else datetime.now()
        except Exception as e:
            raise ValueError(f"Invalid data for Task: {e}")
        task = cls(id, description, status)
        task.created_at = created_at
        task.updated_at = updated_at
        return task

