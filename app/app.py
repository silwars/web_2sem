import datetime
from flask import Flask, render_template, abort, send_from_directory, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')
PER_PAGE = 6

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
from auth import bp as auth_bp, init_login_manager

from models import Book, Covers, Genry, Recives, Visits, Genrys_books
init_login_manager(app)


from books import book_bp
from visits import bp as visits_bp
app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.register_blueprint(visits_bp)


@app.before_request
def log_visit_info():
    if request.endpoint == 'static' or request.args.get('download_csv'):
        return None
    
    user_id = getattr(current_user, 'id', None)
    visit = Visits()
    visit.user_id = user_id
    visit.path = request.path
    if '/images' not in visit.path and visits_count(visit.path, user_id):
        try:
            db.session.add(visit)
            db.session.commit()
        except:
            db.session.rollback()

def visits_count(path, user_id):
    if 'show' in  path:
        date = Visits.query.filter(Visits.created_at.ilike(f"%{datetime.datetime.now().strftime('%Y-%m-%d')}%")).filter(Visits.path == path).filter(Visits.user_id == user_id).all()
        if len(date) > 10:
            return False
    return True


@app.route('/')
def index():
    flag = False
    page = request.args.get('page', 1, type=int)


    books = Book.query.order_by(Book.year.desc())
    pagination = books.paginate(page, PER_PAGE)
    books = pagination.items
    book_genry = Genrys_books.query.all()

    if current_user.is_anonymous:
        flag = Visits.query.filter(Visits.user_id == None).filter(Visits.path.ilike("%show")).order_by(Visits.created_at.desc()).all()
    return render_template('index.html', 
                            books=books, 
                            book_genry=book_genry,
                            pagination=pagination, flag=flag
                            )

@app.route('/images/<image_id>')
def image(image_id):
    img = Covers.query.get(image_id)
    if img is None:
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               img.storage_filename)


