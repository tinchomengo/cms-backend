from flask import Blueprint, request, jsonify
from app.services.admin_service import create_admin

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/create', methods=['POST'])
def create_admin_route():
    data = request.get_json()
    admin = create_admin(data['email'], data['password'], data['role'])
    return jsonify({"id": admin.id, "email": admin.email, "role": admin.role})
