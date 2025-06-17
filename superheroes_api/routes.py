from flask import Blueprint, request, jsonify
from .models import db, Hero, Power, HeroPower

# Blueprint for the API routes
api = Blueprint('api', __name__)

@api.route('/')
def home():
    return "YOOO this is the superhero API "

@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {'id': h.id, 'name': h.name, 'super_name': h.super_name}
        for h in heroes
    ]), 200

@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found '}), 404

    return jsonify({
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'powers': [{
            'id': hp.power.id,
            'name': hp.power.name,
            'description': hp.power.description
        } for hp in hero.hero_powers]
    }), 200

@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([
        {'id': p.id, 'name': p.name, 'description': p.description}
        for p in powers
    ]), 200

@api.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found '}), 404

    return jsonify({
        'id': power.id,
        'name': power.name,
        'description': power.description
    }), 200

@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    try:
        data = request.get_json()
        if 'description' in data:
            power.description = data['description']
            db.session.commit()
            return jsonify({
                'id': power.id,
                'name': power.name,
                'description': power.description
            }), 200
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400

@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    try:
        data = request.get_json()
        new_hp = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hp)
        db.session.commit()

        hero = Hero.query.get(data['hero_id'])

        return jsonify({
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{
                'id': hp.power.id,
                'name': hp.power.name,
                'description': hp.power.description
            } for hp in hero.hero_powers]
        }), 201

    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400
