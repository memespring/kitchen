from flask_script import Manager, prompt_bool
from app import app, db

manager = Manager(app)

@manager.command
def importdata():
    "Import all the things"

    with app.test_request_context():
        table = db['data']
        table.upsert(dict(key="1", message='sausages,chips,beans'), ['key'])
        table.upsert(dict(key="2", message='greens,carrots,sprouts'), ['key'])
   

if __name__ == "__main__":
    manager.run()