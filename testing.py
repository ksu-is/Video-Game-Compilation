x = input("What game would you like to play? ")
print("You have chosen: " + x)

if x == "snake":
    import snake.py

if x == "minesweeper":
    from nachomines.scripts.main import run
    if __name__ == "__main__":
        run()