import requests
import mysql.connector
from mysql.connector import errors

db_conn = mysql.connector.connect(
   host="localhost",
   user="root",
   password = '',
   db = 'api_db'  
)
cursor = db_conn.cursor()
datas = requests.get("http://universities.hipolabs.com/search?country=United+States")
feedbacks = datas.json()
country = ''
name = ''
domains = ''
web_pages = ''
for data in feedbacks:
    country += data['country']
    name += data['name']
    domains += data['domains'][0]
    web_pages += data['web_pages'][0]
    # if cursor:
    #    query = "INSERT INTO `unitab` VALUES (%s, %s, %s, %s, %s)"
    #    values = ('', country, name, domains, web_pages)
    #    if db_conn.is_connected():
    #        cursor.execute(query, values)
    #        db_conn.commit()
    #        info = db_conn.get_server_info()
    #        print('database created ' + info)
    #    else:
    #        print('unable to create data')
    # else:
    #     print('off')

# print(web_pages)
# write_pdf = open("pag.pdf", 'w')
# note = write_pdf.write(web_pages)
# write_pdf.close()
print(web_pages)
write_pdf = open("nom.pdf", 'w', encoding='utf-8')
note = write_pdf.write(name)
write_pdf.close()
