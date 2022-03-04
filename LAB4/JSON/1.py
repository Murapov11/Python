import json
with open('sample-data.txt', 'r') as f:
    x = json.loads(f.read())

print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU')
print('-------------------------------------------------- --------------------  ------  ------')

for j in x['imdata']:
    dn = j['l1PhysIf']['attributes']['dn']
    description = j['l1PhysIf']['attributes']['descr']
    speed = j['l1PhysIf']['attributes']['speed']
    mtu = j['l1PhysIf']['attributes']['mtu']
    print(f'{dn}    {description}{speed}   {mtu}')