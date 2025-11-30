from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.learning_path_path_item import LearningPathPathItem
from app.models.learning_path import LearningPath
from app.models.user_learning_path import UserLearningPath
class LearningPathCURD:
    @staticmethod
    def create_learning_path(db: Session, user_id: int, title: str, description: str= None) -> LearningPath:
        learning_path = LearningPath(title=title, description=description)
        db.add(learning_path)
        db.commit()
        db.refresh(learning_path)

        # 创建关联记录
    
        user_learning_path = UserLearningPath(user_id=user_id, learning_path_id=learning_path.id)
      
        try:
            db.add(user_learning_path)
            db.commit()
        except:
            db.rollback()
            raise Exception("This learning path is already associated with the user.")

        return user_learning_path
    
    @staticmethod
    def get_learning_paths_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[LearningPath]:
        learning_paths = db.query(LearningPath).join(UserLearningPath,UserLearningPath.learning_path_id==LearningPath.id)\
                    .filter(UserLearningPath.user_id == user_id)\
                    .offset(skip)\
                    .limit(limit)\
                    .all()
        return learning_paths
    

    @staticmethod
    def get_learning_path(db: Session, learning_path_id: int) -> Optional[LearningPath]:
        return db.query(LearningPath).filter(LearningPath.id == learning_path_id).first()
    


    
    @staticmethod
    def delete_learning_path(db: Session, learning_path: LearningPath) -> None:
        db.delete(learning_path)
        db.commit() 