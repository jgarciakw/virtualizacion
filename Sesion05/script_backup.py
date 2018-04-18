import commands
import time
import json

def recolectorDatos():
    vms = []

    maquinas = commands.getoutput("xe vm-list tags=BACKUP | awk '/uuid/{print substr($0,24)}/name-label/{print substr($0,24)}/power-state/{print substr($0,24)}'").split('\n')

    for i in range(0, len(maquinas), 3):
        dic = {}
        dic['uuid'] = maquinas[i]
        dic['name-label'] = maquinas[i+1]
        dic['power-state'] = maquinas[i+2]

        interfaces = commands.getoutput("xe vm-vif-list vm={}".format(maquinas[i+1])+" | awk '/MAC/{print substr($0,31)}/device/{print substr($0,31)}'").split('\n')

        for i in range(0, len(interfaces), 2):
            dic['MAC'+interfaces[i]] = interfaces[i+1]

        vms.append(dic)

    return vms


vms = recolectorDatos()

for m in vms:
    print(m['name-label'])
    date = time.strftime("%d-%m-%Y-%H:%M",time.localtime())
    if m['power-state'] == 'running':
        cmd = 'xe vm-snapshot vm={} new-name-label={}'.format(m['name-label'], m['name-label'])
        snapshotUuid = commands.getoutput(cmd)
        print('snapshot ready...')

        cmd = 'xe template-param-set is-a-template=false uuid={}'.format(snapshotUuid)
        commands.getoutput(cmd)

        path = '/var/run/sr-mount/58fc9d3f-f3a5-28d7-de60-c085aebad1a1/rbpj/' + m['name-label'] + date + '.xva'
        cmd = 'xe vm-export uuid={} filename={} preserve-power-state=true'.format(snapshotUuid, path)
        commands.getoutput(cmd)
        print('export ready...')

        cmd = 'xe vm-uninstall uuid={} force=true'.format(snapshotUuid)
        commands.getoutput(cmd)

    else:
        path = '/var/run/sr-mount/58fc9d3f-f3a5-28d7-de60-c085aebad1a1/rbpj/' + m['name-label'] + date + '.xva'
        cmd = 'xe vm-export vm={} filename={} preserve-power-state=true'.format(m['name-label'], path)
        commands.getoutput(cmd)
        print('export ready...')

    with open('/var/run/sr-mount/58fc9d3f-f3a5-28d7-de60-c085aebad1a1/rbpj/' + m['name-label'] + date + '.json', 'w') as f:
        f.write(json.dumps(m))

    print('json ready...')
