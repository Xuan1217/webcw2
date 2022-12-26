from sqlalchemy import and_

from app import app
import time
from flask import render_template, request, flash, redirect, make_response, session, current_app, jsonify
from app.models import*


@app.context_processor
def alert_status():
    status = session.get('status', '')
    return {'status': status}


@app.before_request
def log_each_request():
    app.logger.info('【method】{}【path】{}【addr】{}'.format(request.method, request.path, request.remote_addr))


@app.route('/')
def HomePage():  # put application's code here
    db.create_all()
    return render_template('HomePage.html')


@app.route('/Menu')
def Menu():
    the_menu = Dishes.query.all()
    uid = request.cookies.get('user_id')
    current_app.logger.info("User(ID)" + uid + "enter the menu")
    return render_template('u_menu.html', menu_list=the_menu)


@app.route('/favorite')
def favorite():
    cid = request.args.get('this_id')
    fav_list = Dishes.query.filter(Dishes.Cid == cid).first()
    fav_list.likeNum += 1
    db.session.commit()
    time.sleep(2)
    return redirect('/Menu')


@app.route('/add_shopping')
def add_shopping():
    dishId = request.args.get('this_id')
    userId = request.cookies.get('user_id')
    the_user = Car.query.filter(User.Uid == userId).all()
    the_dishes1 = Dishes.query.filter(Dishes.Cid == dishId).first()
    for i in the_user:
        if i.Uid == userId:
            if i.dish == the_dishes1.dish:
                i.Num += 1
                db.session.commit()
                time.sleep(2)
                return redirect('/Menu')
    car1 = Car(Uid=int(userId), Cid=int(dishId), dish=the_dishes1.dish, price=the_dishes1.price, pic=the_dishes1.pic)
    db.session.add(car1)
    db.session.commit()
    time.sleep(2)
    return redirect('/Menu')


@app.route('/decline_shopping')
def decline_shopping():
    dishId = request.args.get('this_id')
    userId = request.cookies.get('user_id')
    the_user = Car.query.filter(and_(Car.Uid == userId, Car.Cid == dishId)).first()
    if the_user.Num > 1:
        the_user.Num -= 1
        db.session.commit()
        return redirect('/shoppingCar')
    if the_user.Num == 1:
        db.session.delete(the_user)
        db.session.commit()
        return redirect('/shoppingCar')


@app.route('/ad_sh')
def ad_sh():
    dishId = request.args.get('this_id')
    userId = request.cookies.get('user_id')
    the_user = Car.query.filter(and_(Car.Uid == userId, Car.Cid == dishId)).first()
    the_user.Num += 1
    db.session.commit()
    return redirect('/shoppingCar')


@app.route('/UserPage')
def UserPage():
    u = request.cookies.get('user_id')
    uname = request.cookies.get('user_name')
    user = User.query.filter(User.Uid == u).first()
    return render_template('UserPage.html', uname=uname, user=user)


@app.route('/LogPage')
def LogPage():
    return render_template('Login.html')


@app.route('/RegPage')
def RegPage():
    return render_template('Register.html')


@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('user_id')
    resp.delete_cookie('user_name')
    return resp


@app.route('/Login', methods=['POST', 'GET'])
def Login():
    if request.method == 'POST':
        Lus = request.form.get('Lu')
        Lpw = request.form.get('Lp')
        L_check = User.query.all()
        # # code test
        # test_result = ''
        # if not all([Lus, Lpw]):
        #     test_result = {
        #         "code": 1,
        #         "message": "invalid name or password"
        #     }
        #     return jsonify(test_result)
        # if Lus == 'a' and Lpw == 'a':
        #     resp = {
        #         "code": 2,
        #         "message": "login success"
        #     }
        # else:
        #     resp = {
        #         "code": 3,
        #         "message": "login failed"
        #     }
        # return jsonify(resp)
        if Lus == 'Admin':
            if Lpw == 'Xwya201217':
                current_app.logger.info("Admin Login")
                return redirect('/manager')
            else:
                flash("Password or username is wrong!")
                return render_template('Login.html')
        for i in L_check:
            if i.Username == Lus:
                if i.Password == Lpw:
                    current_app.logger.info("user: " + Lus + "login")
                    resp = make_response(redirect('/UserPage'))
                    resp.set_cookie('user_name', i.Username)
                    resp.set_cookie('user_id', str(i.Uid))
                    return resp
                else:
                    current_app.logger.info("User: " + Lus + "wrong password")
                    flash("Password or username is wrong!")
                    return render_template('Login.html')
        flash("Password or username is wrong!")
        return render_template('Login.html')


@app.route('/Register', methods=['POST', 'GET'])
def Register():
    if request.method == 'POST':
        us = request.form.get('Ru')
        pw = request.form.get('Rp')
        check = User.query.all()
        for i in check:
            if i.Username == us:
                flash("the Username is exist!")
                return render_template('Register.html')
        try:
            U = User(Username=us, Password=pw, Currency=0)
            db.session.add(U)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash('Error to register!')
            return render_template('Register.html')
        current_app.logger.info("user: " + us + "Successful register")
        time.sleep(1)
        return render_template('HomePage.html')


@app.route('/shoppingCar')
def shoppingCar():
    bill = 0
    us = request.cookies.get('user_id')
    print(us)
    current_app.logger.info("User(ID): " + us + "enter the shopping car")
    car_list = Car.query.filter(Car.Uid == us).all()
    for i in car_list:
        bill += (i.price*i.Num)
    print(car_list)
    return render_template('shoppingCar.html', car_list=car_list, bill=bill)


