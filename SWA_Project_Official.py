#!/usr/bin/env python
# coding: utf-8

# In[27]:


import time
import pandas as pd
import numpy as np
from tqdm import tqdm


# In[28]:


# MAIN CODE

## Introduction

print('''
█░█ █▄░█ █ █░█░█ █▀█ █ ▀█▀ █▀▀ █
█▄█ █░▀█ █ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ ▄
''')
time.sleep(1)
print('BS20DMU019. Property of prof. Hazem El Alfy et al. TM © 2023 - SP ain School of Data Science. All rights reversed.')
time.sleep(3)
print()
print("WELCOME TO UniWrite!™ ")
time.sleep(1)
print()
print("This app will help you choose your university right.")
print()
print()


# In[33]:


print('Before we proceed, please make sure you have either Mozilla Firefox or Google Chrome on your system!')

ans = input('Which browser would you prefer? F for Mozilla Firefox, C for Google Chrome, E for exit: ')
time.sleep(2)
print()


# In[36]:


if ans.lower()=='f':
    print("Please wait while we prepare the services.")
    print("In case of any error, traceback or setback, try rerunning the application.")
    time.sleep(2)
    # IMPORTS
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    
    # MAIN CODE

    ## Getting Rankings and Employability Rate
    print('Compiling necessary info...')
    options = FirefoxOptions()
    options.add_argument('-headless')

    driver = webdriver.Firefox(options=options,service=Service(GeckoDriverManager().install()))
    driver.get('https://www.topuniversities.com/university-rankings/employability-rankings/2022')
    #time.sleep(5)

    rankings = {}
    emp_rate = {}

    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]')))

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]/a').send_keys(Keys.RETURN)

    search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/input')

    universities = ['UNIVERSITY OF SYDNEY','UNSW','UNIVERSITY OF TECHNOLOGY SYDNEY','MACQUARIE UNIVERSITY', 'WESTERN SYDNEY UNIVERSITY']

    for i in universities:
        search_bar.send_keys(i)

        driver.implicitly_wait(2)
        rank = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div')
        rankings[i] = rank.text

        emp = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/span/div/div')
        emp_rate[i] = emp.text

        search_bar.clear()

    #print(rankings)
    #print(emp_rate)

    driver.quit()

    time.sleep(5)
    print("All necessary resources compiled")
    print()
    
    ## UAC CODE

    # print('CHOOSE YOUR UNIVERSITY RIGHT - WITH UniWrite!')

    query = input("Enter desired course name: ")
    driver = webdriver.Firefox(options=options,service=Service(GeckoDriverManager().install()))
    print('fetching the page...')
    driver.get('https://www.uac.edu.au/')
    original_window = driver.current_window_handle

    searchButton_xpath = '//*[@id="searchBlockButton"]'
    searchBar_xpath = '//*[@id="searchBlockInput"]'
    searchResults_class = 'row course-container course-status-open  participating'

    search = driver.find_element(by=By.XPATH, value=searchBar_xpath)
    search.send_keys(query)
    time.sleep(2)

    driver.find_element(by=By.XPATH, value=searchButton_xpath).send_keys(Keys.RETURN) # Instead of click we can also use `send_keys(Keys.RETURN)`

    #time.sleep(5)

    wait = WebDriverWait(driver,10)
    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
            if window_handle != driver.current_window_handle:
                driver.switch_to.window(window_handle)
                break
    #time.sleep(3)


    time.sleep(5)
    #print('fetching the title')
    #print(driver.title)

    WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='overlay'][contains(@style, 'display: none')]")))

    #time.sleep(5)
    wait.until(EC.presence_of_element_located((By.ID, 'filterSectionInst')))
    filter_inst = driver.find_element(by=By.ID, value='filterSectionInst')
    filter_inst.click()

    time.sleep(1)
    #driver.quit()

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[12]/label/input')))

    # MACQUARIE CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[12]/label/input').click()
    # USYD CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[23]/label/input').click()
    # UTS CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[24]/label/input').click()
    # UNSW CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[26]/label/input').click()
    # WSU CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[27]/label/input').click()


    time.sleep(1)

    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'showAlllink')))
    showAll = driver.find_element(By.CLASS_NAME, 'showAlllink')
    try:
        showAll.click()
    except:
        print("Less than fifteen courses / No courses")
    time.sleep(1)
    all_results_container = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]')

    course_names = driver.find_elements(By.CLASS_NAME, 'course-name')
    curr = driver.current_window_handle
    counter = 0
    '''    
    print("====================================")
    print("Now the try block: ")
    print("====================================")
    '''

    # Lists
    uni_name = []
    guar_atar = []
    pre_requisite = []
    location = []
    assumed_knowledge = []
    course_title = []
    course_ID = []
    duration = []
    start_date = []
    rankings_list = []
    emp_rate_list = []

    print()
    print("RETRIEVING INFORMATION...")
    print()

    try:

        course_names = driver.find_elements(By.CLASS_NAME, 'course-name')
        for course in tqdm(course_names):
            tag = course.find_element(By.TAG_NAME,'a')
            link = tag.get_attribute('href')
            driver.switch_to.new_window('tab')
            time.sleep(1.5)
            driver.get(link)
            time.sleep(1.5)


            # Couse title
            try:
                course_name = driver.find_element(By.CLASS_NAME, 'course-title')
                course_title.append(course_name.text)
            except:
                course_title.append('-')

            # Course code
            try:
                course_code = driver.find_element(By.CLASS_NAME, 'course-code')
                course_ID.append(course_code.text)
            except:
                course_ID.append('-')

            # Duration
            try:
                poa_value = driver.find_element(By.CLASS_NAME, 'poaValue')
                duration.append(poa_value.text)
            except:
                duration.append('-')

            # Start date
            try:
                dates_start = driver.find_elements(By.CLASS_NAME, 'date-start')
                dates_start_list = [i.text for i in dates_start]
                start_date.append(', '.join(dates_start_list))
            except:
                start_date.append('-')

            # Uni name
            try:
                inst_name = driver.find_element(By.CLASS_NAME, 'institution-name')
                if ' / ' in inst_name.text:
                    uni_name.append(inst_name.text.split(' / ')[0])
                else:
                    uni_name.append(inst_name.text)
            except:
                uni_name.append('-')

            # Location
            try:
                location_name = driver.find_element(By.CLASS_NAME, 'course-location-campus')
                location.append(location_name.text)
            except:
                location.append('-')

            # Pre-Requisite
            try:
                prereq_div = driver.find_element(By.ID, 'prereq')
                prereq_para = prereq_div.find_element(By.TAG_NAME, 'p')
                pre_requisite.append(prereq_para.text)
            except:
                pre_requisite.append('-')

            # Guaranteed ATAR
            try:
                admission = driver.find_element(By.ID, 'admission')
                paragraphs = admission.find_elements(By.TAG_NAME, 'p')
                for paragraph in paragraphs:
                    if 'Guaranteed' in paragraph.text:
                        guar_atar.append(': '.join(paragraph.text.split(': ')[1:]).replace('\n', ' '))
                        break
                else:
                    guar_atar.append('-')
            except:
                guar_atar.append('-')

            # Assumed knowledge:
            try:
                admission = driver.find_element(By.ID, 'admission')
                paragraphs = admission.find_elements(By.TAG_NAME, 'p')
                for paragraph in paragraphs:
                    if 'Assumed' in paragraph.text:
                        assumed_knowledge.append(': '.join(paragraph.text.split(': ')[1:]).replace('\n', ' '))
                        break
                else:
                    assumed_knowledge.append('-')
            except:
                assumed_knowledge.append('-')

            driver.close()
            driver.switch_to.window(curr)
            counter += 1
    except:
        print("Some exception occurred!")

    time.sleep(1.5)
    '''
    print(uni_name)
    print()
    print(location)
    print()
    print(pre_requisite)
    print()
    print(len(guar_atar))
    print()
    print(len(assumed_knowledge))
    print()
    print(course_ID)
    print()
    print(duration)
    print()
    print(start_date)
    print()
    '''
    rankings_list = [rankings[i] for i in uni_name]
    emp_rate_list = [emp_rate[i] for i in uni_name]
    '''
    print(rankings_list)
    print(len(rankings_list))
    print()
    print(emp_rate_list)
    print(len(emp_rate_list))
    print()
    '''

    print("All info retrieved successfully")
    driver.quit()
    
    ## BUILDING THE DATAFRAME

    data = {'Uni Name': uni_name, 'Course ID': course_ID, 'Duration':duration, 'Start Date': start_date, 'Course Title':course_title, 'Location': location, 'Pre-Requisites': pre_requisite, 'Guaranteed ATAR': guar_atar, 'Assumed Knowledge': assumed_knowledge, 'Ranking':rankings_list, 'Employability Rate': emp_rate_list}
    df = pd.DataFrame(data)
    df = df.replace('-',np.nan)
    df
    
    # EXPORTING DATAFRAME TO CSV

    name = query.capitalize() + ' Course Details.csv'
    df.to_csv(name)
    print("CSV containing course details by the name '" + query.capitalize() + "Course Details.csv' will be successfully exported after termination of these services.")
    print()
    time.sleep(1)
    print("Thank you for using our services! Please check your directory for the CSV containing all the info regarding your desired courses.")
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Shutting down services...')
    time.sleep(5)
