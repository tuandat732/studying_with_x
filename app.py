from flask import *
# from layde import hoa_collection
from models.layde import dtb 
from models.layuser import user
from models.chothai import cnhn,tuvan,db_demo,lienhe1,cauhoi,db_demo4,dapan_data
from bson.objectid import ObjectId
from models.laytailieu import dtb_tailieu
import random
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
dict_mon = {'toan':'Toán','li':'Lý','hoa':'Hóa','anh':'Anh','sinh':'Sinh','van':'Văn'}

@app.route('/')
def re():
  if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  return redirect('/tin-tuc/tintuc2') 

@app.route('/info')
def info():
  if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  return render_template('info.html',user=session['user'],login=session['logged'],id_login=session['id_login'])

@app.route('/lienhe', methods=["GET", "POST"])
def lienhe():
  if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  else:
    if request.method=='GET':
      return render_template('lienhegopy.html',user=session['user'],login=session['logged'],id_login=session['id_login'])
    else:
      form=request.form
      user_lienhe={
        'hoten':form['input_hoten'],
        'email':form['input_email'],
        'SDT':form['input_SDT'],
        'tieude':form['input_tieude'],
        'noidung':form['input_noidung'],
      }
      lienhe1.insert_one(user_lienhe)
      return redirect('/lienhe')

@app.route('/sign-in', methods=["GET", "POST"])
def login():
    # if 'logged' in session:
        if session['logged'] == True:
            return redirect('/luyende')
        else:
            if request.method == 'GET':
                return render_template('sign_in.html')
            elif request.method == 'POST':
                form = request.form
                input_username = form['username']
                input_password = form['password']
                check_user = user.find_one({'username': input_username,'password': input_password})
                if check_user:
                    session["logged"] = True
                    session['user']=input_username
                    session['id_login']=str(check_user['_id'])
                    if session['diachi']=='luyende': 
                      return redirect('/luyende')
                    elif session['diachi']=='profile':
                      return redirect('/profile/{}'.format(session['id_login']))
                    else:
                      return redirect('/luyende/{}'.format(session['diachi']))

                else:
                    # check = False
                    return render_template('sign_in.html',check = False)
    # else:
    #     session['logged'] = False
    #     return redirect('/sign-in')

@app.route('/sign-out')
def logout():
    # if 'logged' in session:
  session['logged'] = False
  session['user']=''
  session['id_login']=''
  return redirect('/tin-tuc/tintuc2')


@app.route('/sign-up', methods = ["GET","POST"])
def signup():
  if request.method == 'GET':
    return render_template('sign_up.html')
  elif request.method == 'POST':
    form = request.form
    ho_va_ten = form['fullname']
    get_username = form['username']
    get_password = form['password']
    get_email = form['email']
    get_confirm =form['confirm']
    get_birthday = form['birthday']
    # get_grade = form['grade']
    get_school =form['school']
    get_gradeofuser = form['gradeofuser']
    get_gender = form['gender']
    get_telephone = form['telephone']
    
    check_full = True
    for i in form :
      if form[i]  == '':
        check_full = False
        return render_template('sign_up.html',check_full = check_full) 
    check_full_password = True
    if len(get_password) < 8 :
      check_full_password = False
      return render_template('sign_up.html',check_full_password = check_full_password)
      
    
      
    check_confirm = True
    check_username = True 
    check_user = user.find_one({'username':get_username})
    if get_password != get_confirm :
      check_confirm = False
      return render_template('sign_up.html',check_confirm = check_confirm)
    if check_user != None :
      check_username = False
      return render_template('sign_up.html',check_username = check_username)
    new_user = {
      'username':get_username,
      'password':get_password,
      'ho_va_ten':ho_va_ten,
      'email':get_email,
      'birthday':get_birthday,
      # 'grade':get_grade,
      'school':get_school,
      'gradeofuser':get_gradeofuser,
      'gender':get_gender,
      'telephone':get_telephone,
      'toan':[],
      'li':[],
      'hoa':[],
      'anh':[],
      'sinh':[],
      'diem_toan':[],
      'diem_li':[],
      'diem_hoa':[],
      'diem_anh':[],
      'diem_sinh':[]
      }
    user.insert_one(new_user)
    return redirect('/sign-in')


@app.route('/tin-tuc/<loai>')
def home(loai):
    cnhnn=db_demo[loai]
    tintuc = cnhnn.find()
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
    return render_template('home.html',user=session['user'],login=session['logged'],tintuc=tintuc,id_login=session['id_login'],loai=loai)

@app.route('/tin-tuc/<loai>/<id>')
def tin_tuc(id,loai):
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
    cnhnt=db_demo[loai]
    tintuc = cnhnt.find_one({'_id': ObjectId(id)})
    html = tintuc['ndct']
    cnhnm = db_demo[loai]
    tintuc1=cnhnm.find()
    return render_template("tin1.html",ndct=html,tintuc1=tintuc1,id_login=session['id_login'],user=session['user'],login=session['logged'],loai=loai)

