//1. He noticed that the playerResults were not being read from and so were not needed as fields.
//2. Prioritized reducing the number of lines in the getScore function
//3. Removing ambiguity of the state of score from places where previous state is not used. - Remove score from


var TennisGame2 = function () {
    this.P1point = 0;
    this.P2point = 0;
};

var pointLookup = ["Love", "Fifteen", "Thirty", "Forty"];

function getWordForPoint(point) {
    return pointLookup[point];
}

function getScoreWithTwoPointWords() {
    return getWordForPoint(this.P1point) + "-" + getWordForPoint(this.P2point);
}

TennisGame2.prototype.getScore = function () {

    if (this.P1point === this.P2point && this.P1point < 3) {
        return getWordForPoint(this.P1point) + "-All";
    }

    if (this.P1point === this.P2point && this.P1point > 2)
        return "Deuce";

     if (this.P1point >= 4 && this.P2point >= 0 && (this.P1point - this.P2point) >= 2) {
        return "Win for player1";
    }
    if (this.P2point >= 4 && this.P1point >= 0 && (this.P2point - this.P1point) >= 2) {
        return "Win for player2";
    }

    if (this.P1point > this.P2point && this.P2point >= 3) {
        return "Advantage player1";
    }

    if (this.P2point > this.P1point && this.P1point >= 3) {
        return "Advantage player2";
    }

    return getScoreWithTwoPointWords.call(this);

};

TennisGame2.prototype.SetP1Score = function (number) {
    var i;
    for (i = 0; i < number; i++) {
        this.P1Score();
    }
};

TennisGame2.prototype.SetP2Score = function (number) {
    var i;
    for (i = 0; i < number; i++) {
        this.P2Score();
    }
};

TennisGame2.prototype.P1Score = function () {
    this.P1point++;
};

TennisGame2.prototype.P2Score = function () {
    this.P2point++;
};

TennisGame2.prototype.wonPoint = function (player) {
    if (player === "player1")
        this.P1Score();
    else
        this.P2Score();
};

if (typeof window === "undefined") {
    module.exports = TennisGame2;
}