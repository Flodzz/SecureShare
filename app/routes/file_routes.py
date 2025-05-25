from flask import Blueprint, render_template

file_bp = Blueprint('file', __name__)


@file_bp.route('/upload')
def upload():
    return render_template('upload.html')
