#------ This script will follow CanSlim Daily Activity -------
#Step 1 : "Nhip Dap Thi truong"
    # xu huong giam hay tang?
    # cp dan dat nao dang tang gia?
    # xu huong hien tai va cach ung xu ?
#Step 2 : "Nhin lai cac co phieu dang so huu xem nhu the nao"

import webbrowser
from selenium import webdriver

listWebNDTT = ["https://vietstock.vn/nhan-dinh-phan-tich.htm",
                "https://vn.investing.com/news/stock-market-news",
                "https://kinhtechungkhoan.vn/chung-khoan/nhip-dap-thi-truong"]

def step1():
    print("---------------------------")
    print("STEP 1: NHIP DAP THI TRUONG")
    print("Xu huong giam hay tang - Doc Cac bao cao hang ngay de xem xu huong chung cua thi truong")
    input("Nhip Dap Thi Truong (Pres any key for Next Steps)")
    for i in listWebNDTT:
        webbrowser.open(i)
    print("---------")
    input("Note: Xu Huong thay doi ? (Pres any key for Next Steps)")
    input("Note: Co phieu Dan Dat nao tang gia ?")
    input("Note: Cach ung xu theo xu huong hien tai? ")

def step2():
    print("---------------------------")
    print("STEP 2: Kiem Tra Co Phieu Dang So Huu")
    webbrowser.open("https://tcinvest.tcbs.com.vn/tc-price?ticker=TCB&mode=placing")

def main():
    step1()
    step2()
    print("End!")


if __name__ == '__main__':
    main()
    