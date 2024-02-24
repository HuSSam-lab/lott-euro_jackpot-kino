import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def get_data(year_index, month_index, num_table_index, submit_but_name):
    url = 'https://www.lotteryextreme.com/EuroJackpot/results'

    def get_page(year_index, month_index, num_table_index, submit_but_name):
        driver = webdriver.Chrome()  # type of the browser what you will use
        driver.get(url)

        select = Select(driver.find_element(By.ID, "year"))
        select.select_by_index(year_index)
        select = Select(driver.find_element(By.ID, "month"))
        select.select_by_index(month_index)
        select = Select(driver.find_element(By.ID, "last"))
        select.select_by_index(num_table_index)

        element = driver.find_element(By.ID, submit_but_name)
        element.click()
        return driver

    # turning the driver after editting to html page
    # the year index equal 2023-->0  / 2022-->1 /2021-->2   and to active it you should press sb button
    # year_index = year_index
    # month_index = 0  # the month index 0-->januaray 1-->february .....      and to active it you should press sb button
    # num_table_index = 0  # 0 --> 10 values / 1 --> 20 /2 --> 50 / 3 -->100 and to active it you should press sb2 button and this state ignore the last state
    # submit_but_name = "sb"
    soup = BeautifulSoup(get_page(year_index, month_index,
                                  num_table_index, submit_but_name).page_source, "lxml")
    date_temp = []

    date_temp = soup.find_all("tr", {'style': 'background:#F4E591'})
    numbers_temp = soup.find_all('tr', {"style": 'background:#FFFADD'})

    ################################################
    temp = []
    final_result = []
    the_king_result = []

    for j in range(len(numbers_temp)):
        temp = []
        tt = []
        for i in range(5):

            temp.append(numbers_temp[j].find('tr').find_all('td')[i].text)
        tt.append(numbers_temp[j].find('tr').find_all('td')[6].text)
        tt.append(numbers_temp[j].find('tr').find_all('td')[7].text)
        final_result.append(temp)
        the_king_result.append(tt)
    ### fail traing #######################################################
    # ll = np.array_split(np.flatten(
    #     [final_result, the_king_result]), indices_or_sections=7, axis=1)
    # df = pd.DataFrame(list(ll))

    # df = pd.DataFrame([final_result, the_king_result])
    ########################################################################

    if final_result == []:
        return pd.DataFrame([final_result, the_king_result])

    else:
        df = pd.DataFrame(np.concatenate(
            (final_result, the_king_result), axis=1))
        return df

    print(final_result)
    print(the_king_result)


total_df = pd.DataFrame()
e = 12
for i in range(11, -1, -1):
    if i == 0:
        e = 4
    for j in range(e):
        total_df = total_df._append(get_data(i, j, 0, "sb"))
total_df.to_csv('C:/Users/hussam/Desktop/123.csv', index=None,
                header=['1', '2', '3', '4', '5', 'K1', 'K2'])
