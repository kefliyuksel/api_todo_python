from . import db

class TodoModel(db.Model):
  """
  Todo Model
  """

  # table name
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(128))

  # class constructor
  def __init__(self, **data):
    """
    Class constructor
    """
    self.title = data.get('title')
    self.description = data.get('description')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, **data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_todos():
    return TodoModel.query.all()

  @staticmethod
  def get_one_todo(id):
    return TodoModel.query.get(id)

  
  def __repr(self):
    return '<id {}>'.format(self.id)
