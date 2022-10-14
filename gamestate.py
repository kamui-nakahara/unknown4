class Gamestate:
    def __init__(self):
        self.pause=False
        self.count=0
        self.score=0
        self.highscore=0
        self.damage=False
        self.gameflag="playing"
        #playing:進行中 gameover:ゲームオーバー nextstage:次のステージ empty:敵が倒されて次に進むまで
