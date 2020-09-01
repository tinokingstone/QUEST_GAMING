from shop import db
from datetime import datetime


class Addproduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    T_Title = db.Column(db.String(80), nullable=False)
    gamename = db.Column(db.String(80), nullable=False)
    Game_Mode = db.Column(db.String(80), nullable=False)
    Tournament_Type = db.Column(db.String(80), nullable=False)
    Tournament_Title = db.Column(db.String(80), nullable=False)

    Prize_Pot = db.Column(db.Numeric(10,2), nullable=False)
    Entery_Cost = db.Column(db.Numeric(10,2), nullable=False)
    Maximum_Participants = db.Column(db.Numeric(10), nullable=False)
    Minimum_Participants = db.Column(db.Numeric(10), nullable=False)
    Enroled_Participants = db.Column(db.Numeric(10), nullable=False)

    Platform = db.Column(db.String(80), nullable=False)
    Starting_Date = db.Column(db.String(80), nullable=False)
    Tournament_Time = db.Column(db.String(80), nullable=False)
    Game_Settings = db.Column(db.String(80), nullable=False)
    Rule_Group = db.Column(db.String(80), nullable=False)
    Number_Of_Rounds = db.Column(db.String(80), nullable=False)
    Region = db.Column(db.String(80), nullable=False)

    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    descrip = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=True, default='image3.jpg')

    def __repr__(self):
        return '<Post %r>' % self.name


class fortnitesolo(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return '<fortnitesolo %r>' % self.name



class fortnitesquads(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return '<fortnitesquads %r>' % self.name

class fortnitesolops5(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<fortnitesolops5 %r>' % self.name


class fortnitesoloxbox(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)
             
    opponent = db.Column(db.String(80), nullable=False)

    opponent_gamertag = db.Column(db.String(80), nullable=False)
    player1_video = db.Column(db.String(80), nullable=False)
    player2_video = db.Column(db.String(80), nullable=False)
    player1_time = db.Column(db.String(80), nullable=False)
    player2_time = db.Column(db.String(80), nullable=False)
    game_key = db.Column(db.String(80), nullable=False)

    winner = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<fortnitesquads %r>' % self.name

class fifaduo(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<fortnitesquads %r>' % self.name

class fifasolo(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return '<fortnitesquads %r>' % self.name

class codsolo(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<fortnitesquads %r>' % self.name

class codsquads(db.Model):
    __seachbale__ = ['name','desc','Gamertag_PC']
    id = db.Column(db.Integer, primary_key=True)
    Participant_User_Id = db.Column(db.String(80), nullable=False)
    Participant_State = db.Column(db.String(80), nullable=False)
    Gamertag_PC = db.Column(db.String(80), nullable=False)
    Gamertag_XBOX = db.Column(db.String(80), nullable=False)

    Gamertag_PS4 = db.Column(db.String(80), nullable=False)
    Team_member_1 = db.Column(db.String(80), nullable=False)
    Team_member_2 = db.Column(db.String(80), nullable=False)
    Team_member_3 = db.Column(db.String(80), nullable=False)

    opponent = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return '<fortnitesquads %r>' % self.name


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Brand %r>' % self.name

class brand2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Brand %r>' % self.name
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name

db.create_all()