from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError


@contextmanager
def session_scope(session):
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()


class BaseRepository:
    def __init__(self, session):
        self.session = session

    def commit_changes(self):
        self.session.commit()

    def close_session(self):
        self.session.close()
