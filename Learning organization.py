ores = ('iron', 'bronze', 'silver', 'gold', 'diamond', 'ruby', 'emerald', 'lapis lazuli', 'aluminium',
        'barium', 'strontium', 'magnesium', 'copper', 'opal', 'aquamarine', 'moonstone',
        'bloodstone', 'topaz', 'garnet', 'agate', 'citrine', 'zircon', 'amethyst')
print(f"{'|Mineral and Gems|':<25}{'Letters A':>}{'Letters E':>10}"
      f"{'Letters I':>10}{'Letters O':>10}{'Letters U':>10}")
for ore in range(0, len(ores)):
    print(f'{ores[ore]:<25}', end='')
    print(f'{ores[ore].count("a"):>5}', end='')
    print(f'{ores[ore].count("e"):>10}', end='')
    print(f'{ores[ore].count("i"):>10}', end='')
    print(f'{ores[ore].count("o"):>10}', end='')
    print(f'{ores[ore].count("u"):>10}')
