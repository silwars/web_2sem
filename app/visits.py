from datetime import timedelta
from flask import Blueprint, render_template, request, send_file, flash
from flask_login import login_required, current_user
from auth import check_rights
from models import Visits, Book, Covers, Genrys_books, User
from sqlalchemy import distinct, func, desc
import io
import datetime

bp = Blueprint('visits', __name__, url_prefix='/visits')
PER_PAGE = 6

def convert_to_csv(fields, records):
    result = 'No,' + ','.join(fields)+ '\n'
    for i, record in enumerate(records):
        result += f'{i+1},' + ','.join([str(record.get(f)) for f in fields]) + '\n'
    return result

def generate_report(fields, records):
    buffer = io.BytesIO()
    buffer.write(convert_to_csv(fields, records).encode(encoding='utf-8'))
    buffer.seek(0)
    return buffer

@bp.route('/popular_book')
def popular_book():
    dict_book = {}
    visits = Visits.query.filter(Visits.path.ilike("%show")).filter(Visits.created_at >= datetime.date.today() - timedelta(days = 90)).all()
    for visit in visits:
        book_id = visit.path.split('/')[2]
        if book_id in dict_book:
            dict_book[book_id] +=1
        else:
            dict_book[book_id] = 1
    dict_book_id = sorted(dict_book, key=dict_book.get)
    dict_book_id = dict_book_id[::-1]
    books = []
    for id in dict_book_id:
        if Book.query.get(id) is not None and len(books)<5:
            books.append(Book.query.get(id))
    book_genry = Genrys_books.query.all()
    flag = False

    if current_user.is_anonymous:
        flag = Visits.query.filter(Visits.user_id == None).filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc()).all()

    return render_template('visits/popular_book.html',books = books, book_genry = book_genry, flag = flag)


@bp.route('/last_book')
def last_book():
    dict_book = {}
    if current_user.is_authenticated:
        visits = Visits.query.filter(Visits.user_id.ilike(current_user.id)).filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc()).all()
    else:
        visits = Visits.query.filter(Visits.user_id == None).filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc()).all()
    for visit in visits:
        book_id = visit.path.split('/')[2]
        if book_id in dict_book:
            dict_book[book_id] +=1
        else:
            dict_book[book_id] = 1
    books = []
    for id in dict_book:
        if Book.query.get(id) is not None and len(books)<5:
            books.append(Book.query.get(id))
    book_genry = Genrys_books.query.all()
    flag = False
    if current_user.is_anonymous:
        flag = Visits.query.filter(Visits.user_id == None).filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc()).all()
    return render_template('visits/last_book.html',books = books, book_genry = book_genry, flag = flag)


@bp.route('/stats/users', methods=['GET','POST'])
@check_rights('view_logs')
@login_required
def stat_users():

    page = request.args.get('page', 1, type=int)
    visits = Visits.query.filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc())
    pagination = visits.paginate(page, PER_PAGE)

    visits = pagination.items
    for visit in visits:
        book = Book.query.get(visit.path.split('/')[2])
        visits[visits.index(visit)] = (visit.user, book.name_book, visit.created_at)
    if request.args.get('download_csv'):
        visits = Visits.query.filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc()).all()

        records = []
        for i in visits:
            book = Book.query.get(i.path.split('/')[2])
            if i.user:
                records.append({
                    'User': i.user.last_name + ' ' + i.user.first_name + ' ' + (i.user.middle_name or ''), 
                    'Book': book.name_book, 
                    'Date': i.created_at.strftime("%Y-%m-%d %H:%M:%S")})
            else:
                records.append({
                    'User': "Неавторизированный пользователь", 
                    'Book': book.name_book, 
                    'Date': i.created_at.strftime("%Y-%m-%d %H:%M:%S")})

        f = generate_report(['User', 'Book', 'Date'], records)
        filename = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S') + 'pages_stat.csv'
        return send_file(f, mimetype='text/csv', as_attachment=True, attachment_filename=filename)


    return render_template('visits/users_stat.html', visits=visits, pagination=pagination)



@bp.route('/stats/books_stat', methods=['GET','POST'])
@check_rights('view_logs')
@login_required
def stat_books():
    page = request.args.get('page', 1, type=int)

    fromdate = request.form.get('trip-start')
    todate = request.form.get('trip-end')
    if fromdate is None or fromdate == '':
        fromdate = datetime.datetime.today() - timedelta(days = 90)
    else:
        fromdate = datetime.datetime.strptime(fromdate, "%Y-%m-%d") + timedelta(hours=0, minutes=0, seconds=0)
    if todate is None or todate == '':
        todate = datetime.datetime.today()
    else:
        todate = datetime.datetime.strptime(todate, "%Y-%m-%d") + timedelta(hours=23, minutes=59, seconds=59)
    visits = Visits.query.with_entities(Visits.path, func.count(Visits.path).label("total")).filter(todate >= Visits.created_at).filter(Visits.created_at >= fromdate).filter(Visits.path.ilike("%show")).filter(Visits.user_id != None).group_by(Visits.path).order_by(desc('total'))
    pagination = visits.paginate(page, PER_PAGE)
    visits = visits.all()
    visits = pagination.items
    for visit in visits:
        temp = {}
        book = Book.query.get(visit[0].split('/')[2])
        temp[book.name_book] = visit[1]
        visits[visits.index(visit)] = temp
    if request.args.get('download_csv'):
        records = []
        visits = Visits.query.with_entities(Visits.path, func.count(Visits.path).label("total")).filter(todate >= Visits.created_at).filter(Visits.created_at >= fromdate).filter(Visits.path.ilike("%show")).filter(Visits.user_id != None).group_by(Visits.path).order_by(desc('total')).all()
        for i in visits:
            book = Book.query.get(i.path.split('/')[2])
            records.append({ 
                'Book': book.name_book, 
                'Views': i[1]}) 
        
        f = generate_report(['Book', 'Views'] , records)
        filename = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S') + 'pages_stat.csv'
        return send_file(f, mimetype='text/csv', as_attachment=True, attachment_filename=filename)
        


    return render_template('visits/books_stat.html', pagination=pagination, visits=visits, fromdate=fromdate, todate=todate )

    


