from abc import ABC, abstractmethod
from klarify.Sorter import Sorter


class Resource(ABC):
    @abstractmethod
    def __init__(self, body, sorter: Sorter):
        pass

    @abstractmethod
    def getFileName(self) -> str:
        """Return the expected name of the resource file."""
        pass

    @abstractmethod
    def getBody(self) -> str:
        """Return the body of the resource file."""
        pass

    def getPath(self) -> str:
        """Return the expected output path for the resource file"""
        pass


class BasicResource(Resource):
    def __init__(self, body: str, sorter: Sorter):
        self.body = body
        if 'metadata' in body and 'name' in body['metadata']:
            self.resourceName = body['metadata']['name']
        else:
            self.resourceName = "Unknown"
        if 'kind' in body:
            self.resourceKind = body['kind']
        else:
            self.resourceKind = "Unknown"
        self.fileName = f"{self.resourceName}-{self.resourceKind}.yaml"
        self.path = sorter.getPath(self.fileName, self.resourceKind)

    def getFileName(self) -> str:
        """Return the expected name of the resource file."""
        return self.fileName

    def getBody(self) -> str:
        """Return the body of the resource file."""
        return self.body

    def getPath(self) -> str:
        """Return the expected output path for the resource file"""
        return self.path