@app.route('/delete')
def delete():
    dishId = request.args.get('this_id')
    userId = request.cookies.get('user_id')
    current_app.logger.info("User(ID): " + userId + "delete the dish")
    this_dish = Car.query.filter(and_(Car.Uid == userId, Car.Cid == dishId)).first()
    db.session.delete(this_dish)
    db.session.commit()
    return redirect('/shoppingCar')


@app.route('/ShoppingPay')
def ShoppingPay():
    bill = 0
    pus = request.cookies.get('user_id')
    user = User.query.filter(User.Uid == pus).first()
    car_list = Car.query.filter(Car.Uid == pus).all()
    for i in car_list:
        bill = bill + i.price
    if user.Currency < bill:
        current_app.logger.info("User(ID): " + pus + "no currency to pay")
        flash('Your currency is not enough!')
        session['status'] = 'BAD'
        return redirect('/shoppingCar')
    if user.Currency >= bill:
        dish = Dishes.query.filter(Dishes.Cid == i.Cid)
        dish.inventory -= i.Num
        user.Currency = user.Currency - bill
        for i in car_list:
            db.session.delete(i)
        db.session.commit()
        current_app.logger.info("User(ID): " + pus + "successful pay")
        flash('Successful pay!!')
        session['status'] = 'OK'
        return redirect('/shoppingCar')


@app.route('/manager')
def manager():
    return render_template('manager.html')


@app.route('/manager/manager_user')
def manager_user():
    the_user = User.query.all()
    return render_template('manager_user.html', user_list=the_user)


@app.route('/manager/manager_user/del_user')
def del_user():
    userId = request.args.get('this_id')
    user = User.query.filter(User.Uid == userId).first()
    db.session.delete(user)
    db.session.commit()
    time.sleep(3)
    current_app.logger.info("Admin delete User(ID): " + userId)
    return redirect('/manager_user')


@app.route('/manager/manager_user/ad_cur')
def ad_cur():
    userId = request.args.get('this_id')
    user = User.query.filter(User.Uid == userId).first()
    user.Currency += 200
    db.session.commit()
    time.sleep(2)
    current_app.logger.info("Admin add User(ID): " + userId + "200 currency")
    return redirect('/manager/manager_user')


@app.route('/manager/manager_dish')
def manager_dish():
    dish_list = Dishes.query.all()
    current_app.logger.info("Admin begin to manager dish")
    return render_template('manager_dishes.html', dish_list=dish_list)


@app.route('/adj_dish')
def adj_dish():
    cid = request.args.get('this_id')
    this_dish = Dishes.query.filter(Dishes.Cid == cid).first()
    current_app.logger.info("Admin begin to adjust message of dish(ID): " + cid)
    return render_template('adjust_dish.html', dish=this_dish)


@app.route('/add_dish')
def add_dish():
    return render_template('add_dish.html')


@app.route('/del_dish')
def del_dish():
    cid = request.args.get('this_id')
    this_dish = Dishes.query.filter(Dishes.Cid == cid).first()
    db.session.delete(this_dish)
    db.session.commit()
    time.sleep(2)
    current_app.logger.info("Admin delete dish(ID): " + cid)
    return redirect('/manager/manager_dish')


@app.route('/adjust_submit', methods=['POST', 'GET'])   # this route is adjust the content in the database
def adjust_submit():
    if request.method == 'POST':
        this_id = request.form.get('fake_value')
        this_dish = Dishes.query.filter(Dishes.Cid == this_id).first()
        di = request.form.get('a_dish')
        pri = request.form.get('a_price')
        invent = request.form.get('a_invent')
        pic = request.form.get('a_pic')
        pics = "../static/picture/" + pic
        this_dish.dish = di
        this_dish.price = pri
        this_dish.inventory = invent
        this_dish.pic = pics
        db.session.commit()
        current_app.logger.info("Admin successfully adjust message of dish(ID): " + this_id)
        return redirect('/manager/manager_dish')


@app.route('/add_submit', methods=['POST', 'GET'])   # this route is adjust the content in the database
def add_submit():
    if request.method == 'POST':
        di = request.form.get('a_dish')
        pri = request.form.get('a_price')
        invent = request.form.get('a_invent')
        pic = request.form.get('a_pic')
        pics = "../static/picture/" + pic
        this_dish = Dishes(dish=di, price=pri, inventory=invent, pic=pics)
        db.session.add(this_dish)
        db.session.commit()
        current_app.logger.info("Admin successfully add one dish")
        return redirect('/manager/manager_dish')


@app.route('/se', methods=['POST', 'GET'])
def se():
    if request.method == 'POST':
        b = request.form.get('se')
        if b is None:
            return redirect("/Menu")
        dish = Dishes.query.filter(Dishes.dish.like("%" + b + "%")).all()
        return render_template("search_res.html", menu_list=dish)


@app.route('/changeMessage')
def changeMessage():
    uid = request.cookies.get('user_id')
    us = User.query.filter(User.Uid == uid).first()
    return render_template('c_message.html', user=us)


@app.route('/adjust_message', methods=['POST', 'GET'])
def adjust_message():
    if request.method == 'POST':
        un = request.form.get('m_un')
        pw = request.form.get('m_pw')
        uid = request.cookies.get('user_id')
        us = User.query.filter(User.Uid == uid).first()
        us.Username = un
        us.Password = pw
        db.session.commit()
        current_app.logger.info("User(ID): " + uid + "change password")
        return redirect('/UserPage')