@app.route('/luyende')
def luyende():
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  # if 'logged' in session :
    if session['logged']:
      return render_template('luyende.html', dict_mon = dict_mon,user=session['user'],login=session['logged'],id_login=session['id_login'])
    else :
      session['diachi']='luyende'
      return redirect('/sign-in')
  # else :
  #   return redirect('/sign-in')


@app.route('/luyende/<mon>', methods=["GET", "POST"])
def hoa(mon):
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  # if 'logged' in session :
    if session['logged']:
      mon_collection = dtb[mon]
      hoa = mon_collection.find()
      mon1 = mon
      diem = 0
      if request.method == "GET":
        return render_template('dethithu.html', hoa=hoa, mon1=str(mon1),user=session['user'],login=session['logged'],id_login=session['id_login'] )
      elif request.method == "POST":
          form = request.form
          list_hoa = list(hoa)
          caulamdung=[]
          caudalam=[]
          for i in form:
            for j in list_hoa:
              if int(i) == int(j['cau']):
                caudalam.append(i)
                if form[i] == j['dap_an']:
                  diem += 1
                  caulamdung.append(i)
          session['diem']=len(list_hoa)
          session['caulamdung']=caulamdung
          session['caulam']=caudalam
          #tinh_diem
          if mon in ['toan','anh'] :
            diem50 = diem/5
            if mon == 'toan':
              user.update_one({'username':session['user']},{ '$push': { 'diem_toan' : diem50 }})
            if mon == 'anh':
              user.update_one({'username':session['user']},{ '$push': { 'diem_anh' : diem50 }})

          if mon in ['li','hoa','sinh'] :
            diem40 = diem/4
            if mon == 'li':
              user.update_one({'username':session['user']},{ '$push': { 'diem_li' : diem40 }})
            if mon == 'hoa':
              user.update_one({'username':session['user']},{ '$push': { 'diem_hoa' : diem40}})
            if mon == 'sinh' :
              user.update_one({'username':session['user']},{ '$push': { 'diem_sinh' : diem40}})
              #het
          user.update_one({'username':session['user']},{ '$push': { mon : diem }})
          return redirect('/luyende/{}/result'.format(mon))
    else :
      session['diachi']=mon
      return redirect('/sign-in')
  # else :
  #     return redirect('/sign-in')

          
@app.route('/luyende/<mon>/result')
def result(mon):
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  # if 'logged' in session :
    if session['logged']: 
      mon_collection = dtb[mon]
      hoa = mon_collection.find()
      account = user.find_one({'username':session['user']})
      list_mon = account[str(mon)]
      diem = list_mon[-1]
      tong_so_cau = session['diem']
      tongcau=[]
      for i in range(tong_so_cau):
        tongcau.append(str(i+1))
      bang_xep_hang = [
      {
      'username':'unknown',
      'best_score': 0
      }
        ]
      list_user = user.find()
      for i in list_user:
        if i[mon]!=[]:
          best_score = max(i[mon])
          username = i['username']
          id_user = i['_id']
          new_high_user = {
            'username':username,
            'best_score':best_score,
            'id':id_user
          }
          bang_xep_hang.append(new_high_user)
      for j in range(len(bang_xep_hang)) :
        for k in range (j+1,len(bang_xep_hang)):
          if bang_xep_hang[j]['best_score'] < bang_xep_hang[k]['best_score'] :
            switch = bang_xep_hang[j]
            bang_xep_hang[j] = bang_xep_hang[k]
            bang_xep_hang[k] = switch
      return render_template('diem.html', hoa=hoa,diem = diem, tong_so_cau = tong_so_cau , bang_xep_hang = bang_xep_hang,caulamdung=session['caulamdung'],tongcau=tongcau, caudalamm = session['caulam'],mon=dict_mon[mon],user=session['user'],login=session['logged'],id_login=session['id_login'] )
    else :
      return redirect('/sign-in')
  # else :
  #   return redirect('/sign-in')

