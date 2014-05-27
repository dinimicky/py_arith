'''
Created on 2014-5-28

@author: ezonghu
'''
'''
Created on 2014-5-28

@author: ezonghu
'''
import math
class Lottery(object):
    def __parse_rules(self, rule):
        [Name,Others] = rule.split(":")
        res = Others.strip().split(" ")
        [Choices, Blanks, Sorted, Unique] =  res
        return Name, int(Choices), int(Blanks), Sorted, Unique
    def perm(self, Choices, Blanks):
        return math.factorial(Choices) / math.factorial(Choices - Blanks)
    def comb(self, Choices, Blanks):
        return self.perm(Choices, Blanks) / math.factorial(Blanks)
    def __get_odds(self, Choices, Blanks, Sorted, Unique):
        if Sorted == "F" and Unique == "F":
            return Choices ** Blanks

        if Sorted == "F" and Unique == "T":
            return self.perm(Choices, Blanks)
        if Sorted == "T" and Unique == "F":
            return sum(self.comb(Choices, i) * self.comb(Blanks - 1, i - 1) for i in range(1, Blanks + 1))
        if Sorted == "T" and Unique == "T":
            return self.comb(Choices, Blanks)
        
    def sortByOdds(self, rules):
        Name_Odds = []
        for rule in rules:
            Name, Choices, Blanks, Sorted, Unique = self.__parse_rules(rule)
            Odds = self.__get_odds(Choices, Blanks, Sorted, Unique)
            Name_Odds.append((Name, Odds))
        from operator import itemgetter
        sorted_Name_Odds = sorted(Name_Odds, key = itemgetter(1,0), reverse=False)
        print(sorted_Name_Odds)
        return tuple(Name for Name, _Odds in sorted_Name_Odds) 
    

print( Lottery().sortByOdds(["AA: 10 2 T F"]))

print( Lottery().sortByOdds(("INDIGO: 93 8 T F",
"ORANGE: 29 8 T F",
"VIOLET: 76 6 T F",
"BLUE: 100 8 T F",
"RED: 99 8 T F",
"GREEN: 78 6 T F",
"YELLOW: 75 6 T F")))

from functools import lru_cache
@lru_cache(maxsize=None)
def comb_with_replacement(n, r):
    if r == 1:
        return n
    
    return sum(comb_with_replacement(x, r - 1) for x in range(1, n + 1))

@lru_cache(maxsize=None)
def comb(n, r):
    if r == 1:
        return n
    
    return sum(comb(x, r - 1) for x in range(1, n))

print(comb_with_replacement(100, 8)) 
print(comb(100, 8))    
    