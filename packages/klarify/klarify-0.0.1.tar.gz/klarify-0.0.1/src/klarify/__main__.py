import argparse
from genericpath import exists
import os
import os.path

from klarify.Parser import YamlParser
from klarify.Resource import BasicResource
from klarify.Sorter import StandardSorter
from klarify.Kustomizer import StandardKustomizer


def parseArgs():
    parser = argparse.ArgumentParser(
        prog='klarify',
        description='Parse and split yaml files.',
        epilog='See https://github.com/thetalorian/klarify for additional configuration options.'
    )

    parser.add_argument(
        'inputs',
        metavar='input.yaml',
        nargs='+',
        help='One or more yaml files to parse.'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        dest='verbose',
        action='store_true',
        default=False,
        help='Verbose output')

    parser.add_argument(
        '--no-kustomize',
        dest='kustomize',
        default=True,
        action='store_false',
        help='Disable generation of kustomize files.'
    )

    return parser.parse_args()


def readConfig() -> str:
    # Ensure config file
    if not (os.path.exists('.klarify')):
        with open(os.path.join(os.path.dirname(__file__), '.klarify-default'), 'r') as inputfile:
            content = inputfile.read()
        with open('.klarify', 'w') as outputfile:
            outputfile.write(content)
        inputfile.close()
        outputfile.close()
    parser = YamlParser()
    return parser.parse('.klarify')[0]


def main():
    args = parseArgs()
    cfgdata = readConfig()
    sorter = StandardSorter(cfgdata)
    kustomizer = StandardKustomizer(args.kustomize)
    parser = YamlParser()

    for input in args.inputs:
        data = parser.parse(input)
        for resourceData in data:
            r = BasicResource(resourceData, sorter)
            kustomizer.addDir(r.path)
            parser.place(r.body, r.path, r.fileName)
            #print(yaml.dump(config, explicit_start=True, default_flow_style=False))
    kustomizer.generateKustomizations()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
