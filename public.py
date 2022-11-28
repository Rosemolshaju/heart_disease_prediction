from flask import *
from database import *
public=Blueprint('public',__name__)
@public.route('/',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where user_name='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.adminhome'))
	return render_template('login.html')

@public.route('/register',methods=['get','post'])
def register():
	if 	'submit' in request.form:
		name=request.form['username']
		address=request.form['address']
		email=request.form['email']
		username=request.form['uname']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','user')"%(username,password)
		id=insert(q)
		q="insert into register values(null,'%s','%s','%s','%s')"%(id,name,address,email)
		insert(q)
	return render_template('register.html')	