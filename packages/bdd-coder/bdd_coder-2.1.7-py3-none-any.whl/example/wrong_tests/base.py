from bdd_coder import decorators
from bdd_coder import tester

from . import aliases

gherkin = decorators.Gherkin(aliases.MAP, logs_path='example/tests/bdd_runs.log')


@gherkin
class BddTester(tester.BddTester):
    def board__is_added_to_the_game(self, *args):
        pass
