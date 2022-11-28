from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)
@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/adminadd_category',methods=['get','post'])
def adminadd_category():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="update":
		q="select * from category where cat_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updatecat']=res
		print(res)
	if action=="delete":
		q="delete from category where cat_id='%s'"%(id)
		delete(q)
	if 'update' in request.form:
		category=request.form['name']
		content=request.form['content']
		q="update category set cat_name='%s',content='%s' where cat_id='%s'"%(category,content,id)
		update(q)
		print(q)
	if 'submit' in request.form:
		category=request.form['name']
		content=request.form['content']
		q="insert into category values(null,'%s','%s')"%(category,content)
		insert(q)
	q="select * from category"
	res=select(q)
	data['cat']=res
	return render_template('adminaddcategory.html',data=data)	
@admin.route('/adminadd_product',methods=['get','post'])
def admindadd_product():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="update":
		q="select * from product where product_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updateproduct']=res
		print(res)
	if action=="delete":
		q="delete from product where product_id='%s'"%(id)
		delete(q)
	if 'update' in request.form:
		product=request.form['pname']
		amount=request.form['amount']
		q="update product set product_name='%s',amount='%s' where product_id='%s'"%(product,amount,id)
		update(q)
		print(q)
	if 'submit' in request.form:
		product=request.form['pname']
		image=request.files['pimage']
		path='static/images/'+str(uuid.uuid4())+image.filename
		image.save(path)
		category=request.form['cat']
		amount=request.form['amount']
		q="insert into product value(null,'%s','%s','%s','%s')"%(category,product,amount,path)
		insert(q)
	q="SELECT * FROM `category`"
	res=select(q)
	data['category']=res
	q="select * from product inner join category using(cat_id)"
	res=select(q)
	data['cat_prt']=res

	return render_template('adminaddproduct.html',data=data)		