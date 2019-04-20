import requests
import re
from selenium import webdriver
import time

TURN_ON_REAL_REGISTRATION = True

#set the module as the planner
module = 'reg/plan/add_planner.pl'
is_planner = 'Y'

if TURN_ON_REAL_REGISTRATION:
    #set the module for real class registration
    module = 'reg/add/confirm_classes.pl'
    is_planner = ''
    
    
'''
Press F12 in chrome, navigate to the Network tab, then go to your planner on student link, 
click on the item with a long number, under request headers find "Cookie: .... " 
Copy the `cookie` header below
'''
cookies = 'f5_cspm=1234; f5avrbbbbbbbbbbbbbbbb=APIEJCLNAMIDIBIFIMDDLOKPBKNPDKOHADKAENEMGPBJGNFEJAIFCDGJAPOFPMLKEGMDKMNLGFKMKACLHOJAECGFCAPEHDDCJAHNNLJDKKMAICOODBMFECPFCNKCKGGE; _ga=GA1.2.1973835121.1521203300; pt_4b45e398=uid=oW05zkxRdb49sirqCdZOsw&nid=0&vid=ETL2HzRua6yYk/9HnTTZzA&vn=2&pvn=1&sact=1522860206796&to_flag=1&pl=YN2/tT8qowgjcGl1hAIplQ*pt*1522860191391; __lc.visitor_id.5084411=S1522952284.be596373f4; wantsMobile=true_1.2_manual; _fbp=fb.1.1549473602301.1429493471; BIGipServerist-wp-assets-prod-80-pool=1910632714.20480.0000; uiscgi_prod=a4d39148ba5c0b8d3b1986c094b6f9d9:prod; BIGipServerist-uiscgi-app-prod-443-pool=1204143488.47873.0000; BIGipServerist-uiscgi-app-prod-80-pool=1204143488.20480.0000; BIGipServerist-web-legacy-prod-80-pool=1662710026.31745.0000; BIGipServerist-wp-app-prod-443-pool=1843523850.20480.0000; BIGipServerist-wp-assets-prod-443-pool=1910632714.20480.0000; __utmc=21468840; BIGipServerist-wp-app-prod-80-pool=1877078282.20480.0000; BIGipServerist-web-content-prod-443-pool=973727498.47873.0000; BIGipServerist-web-phpbin-prod-443-pool=2162476416.46080.0000; BIGipServerist-uiscgi-content-prod-443-pool=1913054986.47873.0000; weblogin3=a6ce59c3f26e451804769b076596de44:cussp-srv3; BIGipServerist-web-content-prod-80-pool=973727498.20480.0000; BIGipServerist-web-phpbin-prod-80-pool=2162476416.46080.0000; recaptcha_token=03AOLTBLR3xJI-EGbHQbVtECTrCT70uD-6Ikp1EVXdYaD__FL1Goll3mN59WymODeW2FCHWk15OU6HmWDyogaNVDnzGJeXfUjtsHSuChvSQPOEmxrIdzWGHLb9vyK3O69zDKZZ2fwtwswKG_VJBA5wok9twhvfdcWCaOo6g4096SiKBZ5MBBzR3QcyKz7M1Es-8Ip8ut8IHBKmwpRjuI_sxPXfZEn7Hs8EgEnWCaluo8tV4el3REw18H3KdxzFvpX0PQp1VQQ_vPlDU_t1aIt8uMr18fbjNq1koK8740iG06VmXzZ5txzqFYF80pY4obq1U8ETvUIkyhc-; isMobile=false_1.2; credsrv3=cussp-srv3.bu.edu; twHelpLastPage=12747; BIGipServerwww-prod-crc-443-pool=374219533.47873.0000; BIGipServerwww-prod-crc-80-pool=1649287949.20480.0000; __utma=21468840.1973835121.1521203300.1555280370.1555301302.139; __utmz=21468840.1555301302.139.106.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmt_b=1; __utmb=21468840.2.10.1555301302'


