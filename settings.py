class Settings:
    def __init__(self):
        #画面の設定
        self.display={
                "width":600,
                "height":800
        }
        #ステージの設定
        self.stage={
                "bg_color":(0,0,0),
                "lag":500
        }
        #ゲームオーバー画面の設定
        self.gameover={
                "fontsize1":100,
                "bg_color":(0,0,50),
                "fg_color1":(50,50,0)
        }
        #スコアボードの設定
        self.scoreboard={
                "width":200,
                "bg_color":(120,120,120),
                "fg_color":(0,0,0),
                "fontsize":30
        }
        #プレイヤーの設定
        self.player={
                "coll_size":5,
                "size":20,
                "x":300,
                "y":700,
                "color":(255,0,0),
                "coll_color":(255,255,255),
                "speed":5,
                "slow":2,
                "power":1,
                "max_power":5,
                "item_coll":100,
                "life":5
        }
        #プレイヤーの弾の設定
        self.player_bullet1={
                "size":5,
                "color":(100,100,100),
                "speed":7,
                "timing":3
        }
        self.player_bullet2={
                "size":3,
                "color":(200,200,200),
                "speed":8,
                "timing":3
        }
        #敵の設定
        self.enemy1={
                "size":10,
                "color":(120,0,120),
                "speed":3,
                "timing":7,
                "height":300,
                "points":50,
                "height1":200,
                "height2":600,
                "max_enemys":300
        }
        self.item1={
                "size1":10,
                "size2":5,
                "color1":(0,0,255),
                "color2":(255,255,255),
                "speed1":0.2,
                "speed2":1,
                "speed3":5,
                "power":10,
                "prob":20
        }
