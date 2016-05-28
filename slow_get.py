#coding=utf-8
from pyquery import PyQuery as pq
import sqlite3,os

def get_stock_name(stocksindex,cursor):
	stock_dict={}
	for i in stocksindex:
		stock_name=[]
		page=0
		cursor.execute('create table  %s (name varchar(20) primary key,id int,stock_name varchar, last_trade varchar, img varchar, change varchar, vol varchar)'%i)
		while True:
			
			try:
				url='https://finance.yahoo.com/q/cp?s=%5E'+i+'&c='+str(page)#build urls for DOW and NASDAQ in stocksindex
				print url
				d= pq(url=url)
				for j in range(0,len(d('.yfnc_tabledata1')),5):#table has five cols,so each five has a name ,list all names on this page
						name=pq(d('.yfnc_tabledata1')[j]).text()
						print name
						stock_name.append(name)
						cursor.execute('insert into %s (name) values (\'%s\')'%(i,name))

				if len(d("div[align='right']").find("a"))==0 or len(d('.yfnc_tabledata1'))<1:#if it is the last page
					print '!!!!!'
					break
				else:
					print '$$$$$'
					page+=1
				
			finally:
				print '@@@@'
		stock_dict[i]=stock_name
	return stock_dict
def get_stock_inform(stock_name,cursor):
	for index ,names in stock_name.iteritems():
		id=0
		for  name in names:
			url='https://finance.yahoo.com/q?s='+name
			try:
				d= pq(url=url)
				stock_name=d('.title').text()
				last_trade=d('.time_rtq_ticker').text()
				if pq(d('.yfi_rt_quote_summary img:eq(0)')).attr('alt')=='Down':
					change='-'+d('.time_rtq_content').text()
				else:
					change='+'+d('.time_rtq_content').text()
				print d('.time_rtq_content').text()
				vol= d('#table2 tr:eq(2) .yfnc_tabledata1').text()
				img= d('.chart img').attr('src')
				cursor.execute("UPDATE %s set id=%d,last_trade = '%s',stock_name='%s', change = '%s', img='%s',vol='%s' WHERE name = '%s'"%(index,id,last_trade,stock_name.replace('\'',' '),change,img,vol,name))

			finally:
				id+=1
				print url
def run():
	stocksindex=['DJI','IXIC']
	db= sqlite3.connect('tst.db')
	cursor = db.cursor()
	get_stock_inform(get_stock_name(stocksindex,cursor),cursor)
	cursor.close()
	db.commit()
	db.close()
while 1:
	run()
	os.remove('test.db')
	os.rename('tst.db','test.db')