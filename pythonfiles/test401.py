import pyinputplus as pyip
while True:
    try:
        selection=pyip.inputYesNo("請問要計算輸入最小值,請按'y'或是離開請按'n':\n")
        if selection=='yes':
            key_in=[]
            n=pyip.inputInt("要輸入數字的次數:\n",min=0)
            for i in range (n):
                m=pyip.inputInt(f"請輸入第{i+1}數字:\n")
                key_in.append(m)
            print(f"輸入的數字中最小值是 {min(key_in)}")

        else:
            print("程序結束，謝謝使用！")
            break

    except ValueError as ve:
        print(f"輸入錯誤：{ve}")
    except KeyboardInterrupt:
        print("\n程序被用戶中斷")
        break
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")