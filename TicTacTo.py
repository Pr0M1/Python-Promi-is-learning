import pprint

def printboard(board):
    print(board["Top-L"] + "|" + board["Top-M"] + "|" + board["Top-R"])
    print("-----")
    print(board["Mid-L"] + "|" + board["Mid-M"] + "|" + board["Mid-R"])
    print("-----")
    print(board["Bottom-L"] + "|" + board["Bottom-M"] + "|" + board["Bottom-R"])



theBoard = {"Top-L": " ", "Top-M": " ", "Top-R": " ", \
            "Mid-L": " ", "Mid-M": " ", "Mid-R": " ",
            "Bottom-L": " ", "Bottom-M": " ", "Bottom-R": " "}
printboard(theBoard)