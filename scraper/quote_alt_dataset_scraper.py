#can make efficient by not picking if tags len aka total label = 1
#don't enter attributed-no-source, quote-investigator
#if attributed, misattributed, no-source in tag then revise
#remove christian , donkey and hitchshit, harari, sam harris, 
# gay, glbt, lesbian, lgbt, queer,

#Possibilities of this classifier:
'''from mainly quotes and poetry, song, convesation dialogue input. automate hashtag, '''
#suggest simliar famous person, books, fictional character, franchise related to input. 
# so you can explore new horizons according to your interest.
#quote with poetic tendency. so you can 

#after revise check:

# maxlen(tag) 


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common import exceptions
from tqdm import tqdm
import pandas as pd
import time
import csv
import json
import traceback


#keep for professionalism. they will say redundant
def save_scraped_row( author, quote, info_list, info_list_w_author):
    # quote_data = []
    # quote_data.append( author)
    # quote_data.append( quote)
    # quote_data.append( info_list)
    # quote_data.append( info_list_w_author)               
    with open("quote_nlp_dataset.csv", "a", newline="" , encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([author, quote, info_list, info_list_w_author])



def quote_scraper( base_url:str, start_page:int) : 

    for page_no in tqdm(range(start_page,101)): #tqdm(range())
        
        url = f"{base_url}?page={page_no}"
        # track lastest scrap. helps with pause continuing at a later time:
        with open("scrap_tracker.json", "w") as f:
            json.dump( {"latest_page": page_no, "latest_url": base_url}, f)
        
        driver.get(url)
        print(f'\nLaunched {url}')
        
        all_quotes = driver.find_elements(By.CSS_SELECTOR, 'div.quote')       
        for idx, element in enumerate(all_quotes):
            try:
                
                quote_element = element.find_element(By.CSS_SELECTOR, 'div.quoteText').text #quoteText               
                #to be upgraded soon
                author = quote_element.split('―')[1].strip()
                if ',' in author:
                    author = author.split(',')[0]  
                quote = quote_element.split('―')[0].strip('\n').strip('“').strip('”')                              
                # # print(author, quote)               
                info_list_w_author = []
                info_list = []
                tags = element.find_element(By.CSS_SELECTOR, 'div.greyText.smallText.left').find_elements(By.TAG_NAME, "a")
                for tag in tags:
                    #info_list_set.add(tag.text)
                    info_list.append(tag.text)
                    #info_list_w_author.append(tag.text)
                #info_list = [info_list]
                #print(info_list)
                #print(f'no.{idx+1} \ttags processed')
                #print(info_list_set) 

                info_list_w_author = info_list
                info_list_w_author.append(author)

                # likes = element.find_element(By.CSS_SELECTOR, 'div.quoteFooter').find_element(By.CSS_SELECTOR, 'div.right').text
                # likes = likes.split(' ')[0]
                # print(likes)
                
                with open("quote_nlp_dataset.csv", "a", newline="" , encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([author, quote, info_list, info_list_w_author]) 


                #print(f'Appended row to csv {quote_data}\n') #initial_scrap_page={initial_scrap_page}. 
                #print(info_list_set,'\n')
                
                # if(initial_scrap_page) : 
                #     time.sleep(3)               


            except IndexError as e: # when popup appears, scraping at <author> will always throw IndexError 
                print(f'While quote no.{idx+1} handling pop-up window')
                popup_exit_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/button')
                popup_exit_btn.click()
                time.sleep(1)
                print('pop-up closed.')
                continue
            
            except exceptions.NoSuchElementException as e: # handles when tags for a quote is not present
                print(f'\t No Tags at no.{idx+1} Row. NoSuchElementException. Fetched author into info_list because Tags empty')                
                info_list.append(author)
                info_list_w_author.append(author)# = [author]              
                
                with open("quote_nlp_dataset.csv", "a", newline="" , encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([author, quote, info_list, info_list_w_author])               
            
            except Exception as e: # handles other rare exceptions 
                traceback.print_exc()
                continue                

        # if(initial_scrap_page): 
        #     initial_scrap_page = False             
        

            # #time.sleep(1)
            # df = pd.DataFrame(data=quote_data, columns=quote_data[0].keys())
            # df.to_csv("quote_details.csv", index=False)



if __name__ == "__main__":

    # create csv file to enter column headers:
    try:
        with open("quote_nlp_dataset.csv", encoding="utf-8") as csvfile: #"a", newline="", 
            print('\ncsvfile encoding info',csvfile)
            pd.read_csv('quote_nlp_dataset.csv', encoding='utf-8', engine='python')#sep='delimiter')#,on_bad_lines='skip')#, )#,) #cp1252
    
    except pd.errors.EmptyDataError:
        print('\n\t == File is empty. writing header columns ==')
        with open("quote_nlp_dataset.csv", "a", newline="" , encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["attirbuted author", "quote", "quote_info_list", "quote_info_list_w_author"])           
    
    # scraping prepare: 
    webdriver_path = "G:\dokkho week 12\inan_scraper_\chromedriver-win64\chromedriver.exe"
    
    scrap_paths = [
        'quotes',
        'quotes/tag/inspirational-quotes', #quotes/tag/inspiration seems lowkey better. final verdict
        'quotes/tag/death', 
        'quotes/tag/wisdom', 
        'quotes/tag/life',  
        'quotes/tag/truth', 
        'quotes/tag/success', 
        'quotes/tag/time', 
        'quotes/tag/love', #quotes/tag/love-quotes is richer
        'quotes/tag/science', 
        'quotes/tag/humor',
        'quotes/tag/god',
        'quotes/tag/motivational',    
        'quotes/tag/life-lessons',   
        'quotes/tag/happiness'      
    ]
    
    for topic in scrap_paths:
        if topic not in ['quotes/tag/god', 'quotes/tag/happiness' ,'quotes/tag/motivational', 'quotes/tag/life-lessons']: 
            continue
        driver = webdriver.Chrome(webdriver_path)#, chrome_options=chrome_options) 
        # set start_page from scrap_tracker.json['latest_page'] if scrap inturuppted before
        quote_scraper(f"https://www.goodreads.com/{topic}", start_page=1)



# •  Philosophy
# knowledge
#life lesson
# •  Happiness
# •  Religion
# •  Motivational
# •  God
# •  Writing
# ignore poetry

# •  Poetry Quotes at last
    # df = pd.read_csv('quote_nlp_dataset.csv')
    #give me unique quote count
    # df.drop_duplicates(subset="quote",
    #                     keep='first', inplace=True)

    
