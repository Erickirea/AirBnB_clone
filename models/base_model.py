#!/usr/bin/python3
"""A model that defines the BaseModel class for use in other models."""
import uuid
from datetime import datetime
import models 

class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize new instance for BaseModel.

        Args:
            - *args (any): this will not be used
            - **kwargs (dict): dictionary with key and value args
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """Return the print/str representation of the BaseModel class."""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__))
    
    def to_dict(self):
        """Return the dictionary representation of the BaseModel class."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
