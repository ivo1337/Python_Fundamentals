keyMaterials = { "shards": 0, "fragments": 0, "motes": 0 }
junkMaterials = {}
obtainedItem = False
while not obtainedItem:
receivedInput = input().split()

# Looping through the input received to process the items
for i in range(0, len(receivedInput), 2):

    # Extracting the quantity and material from the input received
    quantity = int(receivedInput[i])
    material = receivedInput[i + 1]

    # Checking if the material is a key material or junk
    if material in keyMaterials:

        # Adding the quantity to the respective key material
        keyMaterials[material] += quantity

        # Checking if the key material quantity reached 250
        if keyMaterials[material] >= 250:

            # Determining which legendary item was obtained and printing the message
            if material == "shards":
                print("Shadowmourne obtained!")
            elif material == "fragments":
                print("Valanyr obtained!")
            elif material == "motes":
                print("Dragonwrath obtained!")

            # Reducing the key material quantity by 250 and marking the legendary item as obtained
            keyMaterials[material] -= 250
            obtainedItem = True
            break

    else:

        # Adding the junk item to the dictionary of junk materials
        if material not in junkMaterials:
            junkMaterials[material] = 0
        junkMaterials[material] += quantity

    print(f"shards: {keyMaterials['shards']}")
    print(f"fragments: {keyMaterials['fragments']}")
    print(f"motes: {keyMaterials['motes']}")
    for material, quantity in sorted(junkMaterials.items()): print(f"{material}: {quantity}")