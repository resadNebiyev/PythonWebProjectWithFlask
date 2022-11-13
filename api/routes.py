from api import api_bp
from flask import render_template,jsonify
@api_bp.route("/", methods=['GET','POST'])
def index():
    from model import Category,CategoryItems
    category  = Category.query.all()
    categoryitems = CategoryItems.query.all()
    return render_template('index.html')

@api_bp.route("/categories", methods=['GET','POST'])
def api_categories():
    from model import CategorySchema,Category
    category_schema = CategorySchema(many = True)
    categories = Category.query.all()
    output = category_schema.dump(categories)
    return jsonify(output)

@api_bp.route("/subcategories", methods=['GET','POST'])
def api_subcategories():
    from model import CategorySchema,CategoryItems,CategoryItemsSchema
    subcategory_schema = CategoryItemsSchema(many = True)
    subcategories = CategoryItems.query.all()
    output = subcategory_schema.dump(subcategories)
    return jsonify(output)