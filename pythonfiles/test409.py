import pyinputplus as pyip
while True:
    try:
        selection:str=input("得票數計算程式, 繼續計算請按'y'; 離開程式請按'q' ")
        if selection=='y':
            tickets:int=pyip.inputInt("有多少張選票要計算?")
            nami=0
            chopper=0
            for i in range (tickets):
                num:str=pyip.inputChoice(choices=['1','2'], prompt="('1':No.1,Nami 或 '2':No.2,Chopper) 請選擇: ")
                if num=='1':
                    nami+=1
                else:
                    chopper+=1
            print(f"投票結果:\n No.1 Nami:{nami}, No.2, Chopper:{chopper}") 

            if nami>chopper:
                print("No.1 Nami 高票當選")
            elif nami<chopper:
                print("No.2 Chopper 高票當選")
            else:
                print("沒有人贏得此次選舉")
                    
            
        elif selection=='q':
            print("程式結束,謝謝使用! ")
            break
        else:
            print("輸入有誤! 請從新輸入")
        
    except Exception as error:
        print(f"發生無法預期的錯誤: {error}")