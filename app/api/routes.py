from flask import jsonify, request
from app.api import bp
from app.database.models import Design

design_db = Design()

@bp.route('/design/generate', methods=['POST'])
def generate_design():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    # ここにPhotoshop APIとの連携コードを実装
    # 仮の実装として、ダミーURLを返す
    image_url = "https://example.com/dummy-image.png"
    
    design_id = design_db.create_design(prompt, image_url)
    
    return jsonify({
        'design_id': design_id,
        'image_url': image_url
    })

@bp.route('/design/update', methods=['POST'])
def update_design():
    data = request.get_json()
    design_id = data.get('design_id')
    feedback = data.get('feedback')
    
    if not all([design_id, feedback]):
        return jsonify({'error': 'Design ID and feedback are required'}), 400
    
    # ここにPhotoshop APIとの連携コードを実装
    # 仮の実装として、ダミーURLを返す
    image_url = "https://example.com/updated-image.png"
    
    return jsonify({
        'image_url': image_url
    })

@bp.route('/design/preview', methods=['GET'])
def get_preview():
    design_id = request.args.get('design_id')
    
    if not design_id:
        return jsonify({'error': 'Design ID is required'}), 400
    
    design = design_db.get_design(int(design_id))
    
    if not design:
        return jsonify({'error': 'Design not found'}), 404
    
    return jsonify({
        'image_url': design[2]  # design[2]はimage_urlのカラム
    })