from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary in-memory list to log host lead submissions
kiosk_leads = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/request-kiosk', methods=['POST'])
def request_kiosk():
    data = request.get_json()
    
    # Validate payload input
    if not data or not data.get('email') or not data.get('organization'):
        return jsonify({'success': False, 'message': 'Organization and email are required.'}), 400
    
    # Store lead in-memory and print to server console
    kiosk_leads.append(data)
    print(f"\n[NEW KIOSK LEAD RECEIVED] Organization: {data.get('organization')} | Traffic: {data.get('traffic')} | Email: {data.get('email')}\n")
    
    return jsonify({
        'success': True, 
        'message': 'Host request submitted successfully! Our expansion team will contact you within 24 hours.'
    })

if __name__ == '__main__':
    app.run(debug=True)