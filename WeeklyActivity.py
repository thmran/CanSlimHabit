# ------ This script will follow CanSlim Daily Activity -------
# Step 1 : "Nhip Dap Thi truong cua Tuan"
#     xu huong giam hay tang?
#     cp dan dat nao dang tang gia?
#     xu huong hien tai va cach ung xu ?
# Step 2 : "Tim do CP tren trang xep hang cac nganh"

import webbrowser
from selenium import webdriver

chromePath = "/Users/Thmtran/Google Drive/Bussiness/Company_stock_note/CANSLIM/chromedriver"


listWebNDTT = ["https://vietstock.vn/nhan-dinh-phan-tich.htm",
                "https://vn.investing.com/news/stock-market-news",
                "https://kinhtechungkhoan.vn/chung-khoan/nhip-dap-thi-truong",
                "https://vn.investing.com/indices/vn-chart"]

doThiRS = "https://www.tradingview.com/chart/pOLtTk0b/"

exploringNewStock = {"tcbGoiY": "https://tcinvest.tcbs.com.vn/tc-price?ticker=VRE&price=0&mode=placing",
                     "fireAntTimKiemCoHoi": "https://fireant.vn/top-symbols",
                     "sucManhChiSoCoBan": "https://www.cophieu68.vn/investment_basic_indexes.php"}


def tcbOverallO():
    driver = webdriver.Chrome(chromePath)
    driver.get("https://tcinvest.tcbs.com.vn/tc-price/tc-analysis?ticker=BAX")
    ads = driver.find_element_by_xpath("/html/body/app-root/div/app-tc-price/div/div[2]/app-tc-analysis/div/div/div[1]/div[1]/div/app-analysis-stock-info/div/div[2]/div[1]/div[2]/div[1]/div[2]/img")
    ads.click()


def step1():
    print("---------------------------")
    print("STEP 1: NHIP DAP THI TRUONG")
    print("Xu huong giam hay tang - Doc Cac bao cao hang ngay de xem xu huong chung cua thi truong")
    input("Nhip Dap Thi Truong (Pres any key for Next Steps)")
    for i in listWebNDTT:
        webbrowser.open(i)
    print("---------")
    input("Note: Xu Huong thay doi ? (Pres any key for Next Steps)")
    print("tcb tong quan thi truong theo tcb : dung bieu do de xem RS & overall ")
    tcbOverallO()
    input("Note: Co phieu Dan Dat nao tang gia ?")
    input("Note: Cach ung xu theo xu huong hien tai? ")


def step2():
    print("---------------------------")
    print("STEP 2: Tim Do Co Phieu o cac trang")
    webbrowser.open("https://tcinvest.tcbs.com.vn/tc-price?ticker=TCB&mode=placing")
    RS = input("Suc Manh Gia RS ?")
    if RS == "ok":
        tcbOverallO()


def main():
    step1()
    step2()
    input("Bo Sung Co Phieu Manh Nhat vao Danh Sach !!!!!")
    print("End!")


if __name__ == '__main__':
    main()
