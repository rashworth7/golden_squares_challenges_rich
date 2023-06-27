board = [
            "..........",
            ".SSSSS....",
            ".SSSS.....",
            ".SSSS.....",
            "..SSS.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
            ]

board = [row.replace('X', '💥') for row in board]

# Replace 'S' with motorboat emoji
board = [row.replace('S', '⚫') for row in board]

board = [row.replace('.', '🔵') for row in board]

board = [row.replace('0', '⚪') for row in board]

result = []
for row in board:
    result.append(row)

print(result)