from abc import ABC, abstractmethod
import re


class Sorter(ABC):
    @abstractmethod
    def __init__(self, config):
        """Initial setup for the sorter."""
        pass

    @abstractmethod
    def getPath(self, resource: str, kind: str) -> str:
        """Return calculated path."""
        pass


class StandardSorter(Sorter):
    def __init__(self, config):
        if not "structure" in config:
            raise ValueError('"structure" section required in config file.')
        self.structure = config['structure']
        if not "categories" in config:
            raise ValueError('"categories" section required in config file.')
        self.categories = config['categories']

    def getPath(self, resource: str, kind: str) -> str:
        """Return the calculated path."""
        # Set defaults for mismatches
        path = "generated"
        sub = "unknown"
        for destination in self.structure:
            if self.matches(resource, self.structure[destination]):
                path = destination
                break
        for category in self.categories:
            if self.matches(kind, self.categories[category]):
                sub = category
                break
        return f"{path}/{sub}"

    def matches(self, resource: str, patterns: list) -> bool:
        for pattern in patterns:
            if re.search(pattern, resource):
                return True
        return False
