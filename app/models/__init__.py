# app/models/__init__.py
# optional: package init for models
from User import User
from Category import Category
from Video import Video
from Clip import Clip
from learning_path import LearningPath,PathItem,UserPathProgress

__all__ = [
    "User",
    "Category",
    "Video",
    "Clip",
    "LearningPath",
    "PathItem",
    "UserPathProgress"
]