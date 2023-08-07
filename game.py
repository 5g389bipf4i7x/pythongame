#資訊期末統整
#簡易遊戲製作
import sys
import random

print(" ====================\n"
      "|    簡易骰子遊戲    |\n"
      " ====================")
print("--------------------------------------\n")
while True:
    print("請問您想玩幾局呢?\n(上限20局喲)")
    gamerounds = int(input("請輸入局數: "))

    while True:
        try:
            value = (gamerounds)
            break
        except ValueError:
            print("您输入不是整数")
            gamerounds = input("請輸入局數: ")

    while value == 0:
        exit = input("您真的不打算玩嗎?\n如果是的話請輸入 yes 或是 是 : ")
        if exit == "yes" or exit == "是":
            print("遊戲結束")
            sys.exit()
        else:
            print("很高興你回心轉意\n")
            gamerounds = input("請告訴我您想要玩幾局吧: ")
            while True:
                try:
                    value = int(gamerounds)
                    break
                except ValueError:
                    print("您输入不是整数")
                    gamerounds = input("請輸入局數: ")

    while value > 20 or value <= 0:
        if value > 20:
            print("您所輸入的局數超過上限\n請再次輸入局數")
            gamerounds = input("請輸入局數: ")
            while True:
                try:
                    value = int(gamerounds)
                    break
                except ValueError:
                    print("您输入不是整数")
                    gamerounds = input("請輸入局數: ")
        if value <= 0:
            print("太少了吧! 怎麼能小於1局\n再告訴我一次你想玩幾局吧")
            gamerounds = input("請輸入局數: ")
            while True:
                try:
                    value = int(gamerounds)
                    break
                except ValueError:
                    print("您输入不是整数")
                    gamerounds = input("請輸入局數: ")

    win = 0
    lose = 0
    num = 1
    for rounds in range(gamerounds):
        dice = random.randint(1,6)
        ans = input("\n第%d局\n押大或押小 請選擇: "%(num))
        while True:
            if ans == "大"or ans =="小":
                break
            else:
                print("輸入錯誤\n請再輸入一次\n")
                ans = input("押大或押小 請選擇: ")
        if (dice <= 3 and ans == "小") or  (dice >= 4 and ans == "大"):
            print("莊:%s 客:%s"%(dice,ans))
            print("恭喜你獲得一勝\n")
            win = win+1
            num = num +1 
        elif gamerounds == 1:
            print("莊:%s 客:%s"%(dice,ans))
            print("不好意思 你輸掉了這一局\n")
            lose = lose+1
            num = num +1 
        else:
            print("莊:%s 客:%s"%(dice,ans))
            print("不好意思 你輸掉了這一局\n""別灰心 再來一局!\n")
            lose = lose+1
            num = num +1 


    print("--------------------------------------\n遊戲結束\n")
    percentage =int((win/gamerounds)*100)
    print("你總共勝%s局 敗%s局\n勝率為%s%%\n"%(win,lose,percentage))
    playagain = input("請問你還想再玩一遍嗎?(要/不要): ")
    while True:
        if playagain =="要"or playagain =="不要":
            break
        else:
            print("輸入錯誤")
            playagain = input("請問你還想再玩一遍嗎?(要/不要): ")
    if playagain == "不要":
        break
print("遊戲結束")

#作業完成