elif ans.lower()=='c':
    print("Please wait while we prepare the services.")
    print("In case of any error, traceback or setback, try rerunning the application.")
    time.sleep(2)
    
    # IMPORTS
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    
    # MAIN CODE

    ## Getting Rankings and Employability Rate
    print('Compiling necessary info...')
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('-headless')

    driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    driver.get('https://www.topuniversities.com/university-rankings/employability-rankings/2022')
    #time.sleep(5)

    rankings = {}
    emp_rate = {}

    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]')))

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]/a').send_keys(Keys.RETURN)

    search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/input')

    universities = ['UNIVERSITY OF SYDNEY','UNSW','UNIVERSITY OF TECHNOLOGY SYDNEY','MACQUARIE UNIVERSITY', 'WESTERN SYDNEY UNIVERSITY']

    for i in universities:
        search_bar.send_keys(i)

        driver.implicitly_wait(2)
        rank = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div')
        rankings[i] = rank.text

        emp = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/span/div/div')
        emp_rate[i] = emp.text

        search_bar.clear()

    #print(rankings)
    #print(emp_rate)

    driver.quit()

    time.sleep(5)
    print("All necessary resources compiled")
    print()
    
    ## UAC CODE

    # print('CHOOSE YOUR UNIVERSITY RIGHT - WITH UniWrite!')

    query = input("Enter desired course name: ")
    driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    print('fetching the page...')
    driver.get('https://www.uac.edu.au/')
    original_window = driver.current_window_handle

    searchButton_xpath = '//*[@id="searchBlockButton"]'
    searchBar_xpath = '//*[@id="searchBlockInput"]'
    searchResults_class = 'row course-container course-status-open  participating'

    search = driver.find_element(by=By.XPATH, value=searchBar_xpath)
    search.send_keys(query)
    time.sleep(2)

    driver.find_element(by=By.XPATH, value=searchButton_xpath).send_keys(Keys.RETURN) # Instead of click we can also use `send_keys(Keys.RETURN)`

    #time.sleep(5)

    wait = WebDriverWait(driver,10)
    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
            if window_handle != driver.current_window_handle:
                driver.switch_to.window(window_handle)
                break
    #time.sleep(3)


    time.sleep(5)
    #print('fetching the title')
    #print(driver.title)

    WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='overlay'][contains(@style, 'display: none')]")))

    #time.sleep(5)
    wait.until(EC.presence_of_element_located((By.ID, 'filterSectionInst')))
    filter_inst = driver.find_element(by=By.ID, value='filterSectionInst')
    filter_inst.click()

    time.sleep(1)
    #driver.quit()

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[12]/label/input')))

    # MACQUARIE CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[12]/label/input').click()
    # USYD CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[23]/label/input').click()
    # UTS CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[24]/label/input').click()
    # UNSW CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[26]/label/input').click()
    # WSU CHECKBOX
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[27]/label/input').click()


    time.sleep(1)

    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'showAlllink')))
    showAll = driver.find_element(By.CLASS_NAME, 'showAlllink')
    try:
        showAll.click()
    except:
        print("Less than fifteen courses / No courses")
    time.sleep(1)
    all_results_container = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]')

    course_names = driver.find_elements(By.CLASS_NAME, 'course-name')
    curr = driver.current_window_handle
    counter = 0
    '''    
    print("====================================")
    print("Now the try block: ")
    print("====================================")
    '''

    # Lists
    uni_name = []
    guar_atar = []
    pre_requisite = []
    location = []
    assumed_knowledge = []
    course_title = []
    course_ID = []
    duration = []
    start_date = []
    rankings_list = []
    emp_rate_list = []

    print()
    print("RETRIEVING INFORMATION...")
    print()

    try:

        course_names = driver.find_elements(By.CLASS_NAME, 'course-name')
        for course in tqdm(course_names):
            tag = course.find_element(By.TAG_NAME,'a')
            link = tag.get_attribute('href')
            driver.switch_to.new_window('tab')
            time.sleep(1.5)
            driver.get(link)
            time.sleep(1.5)


            # Couse title
            try:
                course_name = driver.find_element(By.CLASS_NAME, 'course-title')
                course_title.append(course_name.text)
            except:
                course_title.append('-')

            # Course code
            try:
                course_code = driver.find_element(By.CLASS_NAME, 'course-code')
                course_ID.append(course_code.text)
            except:
                course_ID.append('-')

            # Duration
            try:
                poa_value = driver.find_element(By.CLASS_NAME, 'poaValue')
                duration.append(poa_value.text)
            except:
                duration.append('-')

            # Start date
            try:
                dates_start = driver.find_elements(By.CLASS_NAME, 'date-start')
                dates_start_list = [i.text for i in dates_start]
                start_date.append(', '.join(dates_start_list))
            except:
                start_date.append('-')

            # Uni name
            try:
                inst_name = driver.find_element(By.CLASS_NAME, 'institution-name')
                if ' / ' in inst_name.text:
                    uni_name.append(inst_name.text.split(' / ')[0])
                else:
                    uni_name.append(inst_name.text)
            except:
                uni_name.append('-')

            # Location
            try:
                location_name = driver.find_element(By.CLASS_NAME, 'course-location-campus')
                location.append(location_name.text)
            except:
                location.append('-')

            # Pre-Requisite
            try:
                prereq_div = driver.find_element(By.ID, 'prereq')
                prereq_para = prereq_div.find_element(By.TAG_NAME, 'p')
                pre_requisite.append(prereq_para.text)
            except:
                pre_requisite.append('-')

            # Guaranteed ATAR
            try:
                admission = driver.find_element(By.ID, 'admission')
                paragraphs = admission.find_elements(By.TAG_NAME, 'p')
                for paragraph in paragraphs:
                    if 'Guaranteed' in paragraph.text:
                        guar_atar.append(': '.join(paragraph.text.split(': ')[1:]).replace('\n', ' '))
                        break
                else:
                    guar_atar.append('-')
            except:
                guar_atar.append('-')

            # Assumed knowledge:
            try:
                admission = driver.find_element(By.ID, 'admission')
                paragraphs = admission.find_elements(By.TAG_NAME, 'p')
                for paragraph in paragraphs:
                    if 'Assumed' in paragraph.text:
                        assumed_knowledge.append(': '.join(paragraph.text.split(': ')[1:]).replace('\n', ' '))
                        break
                else:
                    assumed_knowledge.append('-')
            except:
                assumed_knowledge.append('-')

            driver.close()
            driver.switch_to.window(curr)
            counter += 1
    except:
        print("Some exception occurred!")

    time.sleep(1.5)
    '''
    print(uni_name)
    print()
    print(location)
    print()
    print(pre_requisite)
    print()
    print(len(guar_atar))
    print()
    print(len(assumed_knowledge))
    print()
    print(course_ID)
    print()
    print(duration)
    print()
    print(start_date)
    print()
    '''
    rankings_list = [rankings[i] for i in uni_name]
    emp_rate_list = [emp_rate[i] for i in uni_name]
    '''
    print(rankings_list)
    print(len(rankings_list))
    print()
    print(emp_rate_list)
    print(len(emp_rate_list))
    print()
    '''

    print("All info retrieved successfully")
    driver.quit()
    
    ## BUILDING THE DATAFRAME

    data = {'Uni Name': uni_name, 'Course ID': course_ID, 'Duration':duration, 'Start Date': start_date, 'Course Title':course_title, 'Location': location, 'Pre-Requisites': pre_requisite, 'Guaranteed ATAR': guar_atar, 'Assumed Knowledge': assumed_knowledge, 'Ranking':rankings_list, 'Employability Rate': emp_rate_list}
    df = pd.DataFrame(data)
    df = df.replace('-',np.nan)
    df
    
    # EXPORTING DATAFRAME TO CSV

    name = query.capitalize() + ' Course Details.csv'
    df.to_csv(name)
    print("CSV containing course details by the name '" + query.capitalize() + "Course Details.csv' will be successfully exported after termination of these services.")
    print()
    time.sleep(1)
    print("Thank you for using our services! Please check your directory for the CSV containing all the info regarding your desired courses.")
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.',end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Shutting down services...')
    time.sleep(5)

elif ans.lower() == 'e':
    print('Exiting...')
    time.sleep(3)
    
else:
    print("Error. Please restart the program and type in a valid option.")
    time.sleep(6)


# In[ ]:




