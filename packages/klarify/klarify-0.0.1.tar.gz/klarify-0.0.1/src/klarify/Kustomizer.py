import yaml
import os
from abc import ABC, abstractmethod
from pathlib import Path

from klarify.Parser import YamlParser


class Kustomizer(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def addDir(self, dir: str):
        pass

    @abstractmethod
    def generateKustomizations(self):
        pass


class StandardKustomizer(Kustomizer):
    def __init__(self, active: bool):
        self.paths = []
        self.active = active
        self.parser = YamlParser()

    def addDir(self, dir: str):
        path = Path(dir)
        ppath = Path('')
        while not path == ppath:
            if path not in self.paths and path != Path(''):
                self.paths.append(path)
            ppath = path
            path = path.parent

    def generateKustomizations(self):
        if self.active:
            for path in self.paths:
                kustom = {}
                kustom['apiVersion'] = 'kustomize.config.k8s.io/v1beta1'
                kustom['kind'] = 'Kustomization'
                kustom['resources'] = os.listdir(path)
                if 'kustomization.yaml' in kustom['resources']:
                    kustom['resources'].remove('kustomization.yaml')
                self.parser.place(kustom, path, 'kustomization.yaml')
