import db

class patients():
    id=''
    fName=''
    mName=''
    lName=''
    cPhone=''
    hPhone=''
    wPhone=''
    email=''
    adr1=''
    adr2=''
    city=''
    state=''
    zc=''
    ssn=''
    dob=''
    usrnm=''
    pw=''

    def __init__(self,id,fName,mName,lName,cPhone,hPhone,wPhone,email,adr1,adr2,city,state,zc,ssn,dob,usrnm,pw):
        self.id=id
        self.fName=fName
        self.mName=mName
        self.lName=lName
        self.cPhone=cPhone
        self.hPhone=hPhone
        self.wPhone=wPhone
        self.email=email
        self.adr1=adr1
        self.adr2=adr2
        self.city=city
        self.state=state
        self.zc=zc
        self.ssn=ssn
        self.dob=dob
        self.usrnm=usrnm
        self.pw=pw

    @classmethod
    def load(cls,id):
        sql="SELECT * FROM patients WHERE id=?;"
        obj=db.select(sql,[id])
        if obj:
            if len(obj)>0:
                return cls( obj[0]["id"],
                            obj[0]["fName"],
                            obj[0]["mName"],
                            obj[0]["lName"],
                            obj[0]["cPhone"],
                            obj[0]["hPhone"],
                            obj[0]["wPhone"],
                            obj[0]["email"],
                            obj[0]["adr1"],
                            obj[0]["adr2"],
                            obj[0]["city"],
                            obj[0]["state"],
                            obj[0]["zc"],
                            obj[0]["ssn"],
                            obj[0]["dob"],
                            obj[0]["usrnm"],
                            obj[0]["pw"])
        return None

    def insert(self):
        sql="INSERT INTO patients(fName,mName,lName,cPhone,hPhone,wPhone,email,adr1,adr2,city,state,zc,ssn,dob,usrnm,pw) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
        affected=db.executeSentence(sql,[self.fName,self.mName,self.lName,self.cPhone,self.hPhone,self.wPhone,self.email,self.adr1,self.adr2,self.city,self.state,self.zc,self.ssn,self.dob,self.usrnm,self.pw])
        return(affected>0)

    @staticmethod
    def lastRow():
        sql="SELECT * FROM patients ORDER BY id;"
        return len(db.select(sql,None))