from terminaltables import AsciiTable
from getpass import getpass
import random

HERD = ['回合', '猜謎數字', '結果']
CONTENT = []

def main():
    print('-----幾A幾B-----')
    while True:
        game_start()
        is_repeat_game = get_is_repeat_game()
        if not is_repeat_game:
            print('遊戲結束!!!')
            exit()


# 取得是否重新再玩一次
def get_is_repeat_game():
    while True:
        ans = input('請問要重新再來一局嗎？[y/n]：')
        if ans.lower() == 'y':
            return True
        elif ans.lower() == 'n':
            return False

# 遊戲開始
def game_start():
    ans = get_ans()
    print('設定完成 遊戲開始!!!!!')
    # print('-----猜謎數字-----')
    round = 1
    while True:
        guess = get_user_ans()
        a, b = get_result(ans, guess)
        CONTENT.append([round, ''.join(guess), '{a}A{b}B'.format(a=a, b=b)])
        if a == 4:
            break
        else:
            print('第{round}局結果為: {a}A{b}B'.format(
                round = round,
                a = a,
                b = b,
            ))
        
        round += 1

    print('恭喜猜中數字 答案為：{ans} 總共耗費{round}回合'.format(
        ans=''.join(ans),
        round=round
    ))
    table = AsciiTable([HERD, *CONTENT])
    print(table.table)

# 取得答案
def get_ans():
    while True:
        ans_choose = input('請先選擇手動設定答案還是由電腦自行產生[y/n]：')
        if ans_choose.lower() == 'y':
            print('由玩家自行設定...')
            return get_user_ans(hide=True)
        elif ans_choose.lower() == 'n':
            print('由電腦設定...')
            return get_system_ans()


# 取得使用者自行設定之答案
def get_user_ans(hide=False):
    while True:
        prompt = '請輸入四位不重複之數字(ex. 1234)：'
        if hide:
            ans = getpass(prompt)
        else:
            ans = input(prompt)

        if len(ans) != 4:
            print('格式錯誤 不為四位數字')
            continue

        if not ans.isdigit():
            print('格式錯誤 答案含有非數字')
            continue

        is_repeat = False
        for n in ans: 
            # 重複數字
            if ans.count(n) > 1:
                print('格式錯誤 數字重複')
                is_repeat = True
                break

        if is_repeat:
            continue
        
        return ans


# 取得電腦設定之答案
def get_system_ans():
    ans = random.sample(range(10), 4)
    for i in range(len(ans)):
        ans[i] = str(ans[i])
    return ans


# 比對猜謎數字與答案
def get_result(ans, guess):
    a = 0
    b = 0
    for i in range(len(ans)):
        # 找到一樣的數字
        if guess[i] in ans:
            # 相同位置
            if ans[i] == guess[i]:
                a += 1
            # 不同位置
            else:
                b += 1
    
    return a, b
                

if __name__ == '__main__':
    main()