import pyinputplus as pyip
while True:
    try:
        selection:str=pyip.inputStr("請問要計算輸入最小值,繼續請按'y'或是離開請按'q':")
        if selection=='y':
            lst:list=[]
            n=pyip.inputInt("要輸入數字的次數:",min=1)
            for i in range (n):
                m=pyip.inputInt(f"請輸入第{i+1}個數字:")
                if m==9999:
                    break
                else:
                    lst.append(m)
                        
            print(f"輸入的數字中最小值是 {min(lst)}")
        elif selection=='q':
            print("程序結束，謝謝使用！")
            break

        else:
            print("無效的選擇，請重新輸入:")

            
    except ValueError as ve:
        print(f"輸入錯誤:{ve}")
    except Exception as error:
        print(f"發生未預期的錯誤：{error}")