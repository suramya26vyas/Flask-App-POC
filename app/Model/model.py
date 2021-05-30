from app.utilities import LibraryUtilities

db = LibraryUtilities.return_db_instance()


class Students(db.Model):
    """
    The information about class in Declarative system, is called as table metadata.
    SQLAlchemy uses Table object to represent this information for a specific table created by Declarative i.e. Base Object.
    The Table object is created according to the specifications,
    and is associated with the class by constructing a Mapper object.
    This mapper object is not directly used but is used internally as interface between mapped class and table.
    """

    __tablename__ = 'Students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)


class StudentsData(db.Model):
    """
    The information about class in Declarative system, is called as table metadata.
    SQLAlchemy uses Table object to represent this information for a specific table created by Declarative i.e. Base Object.
    The Table object is created according to the specifications,
    and is associated with the class by constructing a Mapper object.
    This mapper object is not directly used but is used internally as interface between mapped class and table.
    """

    __tablename__ = 'StudentsData'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, db.ForeignKey(
        "StudentCredentials.email"))
    PhoneNumber = db.Column(db.String)
    EmailIDRel = db.relationship(
        "StudentCredentials", foreign_keys="StudentsData.email")


class StudentCredentials(db.Model):
    """
    The information about class in Declarative system, is called as table metadata.
    SQLAlchemy uses Table object to represent this information for a specific table created by Declarative i.e. Base Object.
    The Table object is created according to the specifications,
    and is associated with the class by constructing a Mapper object.
    This mapper object is not directly used but is used internally as interface between mapped class and table.
    """

    __tablename__ = 'StudentCredentials'
    email = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
