#!/usr/bin/python

labels = ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle', 'snapdragon', "colt's foot", 'king protea', 'spear thistle', 'yellow iris', 'globe-flower', 'purple coneflower', 'peruvian lily', 'balloon flower', 'giant white arum lily', 'fire lily', 'pincushion flower', 'fritillary', 'red ginger', 'grape hyacinth', 'corn poppy', 'prince of wales feathers', 'stemless gentian', 'artichoke', 'sweet william', 'carnation', 'garden phlox', 'love in the mist', 'mexican aster', 'alpine sea holly', 'ruby-lipped cattleya', 'cape flower', 'great masterwort', 'siam tulip', 'lenten rose', 'barbeton daisy', 'daffodil', 'sword lily', 'poinsettia', 'bolero deep blue', 'wallflower', 'marigold', 'buttercup', 'oxeye daisy', 'common dandelion', 'petunia', 'wild pansy', 'primula', 'sunflower', 'pelargonium', 'bishop of llandaff', 'gaura', 'geranium', 'orange dahlia', 'pink-yellow dahlia?', 'cautleya spicata', 'japanese anemone', 'black-eyed susan', 'silverbush', 'californian poppy', 'osteospermum', 'spring crocus', 'bearded iris', 'windflower', 'tree poppy', 'gazania', 'azalea', 'water lily', 'rose', 'thorn apple', 'morning glory', 'passion flower', 'lotus', 'toad lily', 'anthurium', 'frangipani', 'clematis', 'hibiscus', 'columbine', 'desert-rose', 'tree mallow', 'magnolia', 'cyclamen ', 'watercress', 'canna lily', 'hippeastrum ', 'bee balm', 'ball moss', 'foxglove', 'bougainvillea', 'camellia', 'mallow', 'mexican petunia', 'bromelia', 'blanket flower', 'trumpet creeper', 'blackberry lily']
import MySQLdb as mysql
import wikipedia 
import sys
from retrying import retry

conn = mysql.connect('localhost', 'testuser', 
        'test623', 'demoflowerdb');
cur = conn.cursor()

conn.set_character_set('utf8')
cur.execute('SET NAMES utf8;') 
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')
#cur.execute("select * from flower")
#rows = cur.fetchall()
#for row in rows:
#    print row

@retry(stop_max_attempt_number=2)
def getinfo(conn,cur,index,count):
    print index
    print count
    try:
	content = wikipedia.search(index,"flower")
    	page = wikipedia.page(content[0])
	description = page.content    
    	web = page.url
    	print description
    	print web
    except  Exception:
	print "###########ERRO################"
	return 0
    try:
    	cur.execute(    "INSERT INTO flower(name, \
    		  id, description, web) \
    		   VALUES ('%s', '%d', '%s', '%s' )" % \
    		   (index, count, description[1:500],web ))
    except Exception:
	print "############ERRO################"
    	return -1
    conn.commit()
    return 1

count =1
for index in labels:
    count = count + 1
    getinfo(conn,cur,index,count)

conn.close()

cur.execute("select * from flower")
rows = cur.fetchall()
for row in rows:
    print row
