#You might also have to copy the other headers into here
def generate_headers():
    return {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': cookies,
    'DNT': '1',
    'Host': 'www.bu.edu',
    'Referer': 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1555301829?ModuleName=reg%2Fadd%2F_start.pl&ViewSem=Fall%202019&KeySem=20203',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }



url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1524289373'

def generate_params(college, dept, course, section):
    return {
    'College': college,
    'Dept': dept,
    'Course': course,
    'Section': section,
    'ModuleName': 'reg/add/browse_schedule.pl',
    'AddPreregInd': '',
    'AddPlannerInd': '',
    'ViewSem': 'Fall 2019',
    'KeySem': '20203',
    'PreregViewSem':  '',
    'PreregKeySem':  '',
    'SearchOptionCd': 'S',
    'SearchOptionDesc': 'Class Number',
    'MainCampusInd': '',
    'BrowseContinueInd': '', 
    'ShoppingCartInd': '' ,
    'ShoppingCartList': '' }

def generate_reg_params(college, dept, course, section, ssid):
    return {'SelectIt': ssid, 
    'College':college.upper(),
    'Dept':dept.upper(),
    'Course':course, 
    'Section':section.upper(),
    'ModuleName': module,
    'AddPreregInd': '',
    'AddPlannerInd': is_planner,
    'ViewSem':'Fall 2019',
    'KeySem':'20203',
    'PreregViewSem':'',
    'PreregKeySem':'',
    'SearchOptionCd':'S',
    'SearchOptionDesc':'Class Number',
    'MainCampusInd':'',
    'BrowseContinueInd':'',
    'ShoppingCartInd':'',
    'ShoppingCartList':''}
    
# Replace with your own BU login and password.
# Your credentials are only stored in this file, and I am not liable if you expose this file to anyone else.
def credentials():
    return ('lifu', 'ALex991188.')

def login():
    print('logging in...')
    driver = webdriver.Chrome()

    driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1524541319?ModuleName=regsched.pl")
    username, password = credentials()
    driver.find_element_by_id('j_username').send_keys(username)
    driver.find_element_by_id('j_password').send_keys(password)
    driver.find_element_by_class_name('input-submit').click()
    while 'studentlink' not in driver.current_url:
        time.sleep(3)
        
    cookies_list = driver.get_cookies()
    global cookies
    cookies = ''
    for cookie in cookies_list:
        cookies = cookies + cookie['name'] + '=' + cookie['value'] + '; '
    print('Retrieving cookies: ' + cookies)
    driver.close()

'''
Finds course listing and tries to register for the class.

Sometimes course names are wrong, use at your own discretion. 
'''
def find_course(college, dept, course, section):
    name =  dept.upper() + course + ' ' + section.upper()
    print('searching for ' + name)
    params_browse = generate_params(college, dept, course, section)
    headers = generate_headers()
    ####
    for retry in range(1, 5):
        #logging.warning('[fetch] try=%d, url=%s' % (retry, url))
        retry_because_of_timeout = False
        try:
            r = requests.get(url, headers=headers,params=params_browse, timeout = 3)
            text = r.text
        except Exception as e:
            retry_because_of_timeout=True
            pass
    
        if retry_because_of_timeout:
            time.sleep(retry * 2 + 1)
        else:
            break
    ####
    #print(r.text)
    #(?<=abc)
    p = re.compile('<tr ALIGN=center Valign= top>.+?</td></tr>', re.DOTALL)
    m = p.findall(text)
    if len(m) == 0:
        print('Something went wrong with the request for ' + dept + course)
        login()
        find_course(college, dept, course, section)
        return
    s = college.upper() + dept.upper() + course + '%20' + section.upper()

    found = False
    for item in m:
        if re.search(s, item):
            found = True
            n = re.search('value="(\d{10})"', item)
            if n:
                params_reg = generate_reg_params(college, dept, course, section, n.group(1))
                reg = requests.get(url, headers=headers,params=params_reg)
                o = re.search('<title>Error</title>', reg.text)
                if o:
                    print('Can not register yet :/')
                else:
                    print('Registered successfully!')
            else:
                print('Class is full :(')
            break
    if not found:
        print('could not find course')

# Replace with your own course.
# Ex. ('cas','wr','100','a1')
my_courses = [('ENG', 'EC', '401', 'A1')]

beginning = time.time()
cycles = 0
login()
while True:
    for i in my_courses:
        print('\n['+str(time.asctime())+']')
        start = time.time()
        find_course(*i)
        duration = (time.time() - start)
        print('Took ' + str(round(duration, 1)) + ' seconds')
        cycles+=1
        print('Average time: ' + str(round((time.time() - beginning)/cycles,1)))


    
