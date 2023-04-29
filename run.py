from app import myapp_obj, db
myapp_obj.run(debug=True)

with myapp_obj.app_context():
    db.create_all()