#module for the program's internal FUNCTIONS
import  re
 
def  fetch_cpf ( text ):
 """Function to search for CPF in the text that was extracted.
 \n Returns a list with the CPFs found or False if it does not exist.
 \n To be found, the value must be in the format xxx.xxx.xxx-xx.
 \ nExample:
text = text extracted from the image
CPFs = fetch_cpf(text)"""
 CPF  =  re . findall ( '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}' , text )
 if  len ( CPF ) > 0 :
 return  CPF
 else :
 false
 
 
def  fetch_date ( text ):
 """Function to search for dates in the text that was extracted.
 \n Returns a list with the dates found or False if it doesn't exist.
 \n To be found, the value must be in the format xx/xx/xxxx.
 \ nExample:
text = text extracted from the image
Dates = fetch_date(text)"""
 DATE  =  re . findall ( '[0-9]{2}/[0-9]{2}/[0-9]{4}' , text )
 if  len ( DATE ) > 0 :
 return  DATE
 else :
 false
 
 
def  fetch_words_mas ( text ):
 """Function to search for 'mas' (bad) words in the extracted text.
 \n Disregard repeated words. Returns an int, float.
 \n Respectively the number of words found and the percentage of them in the whole text.
 \ nExample:
text = text extracted from the image
amount, percentage = search_words_mas(text)"""
 bad_count  =  0
 mas_words  =  open ( "functions/mas_words.txt" ). read ()
 but_words  =  but_words . split ( " \n " )
 text_words  =  set ( re . split ( '[,;.?!/-: ]' , text ))
 for  i  in  text_words :
 if  i . upper () in  word_mas :
 bad_count  +=  1
 percent  =  calculate_percent ( bad_count , len ( text_words ) )
 
 return  bad_count , percentage
 
 
def  fetch_good_words ( text ):
 """Function to search for 'good' words in the extracted text.
 \n Disregard repeated words. Returns an int, float.
 \n Respectively the number of good words found and the percentage of them in the whole text.
 \ nExample:
text = text extracted from the image
quantity, percentage = fetch_good_words(text)"""
 count_well  =  0
 good_words  =  open ( "functions/good_words.txt" ). read ()
 good_words  =  good_words . split ( " \n " )
 text_words  =  set ( re . split ( '[,;.?!/-: ]' , text ))
 for  i  in  text_words :
 if  i . upper () in  goodwords :
 count_well  +=  1
 percentage  =  calculate_percent ( count_well , len ( text_words ) )
 
 return  count_well , percentage
 
 
def  calculate_percent ( amount , size ):
 """Function to calculate the percentage of good/bad words.
 \n Returns float, the percentage.
 \ nExample:
quantity = quantity of good/but words
size = number of words in the text
percentage = calculate_percent(amount, size)"""
 percentage  = ( amount  /  size ) *  100
 return  percentage
 
 
def  summarize_cpf ( cpf ):
 """Function to leave the CPF in string.
 \n Returns string.
 \ nExample:
cpf = list of CPFs found in the text
CPF = summarize_cpf(cpf)"""
 CPF  =  ""
 for  i  in  cpf :
 CPF  +=  i + "."
 return  CPF
 
 
def  summarize_dates ( dates ):
 """Function to leave the Date in a string.
 \n Returns string.
 \ nExample:
dates = list of dates found in the text
DATES = summarize_dates(dates)"""
 DATE  =  ""
 for  i  in  dates :
 DATE  +=  i + "."
 return  DATE