import commands
import json

nfs = '/var/run/sr-mount/58fc9d3f-f3a5-28d7-de60-c085aebad1a1/rbpj/'

output = commands.getoutput('ls -l {}/*.json'.format(nfs))

lines = output.split('\n')

vms = []
for l in lines:
    name = l.split(' ')[-1]

    with open(name, 'r') as f:

        dic = json.load(f)
        dic['export'] = name.split('/')[-1].split('.')[0] + '.xva'

    vms.append(dic)


for m in vms:
    print(m['name-label'])

    vmUuid = commands.getoutput('xe vm-import vm={} filename={} preserve=true'.format(m['name-label'], nfs + m['export']))
    print('import ready...')

    output = commands.getoutput('xe vm-start uuid={}'.format(vmUuid))
    print(output)