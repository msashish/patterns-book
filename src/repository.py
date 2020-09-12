import abc

from src import model


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, reference: str) -> model.Batch:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def add(self, batch):
        self.session.add(batch)

    def list(self):
        return self.session.query(model.Batch).all()
