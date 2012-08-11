import models

def migrate_bills():
    session = models.DBSession()
    bills = session.query(models.Bill).all()
    en = session.query(models.Language).get(name='en')
    for bill in bills:
        translate = models.BillTranslation(
                lang_id=en.id,
                name = bill.name,
                bill_id=bill.id
            )
        session.add(translate)
        session.flush()

def migrate_revisions():
    session = models.DBSession()
    en = session.query(models.Language).get(name='en')
    revs = session.query(models.BillRevision).all()
    for rev in revs:
        translate = models.BillRevisionTranslation(
                lang_id=en.id,
                name=rev.bill.name
                rev_id=rev.id
            )
        session.add(translate)
        session.flush()

def add_language():
    session = models.DBSession()
    language = models.Language(name='en')
    session.add(language)
    session.flush() 

def run():
    models.initdb()
    add_language()
    migrate_bills()
    migrate_revisions() 
    
if __name__ == "__main__":
    run()
