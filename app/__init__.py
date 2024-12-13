from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db= SQLAlchemy()
migrate= Migrate()

DB_USER= "root"
DB_PASSWORD="Bestisabully3$"
DB_HOST="localhost"
DB_NAME="student_course_group"

def create_app():
    app=Flask(__name__)
    app.secret_key="Asher"

    @app.route('/')
    def index():
        return render_template('index.html')
    
  

    DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
     
    db.init_app(app)
    migrate.init_app(app, db)
    


    from app.faculty.models import faculty
    from app.department.models import department
    from app.program.models import program
    from app.course.models import course
    from app.group.models import group
    from app.level.models import level
    from app.student.models import student
    from app.assign_student.models import assign_student

    from app.faculty import faculty_bp
    app.register_blueprint(faculty_bp)

    from app.department import department_bp
    app.register_blueprint(department_bp)

    from app.group import group_bp
    app.register_blueprint(group_bp)

    from app.level import level_bp
    app.register_blueprint(level_bp)

    from app.program import program_bp
    app.register_blueprint(program_bp)

    from app.student import student_bp
    app.register_blueprint(student_bp)

    from app.course import course_bp
    app.register_blueprint(course_bp)

    from app.assign_student import assign_student_bp
    app.register_blueprint(assign_student_bp)

    with app.app_context():
        db.create_all()




    return app
    