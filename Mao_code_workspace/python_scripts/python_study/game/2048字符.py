# -*- coding:UTF-8 -*-

import random
import os
import sys

v = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def display(v, score):
    print("%4d%4d%4d%4d" % (v[0][0], v[0][1], v[0][2], v[0][3])) 
    print("%4d%4d%4d%4d" % (v[1][0], v[1][1], v[1][2], v[1][3]))
    print("%4d%4d%4d%4d" % (v[2][0], v[2][1], v[2][2], v[2][3]))
    print("%4d%4d%4d%4d" % (v[3][0], v[3][1], v[3][2], v[3][3]))
    print("Total score: %d" % score)


def init(v):
    for i in range(4):
        v[i] = [random.choice([0, 0, 0, 2, 2, 4]) for x in range(4)]


def align(vList, direction):
    for i in range(vList.count(0)):
        vList.remove(0)
    zeros = [0 for x in range(4 - len(vList))]
    if direction == 'left':
        vList.extend(zeros)
    else:
        vList[:0] = zeros


def addSame(vList, direction):
    score = 0
    if direction == 'left':
        for i in [0, 1, 2]:
            align(vList, direction)
            if vList[i] == vList[i + 1] != 0:
                vList[i] *= 2
                vList[i + 1] = 0
                score += vList[i]
                return {'bool': True, 'score': score}
    else:
        for i in [3, 2, 1]:
            align(vList, direction)
            if vList[i] == vList[i - 1] != 0:
                vList[i] *= 2
                vList[i - 1] = 0
                score += vList[i]
                return {'bool': True, 'score': score}
    return {'bool': False, 'score': score}


def handle(vList, direction):
    totalScore = 0
    align(vList, direction)
    result = addSame(vList, direction)
    while result['bool'] == True:
        totalScore += result['score']
        align(vList, direction)
        result = addSame(vList, direction)
    return totalScore


def operation(v):
    totalScore = 0
    gameOver = False
    direction = 'left'
    op = input('operator:')
    if op in ['a', 'A']:
        direction = 'left'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['d', 'D']:
        direction = 'right'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['w', 'W']:
        direction = 'left'
        for col in range(4):
            vList = [v[row][col] for row in range(4)]
            totalScore += handle(vList, direction)
            for row in range(4):
                v[row][col] = vList[row]
    elif op in ['s', 'S']:
        direction = 'right'
        for col in range(4):
            vList = [v[row][col] for row in range(4)]
            totalScore += handle(vList, direction)
            for row in range(4):
                v[row][col] = vList[row]
    else:
        print("Invalid input,please enter a charactor in [W,S,A,D] or the lower")
        gameOver = True
        return {'gameOver': gameOver, 'score': totalScore}

    N = 0
    for q in v:
        N += q.count(0)

    if N == 0:
        gameOver = True
        return {'gameover': gameOver, 'score': totalScore}

    num = random.choice([2, 2, 2, 4])
    k = random.randrange(1, N + 1)
    n = 0

    for i in range(4):
        for j in range(4):
            if v[i][j] == 0:
                n += 1
                if n == k:
                    v[i][j] = num
                    break

    return {'gameOver': gameOver, 'score': totalScore}


init(v)
score = 0
print("Input: W(Up) S(Down) A(Left) D(Right), press <CR>.")
while True:
    os.system("cls")
    display(v, score)
    result = operation(v)
    print(result["score"])
    if result['gameOver'] == True:
        print("Game Over, You failed!")
        print("Your total score %d" % (score))
        sys.exit(1)
    else:
        score += result['score']
        if score >= 2048:
            print("Game Over, You Win!!!")
            print("Your total score: %d" % (score))
            sys.exit(0)