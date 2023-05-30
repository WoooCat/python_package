from sqlalchemy.exc import SQLAlchemyError


class BaseRepository:
    def __init__(self, session):
        self.session = session

    def commit_changes(self):
        try:
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def close_session(self):
        self.session.close()
