# -*- coding: utf-8 -*-

from enum import Enum

class SCORE(Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        result = ""
        tempScore=0

        if self.__has_any_player_won():
            result = self.__get_winning_player_score()

        elif self.__is_same_score():
            result = self.__get_same_score()

        elif self.__any_player_has_at_least_4_points():
            result = self.__get_player_has_at_least_4_points_score()

        else:
            result = self.__get_no_player_has_at_least_4_points_score()

        return result

    def __has_any_player_won(self):
        if self.__any_player_has_at_least_4_points():
            return abs(self.p1points - self.p2points) >= 2

    def __is_same_score(self):
        return self.p1points==self.p2points

    def __any_player_has_at_least_4_points(self):
        return self.p1points>=4 or self.p2points>=4

    def __get_winning_player_score(self):
        if self.p1points > self.p2points:
            return "Win for " + self.player1Name
        return "Win for " + self.player2Name

    def __get_same_score(self):
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(self.p1points, "Deuce")

    def __get_player_has_at_least_4_points_score(self):
        result = ''
        minusResult = self.p1points-self.p2points
        if (minusResult==1):
            result ="Advantage " + self.player1Name
        elif (minusResult ==-1):
            result ="Advantage " + self.player2Name
        elif (minusResult>=2):
            result = "Win for " + self.player1Name
        else:
            result ="Win for " + self.player2Name

        return result

    def __get_no_player_has_at_least_4_points_score(self):
        result = ''
        for i in range(1,3):
            if (i==1):
                tempScore = self.p1points
            else:
                result+="-"
                tempScore = self.p2points
            result += {
                0 : "Love",
                1 : "Fifteen",
                2 : "Thirty",
                3 : "Forty",
            }[tempScore]

        return result


# notes:
# enum for scores (code consolidation due to indexing vs if statements)
# consistent use of operators (more like flow readability)
#   for example: self.p1points < 3 => self.p1points <= 2
#                self.p1points > 2 => self.p1points >= 3
# create a scorer class (use SRP to keep things tidy)
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self):
        result = ""

        # 3 major if statements:
        # Goal: to help organize these string of if statements to find common functionality
        # if self.__is_tied():
        #     blah
        # elif self.__is_p1_winning():
        #     blah
        # elif self.__is_p2_winning():
        #     blah


        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points==0):
                result = "Love"
            if (self.p1points==1):
                result = "Fifteen"
            if (self.p1points==2):
                result = "Thirty"
            result += "-All"
        if (self.p1points==self.p2points and self.p1points>2):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points <= 3):
                P1res = next([x.name for x in SCORE.x if x.value == self.p1points])
            # if (self.p1points==1):
            #     P1res = "Fifteen"
            # if (self.p1points==2):
            #     P1res = "Thirty"
            # if (self.p1points==3):
            #     P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res="Thirty"
            if (self.p1points==3):
                P1res="Forty"
            if (self.p2points==1):
                P2res="Fifteen"
            if (self.p2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res="Thirty"
            if (self.p2points==3):
                P2res="Forty"
            if (self.p1points==1):
                P1res="Fifteen"
            if (self.p1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.p1points +=1
    
    
    def P2Score(self):
        self.p2points +=1
        
class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1
    
    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
