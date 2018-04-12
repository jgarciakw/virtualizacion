import commands

vms = []

maquinas = commands.getoutput('xe vm-list tags=BACKUP params=uuid,name-label').strip('\n').split('\n\n\n')

for m in maquinas:
    params = m.split('\n')

    dic = {}

    for p in params:

        elem = p.strip(' ').split(' ')

        dic[elem[0]] = elem[-1]


    vms.append(dic)

#En este punto, vms es una lista de diccionarios, y cada diccionario esta formado por {name-label:---, uuid:---}
#for machine in vms:
#    print(machine)


for dic in vms:

    interfaces = commands.getoutput('xe vm-vif-list vm={} params=MAC,device'.format(dic['name-label'])).strip('\n').split('\n\n\n')

    for i in interfaces:
        params = i.split('\n')

        device = params[0].strip(' ').split(' ')
        mac = params[1].strip(' ').split(' ')

        key = mac[0] + device[-1]
        value = mac[-1]

        dic[key] = value


#En este punto, vms es una lista de diccionarios, y cada diccionario esta formado por {name-label:---, uuid:---, MAC1:---, MAC0:---}
#for machine in vms:
#    print(machine)
