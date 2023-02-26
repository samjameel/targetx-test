from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    messages_sent = db.relationship('Message', backref='sender', lazy=True, foreign_keys='Message.sender_id')
    messages_received = db.relationship('Message', backref='receiver', lazy=True, foreign_keys='Message.receiver_id')


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message_text = db.Column(db.String(160), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=False)

@app.route('/api/send-sms', methods=['POST'])
def send_sms():
    data = request.get_json()

    sender_phone = data['senderPhone']
    receiver_phone = data['receiverPhone']
    message_text = data['messageText']
    timestamp = data['timestamp']
    uuid = data['uuid']

    sender = User.query.filter_by(phone_number=sender_phone).first()
    receiver = User.query.filter_by(phone_number=receiver_phone).first()

    if not sender:
        sender = User(phone_number=sender_phone)
        db.session.add(sender)

    if not receiver:
        receiver = User(phone_number=receiver_phone)
        db.session.add(receiver)

    message = Message(sender=sender, receiver=receiver, message_text=message_text, timestamp=timestamp, uuid=uuid)
    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'SMS sent successfully'})

@app.route('/api/receive-sms', methods=['POST'])
def receive_sms():
    data = request.get_json()

    sender_phone = data['senderPhone']
    receiver_phone = data['receiverPhone']
    message_text = data['messageText']
    timestamp = data['timestamp']
    uuid = data['uuid']

    sender = User.query.filter_by(phone_number=sender_phone).first()
    receiver = User.query.filter_by(phone_number=receiver_phone).first()

    if not sender:
        sender = User(phone_number=sender_phone)
        db.session.add(sender)

    if not receiver:
        receiver = User(phone_number=receiver_phone)
        db.session.add(receiver)

    message = Message(sender=sender, receiver=receiver, message_text=message_text, timestamp=timestamp, uuid=uuid)
    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'SMS received successfully'})


@app.route('/api/get-conversation/<phone_number>', methods=['GET'])
def get_conversation(phone_number):
    user = User.query.filter_by(phone_number=phone_number).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    messages_sent = user.messages_sent
    messages_received = user.messages_received

    messages = []
    for message in messages_sent:
        messages.append({
            'phone_number': message.receiver.phone_number,
            'message_text': message.message_text,
            'timestamp': message.timestamp,
            'direction': 'sent'
        })

    for message in messages_received:
        messages.append({
            'phone_number': message.sender.phone_number,
            'message_text': message.message_text,
            'timestamp': message.timestamp,
            'direction': 'received'
        })

    messages = sorted(messages, key=lambda x: x['timestamp'])
    
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')