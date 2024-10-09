def count_paper(x,y,size):
    global blue_paper, white_paper
    blue_cnt = 0
    white_cnt = 0
    for row in range(x,x+size):
        for col in range(y,y+size):
            if paper[row][col] == 1:
                blue_cnt +=1
            else:
                white_cnt +=1

    total_cnt = size*size

    if blue_cnt == total_cnt:
        blue_paper +=1
    elif white_cnt == total_cnt:
        white_paper +=1

    else:
        count_paper(x,y,size//2)
        count_paper(x,y+size//2,size//2)
        count_paper(x+size//2,y,size//2)
        count_paper(x+size//2,y+size//2,size//2)






N = int(input())

paper = [list(map(int,input().split())) for _ in range(N)]

blue_paper = 0
white_paper = 0

count_paper(0,0,N)

print(white_paper)
print(blue_paper)