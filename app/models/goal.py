from flask import current_app
from app import db

#WAVE 1
class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    
    #WAVE 6
    tasks = db.relationship('Task', backref='goal', lazy=True) 
    
    
    def to_json_goal(self):
        
        return {
                "goal":     
                       {
                            "id": self.goal_id,
                            "title": self.title,
                        }
                     }
        
        
    def to_json_goal_no_key(self):    
                return {
                            "id": self.goal_id,
                            "title": self.title
                        }
                
                
    # optional enchancement: This method is marked static because it does not operate on current instance, instead it creates a new instance from json 
    @staticmethod
    def from_json(goal_json):
        return Goal(title=goal_json["title"])