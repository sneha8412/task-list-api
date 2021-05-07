from flask import current_app
from app import db
#from .models.goal import Goal #wave 6

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)

    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True) #wave 6
    
    is_complete = False #wave 3
    
    def compute_is_complete(self):
        if self.completed_at == None:
            return False
        else:
            return True #wave 3
    
    #Create an instance method in Task named to_json()
    def to_json(self):
        
        return {
                "task":     
                       {
                            "id": self.task_id,
                            "title": self.title,
                            "description": self.description,
                            "is_complete": self.compute_is_complete()
                        }
                     }
        
    def to_json_no_key(self):    
                return {
                            "id": self.task_id,
                            "title": self.title,
                            "description": self.description,
                            "is_complete": self.compute_is_complete()
                        }
    
    #optional enhancement Create a class method in Task named from_json(): Converts JSON into a new instance of Task
    
    
    def to_string(self):
        return f"{self.task_id}: {self.title} Description: {self.description} completed at {self.completed_at} " 