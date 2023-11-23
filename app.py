from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 遊戲數據，這裡只是一個簡單的例子
game_data = {
    'players': [],
    'quests': [],
    'game_rooms': {},  # 每個房間的玩家列表
    'max_players_per_room': 10,
}

@app.route('/')
def index():
    return render_template('index.html', players=game_data['players'])

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form.get('player_name')
    game_data['players'].append(player_name)
    return redirect(url_for('lobby'))

@app.route('/lobby')
def lobby():
    return render_template('lobby.html', players=game_data['players'], game_rooms=game_data['game_rooms'])

@app.route('/create_room', methods=['POST'])
def create_room():
    room_name = request.form.get('room_name')
    
    if room_name not in game_data['game_rooms']:
        game_data['game_rooms'][room_name] = []
        
    return redirect(url_for('lobby'))

@app.route('/join_room/<room_name>')
def join_room(room_name):
    # 你的處理邏輯
    return render_template('room.html', room_name=room_name)

@app.route('/reset')
def reset():
    game_data['players'] = []
    game_data['game_rooms'] = {}
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)