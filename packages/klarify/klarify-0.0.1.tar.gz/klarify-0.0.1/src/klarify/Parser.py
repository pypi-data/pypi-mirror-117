import yaml
import os
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def parse(self, input: str) -> str:
        pass

    @abstractmethod
    def place(self, data: str, path: str):
        pass


class YamlParser(Parser):
    def __init__(self):
        pass

    def str_presenter(self, dumper, data):
        """Lifted from ysaakpr at https://github.com/yaml/pyyaml/issues/237"""
        try:
            dlen = len(data.splitlines())
            if (dlen > 1):
                return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        except TypeError as ex:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data)
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    def parse(self, input: str) -> str:
        #print(f"input file {input}")
        with open(input, 'r') as stream:
            resources = list(yaml.safe_load_all(stream))
        stream.close()
        return resources

    def place(self, data: str, path: str, output: str):
        yaml.add_representer(str, self.str_presenter)
        if not(os.path.exists(path)):
            os.makedirs(path)
        #print(f"Writing to {output}")
        with open(os.path.join(path, output), 'w') as stream:
            # subdata = {}
            # if 'data' in data:
            #     subdata['data'] = data['data']
            #     del data['data']

            stream.write(yaml.dump(data,
                                   sort_keys=False,
                                   explicit_start=True,
                                   default_flow_style=False,
                                   ))
            # if not subdata is None:
            #     stream.write(yaml.dump(subdata,
            #                            sort_keys=False,
            #                            explicit_start=False,
            #                            default_flow_style=False,
            #                            default_style=None
            #                            ))
            stream.close()
