#!/usr/bin/python

labels = ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle', 'snapdragon', "colt's foot", 'king protea', 'spear thistle', 'yellow iris', 'globe-flower', 'purple coneflower', 'peruvian lily', 'balloon flower', 'giant white arum lily', 'fire lily', 'pincushion flower', 'fritillary', 'red ginger', 'grape hyacinth', 'corn poppy', 'prince of wales feathers', 'stemless gentian', 'artichoke', 'sweet william', 'carnation', 'garden phlox', 'love in the mist', 'mexican aster', 'alpine sea holly', 'ruby-lipped cattleya', 'cape flower', 'great masterwort', 'siam tulip', 'lenten rose', 'barbeton daisy', 'daffodil', 'sword lily', 'poinsettia', 'bolero deep blue', 'wallflower', 'marigold', 'buttercup', 'oxeye daisy', 'common dandelion', 'petunia', 'wild pansy', 'primula', 'sunflower', 'pelargonium', 'bishop of llandaff', 'gaura', 'geranium', 'orange dahlia', 'pink-yellow dahlia?', 'cautleya spicata', 'japanese anemone', 'black-eyed susan', 'silverbush', 'californian poppy', 'osteospermum', 'spring crocus', 'bearded iris', 'windflower', 'tree poppy', 'gazania', 'azalea', 'water lily', 'rose', 'thorn apple', 'morning glory', 'passion flower', 'lotus', 'toad lily', 'anthurium', 'frangipani', 'clematis', 'hibiscus', 'columbine', 'desert-rose', 'tree mallow', 'magnolia', 'cyclamen ', 'watercress', 'canna lily', 'hippeastrum ', 'bee balm', 'ball moss', 'foxglove', 'bougainvillea', 'camellia', 'mallow', 'mexican petunia', 'bromelia', 'blanket flower', 'trumpet creeper', 'blackberry lily']


import MySQLdb as mysql
import wikipedia 
import sys
from retrying import retry
import chardet 
import time
import requests
#conn = mysql.connect('localhost', 'testuser', 
#        'test623', 'demoflowerdb');
conn = mysql.connect('localhost','root','balabalabala','flowerdatabase')
cur = conn.cursor()

conn.set_character_set('utf8')
cur.execute('SET NAMES utf8;') 
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')

#@retry(stop_max_attempt_number=1)
def getinfo(conn,cur,index,count,delaytime):
    print "|",time.ctime(),"|",index,"=> data[",count,"]"
    try:
	content = wikipedia.search(index,"flower")
	page = wikipedia.page(content[0])
   	description = wikipedia.summary(content[0])    
    	web = page.url
	description = description.replace('\"'," ")
	description = description.replace("\'"," ")
    except  wikipedia.exceptions.DisambiguationError as err:
	print "|",time.ctime(),"|","##############DISAMBIGUATION IN WIKI###################"
	return getinfo(conn,cur,err.options[0],count,delaytime)
    except wikipedia.exceptions as err:
	print "|",time.ctime(),"|","###################NETWORK ERRO########################"
	description = "failtogetinwiki"
	web = "wiki"
    except requests.exceptions.ConnectionError as err:
	print "|",time.ctime(),"|","#################CONNECT TOO QUICK#####################"
	time.sleep(delaytime*150)
	return getinfo(conn,cur,index,count,delaytime)
    try:
    	index = index.replace("\'"," ")
    	index = index.replace('\"'," ")
	cur.execute(    "INSERT INTO flower(name, \
    		  unique_id, description, web) \
    		   VALUES ('%s', '%d', '%s', '%s' )" % \
    		   (index, count, description,web ))
    except mysql.Error,e:
	print "|",time.ctime(),"|","####################ERRO IN DB########################"
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	return -1

    conn.commit()
    print     "|",time.ctime(),"|","=================INSERT SUCCESSFULLY=================="
    print web
    return 1

count = 0
delaytime = 2
for index in labels:
    time.sleep(delaytime)
    getinfo(conn,cur,index,count,delaytime)
    count = count + 1
conn.close()

#cur.execute("select * from flower")
#rows = cur.fetchall()
#for row in rows:
#    print row
























