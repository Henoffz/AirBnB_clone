#!/usr/bin/python3
import models
import uuid
from datetime import datetime

"""
Base class  that defines all common attributes/methods for other classes.
"""

class BaseModel:
    """
    Instantiating BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        initializing instance attributes
        """
        if not kwargs:
            """proceed with initialization"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.stiorage.new(self)
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "__class__":
                        continue
                    elif key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        method that returns a string representation 
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dic__)

    def save(self):
        """method that update the instance attribute 'updated_at'"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ 
        of the instance
        """
        insta_dic = {**self.__dict__}
        insta_dic['__class__'] = type(self).__name__
        insta_dic['created_at'] = self.created_at.isoformat()
        insta_dic['updated_at'] = self.updated_at.isoformat()

        return insta_dic
