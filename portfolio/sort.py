#Deze functie sorteert de queryselector van work-experiences op datum, de startdatum wordt hiervoor gebruikt. 
# queryselector is een lijst van dictionaries. 

def work_date_sort(queryselector):
    sorted_by_year = sorted(queryselector,key = get_work_year,reverse=True) 
    sorted_by_month = sorted(sorted_by_year, key= get_work_month, reverse=True)
    return sorted_by_month
    
# de queryselector is een lijst van dictionaries, waar ieder dictionary voor een object staat.
# dates staan in de database in de volgende format: {eerste 3 letters maand}. {jaar}
def get_work_year(work_object):
    year = int(work_object.job_start_date.split(". ")[-1]) 
    return year

def get_work_month(work_object):
    month = work_object.job_start_date.split(". ")[0]
    indexed_month = month_index(month)
    return indexed_month

def education_date_sort(queryselector):
    sorted_by_year = sorted(queryselector,key = get_education_year,reverse=True) 
    return sorted_by_year
    

def get_education_year(education_object):
    year = int(education_object.edu_start_date)
    return year

def month_index(month):
    index = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'mei': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'okt': 10, 'nov': 11, 'dec': 12
    }
    return index[month.lower()]


