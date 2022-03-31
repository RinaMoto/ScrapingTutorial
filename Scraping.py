import requests
from bs4 import BeautifulSoup

def extract(page):
    job = "Software Engineer"
    Location = "Remote"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q={job}&l={Location}&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    
    arr = []
    divs = soup.find_all('div', class_ = "job_seen_beacon")

    # iterate through the div 
    for item in divs:
        title = item.find('h2').text.strip()

        # find company name via the span element and class name
        company = item.find('span', class_ = 'companyName').text.strip()

        # span element includes the phrase "new", so remove that here
        title = title.replace("new", '')
     
        # attempt to find salary 
        try:
            salary = item.find('span', class_ = "estimated-salary").text.strip()
          
        except: 
            salary = ''
       

        # job description
        summary = item.find('div', class_ = 'job-snippet').text.strip()
        
       

        job = {'title': title, 'company': company, 'salary': salary, 'summary': summary}
        # go through the array and append to the data sheet
        arr.append(job)

    return arr

if __name__ == "__main__":
    # takes the first 2 pages
    for i in range(0, 20, 10):
        c = extract(i)
        print(transform(c))