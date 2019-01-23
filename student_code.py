import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        # print("Asserting {!r}".format(fact))

        # 1) check if the arg is already a fact in the kb --> we don't store facts that are already in the kb 
        # 2) facts should be stored in a list --> use append
        if fact not in self.facts:
            self.facts.append(fact)
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        # print("Asking {!r}".format(fact))

        # find any fact that matches the queried fact
        # use match from util.py to find matches if fact input is a variable
        # if facts match, matches returns a bindings list
        # ask needs to return either a list of bindings or false
        # ask will return false if no match was made 
        bindings_list = ListOfBindings()
        match_made = False
        for f in self.facts:
            bindings = match(fact.statement, f.statement)
            if bindings != False:
                bindings_list.add_bindings(bindings)
                match_made = True
        if match_made == False: 
            return False
        return bindings_list
        
