import requests

print('\nBattle.net PvP Stats by Juicebox.\n')

while True:        
    valid = False
    while valid == False:
        print('[1] Show data for 2v2')
        print('[2] Show data for 3v3')
        print('[3] Show data for 5v5')
        print('[4] Show data for rbg')
        print('[5] Exit\n')
        
        bracket = input('Enter selection: ')
        
        if bracket == '1':
            bracket = '2v2'
            break
        elif bracket == '2':
            bracket = '3v3'
            break
        elif bracket == '3':
            bracket = '5v5'
            break    
        elif bracket == '4':
            bracket = 'rbg'
            break
        elif bracket == '5':
            raise SystemExit
            break
        else:
            print('Invalid item.\n')    
    
    print('Loading %s stats...\n' % bracket)    
    
    try:
        request = requests.get('http://us.battle.net/api/wow/leaderboard/%s' % bracket)
    except:
        print('Unable to connect to Battle.net armory.  Please try again later.\n')
        continue
    
    data = request.json()
    data = data['rows']
    
    faction = {
       'horde': 0,
       'alliance': 0
    }
    
    cl = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    
    classNames = {
        1: 'Warriors',
        2: 'Paladins',
        3: 'Hunters',
        4: 'Rogues',
        5: 'Priests',
        6: 'Death Knights',
        7: 'Shaman',
        8: 'Mages',
        9: 'Warlocks',
        10: 'Monks',
        11: 'Druids'
    }
    
    for item in data:
        if item['factionId'] == 0:
            faction['alliance'] += 1
        else:
            faction['horde'] += 1
            
        cl[item['classId']-1] += 1
    
    print('===================================')
    print('Alliance: %s, Horde: %s' % (faction['alliance'], faction['horde']))
    
    for (k, v) in enumerate(cl):
        print('%d are %s' % (v, classNames[k+1]))
    print('===================================\n')