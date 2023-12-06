# Functions
def NoEdge(HP, AP, APThreshold, enemy):
    shots = 0
    APMult = APen - APThreshold
    if APMult < 0:
        APMult = 0
    #print("")
    while HP > 0:
        while AP > 0:
            shots += 1
            AP -= Damage
            HP -= APMult * Damage * CritMult
            #print('Shot {}. AP: {}. HP: {}'.format(shots,AP,HP))
            if HP <= 0:
                AP = 0
        if HP > 0:
            shots += 1
            HP -= Damage * CritMult
            #print ('Shot {}. HP: {}'.format(shots,HP))
    print ("{} killed without Edge in {} shots.".format(enemy,shots))

def Edge(HP, AP, APThreshold, enemy):
    shots = 0
    APMult = APen - APThreshold
    if APMult < 0:
        APMult = 0
    #print("")
    while HP > 0:
        while AP > 0:
            shots += 1
            AP -= Damage * 1.1
            HP -= APMult * Damage * 1.1 * CritMult
            #print('Shot {}. AP: {}. HP: {}'.format(shots,AP,HP))
            if HP <= 0:
                AP = 0
        if HP > 0:
            shots += 1
            HP -= Damage * 1.1 * CritMult
            #print ('Shot {}. HP: {}'.format(shots,HP))
    print ("{} killed with Edge in {} shots.".format(enemy,shots))

def CuttingShot(HP, AP, APThreshold, enemy):
    shots = 0
    APMult = APen - APThreshold + 0.1
    if APMult < 0:
        APMult = 0
    #print("")
    while HP > 0:
        while AP > 0:
            shots += 1
            AP -= Damage * 1.1
            HP -= APMult * Damage * 1.1 * CritMult
            #print('Shot {}. AP: {}. HP: {}'.format(shots,AP,HP))
            if HP <= 0:
                AP = 0
        if HP > 0:
            shots += 1
            HP -= Damage * 1.1 * CritMult
            #print ('Shot {}. HP: {}'.format(shots,HP))
    print ("{} killed with Cutting Shot in {} shots.".format(enemy,shots))

while True:
    print("-----------------------------------------")
    # User Input
    Damage = float(input('Weapon damage: '))
    CritMult = float(input('Crit multiplier: '))
    APen = float(input('AP Value: '))
    print("")

    # Light SWAT
    NoEdge(150,70,0.5,"Light SWAT")
    Edge(150,70,0.5,"Light SWAT")
    CuttingShot(150,70,0.5,"Light SWAT")
    print("")

    # Heavy SWAT
    NoEdge(150,170,0.5,"Heavy SWAT")
    Edge(150,170,0.5,"Heavy SWAT")
    CuttingShot(150,170,0.5,"Heavy SWAT")
    print("")

    # Taser
    NoEdge(150,140,0.5,"Taser")
    Edge(150,140,0.5,"Taser")
    CuttingShot(150,140,0.5,"Taser")
    print("")

    # Nader

    print("")

    # Cloaker
    NoEdge(150,0,0,"Cloaker")
    Edge(150,0,0,"Cloaker")
    CuttingShot(150,0,0,"Cloaker")
    print("")

    # Shield
    NoEdge(160,180,1.0,"Shield")
    Edge(160,180,1.0,"Shield")
    CuttingShot(160,180,1.0,"Shield")
    print("")
