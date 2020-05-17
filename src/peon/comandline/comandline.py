import argparse

from peon.comandline.project_tree import ProjectTree
from peon.lint.lint import Lint


class CommandLine:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process some integers.')

    def argument_initialization(self):
        self.parser.add_argument(
            'path_to_project',
            metavar='PATH',
            type=str,
            nargs='?',
            help='path to your project'
        )

    def parse_input(self):
        args = self.parser.parse_args()

        if args.path_to_project:
            project_tree = ProjectTree(args.path_to_project)
            files = project_tree.inspect()
            Lint(files).project()

