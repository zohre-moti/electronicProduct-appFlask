from app import db

#محصولات
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.BigInteger, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}','{self.description}, '{self.price}', '{self.quantity}')"
    

#کلاس نظرات کاربران
class UserComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"UserComment( '{self.product_id}','{self.comment}', '{self.rating}')"
 

    



