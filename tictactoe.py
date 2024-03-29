import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        print(self.game_engine)

        #무한반복
        while True:
            #input row, col
            row = int(input('row: '))
            col = int(input('col : '))

            #set
            self.game_engine.set(row, col)

            #show board
            print(self.game_engine)

            #check_winner 승패가 결정나면 break
            winner = self.game_engine.check_winner()

            if winner != None :
                break

        if winner == 'O' :
            print('O 이김')
        elif winner == 'X':
            print('X 이김')
        elif winner == 'd':
            print('무승부')

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_ui()

    def init_ui(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱 택 토')
        self.root.geometry(str(self.CANVAS_SIZE) + 'x' + str(self.CANVAS_SIZE)) # '300 x 300'
        self.canvas = tkinter.Canvas(self.root, bg = 'white', width= self.CANVAS_SIZE, height = self.CANVAS_SIZE)
        self.canvas.pack()

        #{'O' : PhotoImage 객체, 'X': PhotoImage 객체 } 딕셔너리
        self.images = {}
        self.images['O'] = tkinter.PhotoImage(file = '짜장면.png')
        self.images['X'] = tkinter.PhotoImage(file = '짬뽕.png')

        self.canvas.bind('<Button-1>', self.click_handler) #bind는 연결, <button-1>로 연결

    def click_handler(self, event):
        x = event.x
        y = event.y
        # if 0 <= x < 100:
        #     row = 1
        # elif 100 <= x < 200:
        #     row = 2
        # elif 200 <= x < 300:  
        #     row = 3



        #클릭처리 => 말응 놓는다
        col = x // 100 + 1
        row = y // 100 + 1

        self.game_engine.set(row, col)

        #show board
        self.draw_board()

        #승자 결졍되면 break
        winner = self.game_engine.check_winner()

        #결과보여주기
        if winner == 'O':
            messagebox.showinfo('Game Over', '짜장면 승')
            self.root.quit() #root는 창


        elif winner == 'X':
            messagebox.showinfo('Game Over', '짬뽕 승')
            self.root.quit()


        elif winner == 'd':
            messagebox.showinfo('Game Over', '무승부')
            self.root.quit()

    def draw_board(self):

        x = 0
        y = 0
        for i, v in enumerate(self.game_engine.board):
            if v == 'O':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['O'])

            elif v == 'X':
                self.canvas.create_image(x, y, anchor='nw', image = self.images['X'])

            TILE_SIZE = self.CANVAS_SIZE//3
            x += TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += TILE_SIZE


    def play(self):
        self.root.mainloop()


if __name__ == '__main__':

    #ttt = Tictactoe()
    ttt = TictactoeGUI()
    ttt.play()