@app.route('/tuvan', methods=["GET","POST"])
def tuvan2():
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
    if request.method=="GET":
        return render_template('dattuvan.html',checkload=False,user=session['user'],login=session['logged'],id_login=session['id_login'])        
    elif request.method =="POST":
        form=request.form
        if form['subject'] != 'Chọn' and form['school'] !='Chọn':
          dss=tuvan.find({'school':form['school']})
          ds=[]
          for i in dss:
            if form['subject'] in i['subject']:
              ds.append(i)
        elif form['subject'] != 'Chọn':
            dss=tuvan.find()
            ds=[]
            for i in dss:
              if form['subject'] in i['subject']:
                ds.append(i)
        elif form['school'] != 'Chọn':
          ds=tuvan.find({'school':form['school']})
        else: ds=tuvan.find()
        if ds != []:
          if form['mark'] != '':
            diemnhap1=(str(form['mark'])).replace(',','',-1).replace('.','',-1).replace(' ','',-1)
            if diemnhap1.isdigit():
              diemnhap=(str(form['mark'])).replace(',','.',-1).split()
              tong=0
              ds_do=[]
              ds_cothedo=[]
              for i in diemnhap:
                tong=tong+float(i)
              for i in ds:
                if i['mark']!='---':
                  if float(i['mark']) <= (tong/len(diemnhap))+1:
                    ds_do.append(i)
                  elif (tong/len(diemnhap)) < float(i['mark']) <= (tong/len(diemnhap))+5:
                    ds_cothedo.append(i)
              if (ds_do != []):
                return render_template('dattuvan.html' ,ds_do=ds_do,ds_cothedo=ds_cothedo,checkdiem='True',user=session['user'],login=session['logged'],id_login=session['id_login'])
              else: return render_template('dattuvan.html' ,ds_do=ds_do,ds_cothedo=ds_cothedo,checkdiem='False',user=session['user'],login=session['logged'],id_login=session['id_login'])
            else: return render_template('dattuvan.html',checkdiem='sai',user=session['user'],login=session['logged'],id_login=session['id_login'])    
          else:
            return render_template('dattuvan.html' ,ds=ds,checkload='True',user=session['user'],login=session['logged'],id_login=session['id_login'])
        else: return render_template('dattuvan.html' ,ds=ds,user=session['user'],login=session['logged'],checkload='False',id_login=session['id_login'])


@app.route('/profile/<id>')
def profile(id):
    if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
    user_profile = user.find_one({'_id':ObjectId(id)})
    list_diem_hoa = user_profile['diem_hoa']
    list_diem_toan = user_profile['diem_toan']
    list_diem_li = user_profile['diem_li']
    list_diem_sinh = user_profile['diem_sinh']
    list_diem_anh = user_profile['diem_anh']
    users = user.find()
    list_user = list(users)
    random.shuffle(list_user) 
    return render_template('profile.html',user_profile = user_profile, list_user = list_user , list_diem_hoa = list_diem_hoa
    ,list_diem_toan =list_diem_toan ,list_diem_li = list_diem_li,list_diem_sinh =list_diem_sinh,list_diem_anh = list_diem_anh,id_login=session['id_login'],user=session['user'],login=session['logged'])

@app.route('/profile/')
def pro():
  session['diachi']='profile'
  return redirect('/sign-in')

@app.route('/tailieu')
def tai_lieu():
  if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  tailieu_hoa = dtb_tailieu['hoa'].find()
  tailieu_anh = dtb_tailieu['anh'].find()
  tailieu_sinh = dtb_tailieu['sinh'].find()
  tailieu_toan = dtb_tailieu['toan'].find()
  tailieu_li = dtb_tailieu['li'].find()
  tailieu_van = dtb_tailieu['van'].find()
  return render_template('tailieu.html',tailieu_hoa =tailieu_hoa ,tailieu_anh= tailieu_anh,tailieu_li = tailieu_li, tailieu_sinh = tailieu_sinh, tailieu_toan = tailieu_toan,tailieu_van = tailieu_van,id_login=session['id_login'],user=session['user'],login=session['logged'])


@app.route('/tailieu/<mon>')
def tai_lieu_mon(mon):
  if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  tailieu_mon = dtb_tailieu[mon].find()
  return render_template('tailieumon.html', tailieu_mon = tailieu_mon,id_login=session['id_login'],user=session['user'],login=session['logged'],mon=dict_mon[mon] )

@app.route('/giaitri')
def vid():
  return render_template('vid.html',id_login=session['id_login'],user=session['user'],login=session['logged'])

@app.route('/tracnghiemtc',methods=["GET", "POST"])
def tntc():
  if 'logged' not in session:
      session['logged']=False
      session['user']=''
      session['id_login']=''
  else:
    if request.method=="GET":
      cauhoi_all=cauhoi.find()
      return render_template('tracnghiemtc.html',id_login=session['id_login'],user=session['user'],login=session['logged'],cauhoi=cauhoi_all) 
    else:
      form=request.form
      cauhoi_all=cauhoi.find()
      if len(form) < 30:
        return render_template('tracnghiemtc.html',id_login=session['id_login'],user=session['user'],login=session['logged'],check='False',cauhoi=cauhoi_all)
      else:
        chon=form['1']+form['15']+form['8']+form['20']
        return redirect('/tracnghiemtc/{}'.format(chon))

@app.route('/tracnghiemtc/<ma>')
def mae(ma):
  nd=dapan_data.find_one({'codeid':ma})
  nt=nd['ndct']
  return render_template('tracnghiem.html',nd=nt,nt=nd,id_login=session['id_login'],user=session['user'],login=session['logged'])

if __name__ == '__main__':
    app.run(debug=True)


