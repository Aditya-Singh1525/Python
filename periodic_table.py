print("This is a AI for periodic table!")


def main():

    ask = input("\nEnter any thing of an element:")
    found_elements = []

    elements = {
        1: ("Hydrogen", "H", "Atomic.no: 1", "Mass.no: 1.008"),
        2: ("Helium", "He", "Atomic.no: 2", "Mass.no: 4.0026"),
        3: ("Lithium", "Li", "Atomic.no: 3", "Mass.no: 6.94"),
        4: ("Beryllium", "Be", "Atomic.no: 4", "Mass.no: 9.0122"),
        5: ("Boron", "B", "Atomic.no: 5", "Mass.no: 10.81"),
        6: ("Carbon", "C", "Atomic.no: 6", "Mass.no: 12.011"),
        7: ("Nitrogen", "N", "Atomic.no: 7", "Mass.no: 14.007"),
        8: ("Oxygen", "O", "Atomic.no: 8", "Mass.no: 15.999"),
        9: ("Fluorine", "F", "Atomic.no: 9", "Mass.no: 18.998"),
        10: ("Neon", "Ne", "Atomic.no: 10", "Mass.no: 20.180"),
        11: ("Sodium", "Na", "Atomic.no: 11", "Mass.no: 22.990"),
        12: ("Magnesium", "Mg", "Atomic.no: 12", "Mass.no: 24.305"),
        13: ("Aluminium", "Al", "Atomic.no: 13", "Mass.no: 26.982"),
        14: ("Silicon", "Si", "Atomic.no: 14", "Mass.no: 28.085"),
        15: ("Phosphorus", "P", "Atomic.no: 15", "Mass.no: 30.974"),
        16: ("Sulfur", "S", "Atomic.no: 16", "Mass.no: 32.06"),
        17: ("Chlorine", "Cl", "Atomic.no: 17", "Mass.no: 35.45"),
        18: ("Argon", "Ar", "Atomic.no: 18", "Mass.no: 39.948"),
        19: ("Potassium", "K", "Atomic.no: 19", "Mass.no: 39.098"),
        20: ("Calcium", "Ca", "Atomic.no: 20", "Mass.no: 40.078"),
        21: ("Scandium", "Sc", "Atomic.no: 21", "Mass.no: 44.956"),
        22: ("Titanium", "Ti", "Atomic.no: 22", "Mass.no: 47.867"),
        23: ("Vanadium", "V", "Atomic.no: 23", "Mass.no: 50.942"),
        24: ("Chromium", "Cr", "Atomic.no: 24", "Mass.no: 51.996"),
        25: ("Manganese", "Mn", "Atomic.no: 25", "Mass.no: 54.938"),
        26: ("Iron", "Fe", "Atomic.no: 26", "Mass.no: 55.845"),
        27: ("Cobalt", "Co", "Atomic.no: 27", "Mass.no: 58.933"),
        28: ("Nickel", "Ni", "Atomic.no: 28", "Mass.no: 58.693"),
        29: ("Copper", "Cu", "Atomic.no: 29", "Mass.no: 63.546"),
        30: ("Zinc", "Zn", "Atomic.no: 30", "Mass.no: 65.38"),
        31: ("Gallium", "Ga", "Atomic.no: 31", "Mass.no: 69.723"),
        32: ("Germanium", "Ge", "Atomic.no: 32", "Mass.no: 72.630"),
        33: ("Arsenic", "As", "Atomic.no: 33", "Mass.no: 74.922"),
        34: ("Selenium", "Se", "Atomic.no: 34", "Mass.no: 78.971"),
        35: ("Bromine", "Br", "Atomic.no: 35", "Mass.no: 79.904"),
        36: ("Krypton", "Kr", "Atomic.no: 36", "Mass.no: 83.798"),
        37: ("Rubidium", "Rb", "Atomic.no: 37", "Mass.no: 85.468"),
        38: ("Strontium", "Sr", "Atomic.no: 38", "Mass.no: 87.62"),
        39: ("Yttrium", "Y", "Atomic.no: 39", "Mass.no: 88.906"),
        40: ("Zirconium", "Zr", "Atomic.no: 40", "Mass.no: 91.224"),
        41: ("Niobium", "Nb", "Atomic.no: 41", "Mass.no: 92.906"),
        42: ("Molybdenum", "Mo", "Atomic.no: 42", "Mass.no: 95.95"),
        43: ("Technetium", "Tc", "Atomic.no: 43", "Mass.no: [97]"),
        44: ("Ruthenium", "Ru", "Atomic.no: 44", "Mass.no: 101.07"),
        45: ("Rhodium", "Rh", "Atomic.no: 45", "Mass.no: 102.91"),
        46: ("Palladium", "Pd", "Atomic.no: 46", "Mass.no: 106.42"),
        47: ("Silver", "Ag", "Atomic.no: 47", "Mass.no: 107.87"),
        48: ("Cadmium", "Cd", "Atomic.no: 48", "Mass.no: 112.41"),
        49: ("Indium", "In", "Atomic.no: 49", "Mass.no: 114.82"),
        50: ("Tin", "Sn", "Atomic.no: 50", "Mass.no: 118.71"),
        51: ("Antimony", "Sb", "Atomic.no: 51", "Mass.no: 121.76"),
        52: ("Tellurium", "Te", "Atomic.no: 52", "Mass.no: 127.60"),
        53: ("Iodine", "I", "Atomic.no: 53", "Mass.no: 126.90"),
        54: ("Xenon", "Xe", "Atomic.no: 54", "Mass.no: 131.29"),
        55: ("Caesium", "Cs", "Atomic.no: 55", "Mass.no: 132.91"),
        56: ("Barium", "Ba", "Atomic.no: 56", "Mass.no: 137.33"),
        57: ("Lanthanum", "La", "Atomic.no: 57", "Mass.no: 138.91"),
        58: ("Cerium", "Ce", "Atomic.no: 58", "Mass.no: 140.12"),
        59: ("Praseodymium", "Pr", "Atomic.no: 59", "Mass.no: 140.91"),
        60: ("Neodymium", "Nd", "Atomic.no: 60", "Mass.no: 144.24"),
        61: ("Promethium", "Pm", "Atomic.no: 61", "Mass.no: [145]"),
        62: ("Samarium", "Sm", "Atomic.no: 62", "Mass.no: 150.36"),
        63: ("Europium", "Eu", "Atomic.no: 63", "Mass.no: 151.96"),
        64: ("Gadolinium", "Gd", "Atomic.no: 64", "Mass.no: 157.25"),
        65: ("Terbium", "Tb", "Atomic.no: 65", "Mass.no: 158.93"),
        66: ("Dysprosium", "Dy", "Atomic.no: 66", "Mass.no: 162.50"),
        67: ("Holmium", "Ho", "Atomic.no: 67", "Mass.no: 164.93"),
        68: ("Erbium", "Er", "Atomic.no: 68", "Mass.no: 167.26"),
        69: ("Thulium", "Tm", "Atomic.no: 69", "Mass.no: 168.93"),
        70: ("Ytterbium", "Yb", "Atomic.no: 70", "Mass.no: 173.05"),
        71: ("Lutetium", "Lu", "Atomic.no: 71", "Mass.no: 174.97"),
        72: ("Hafnium", "Hf", "Atomic.no: 72", "Mass.no: 178.49"),
        73: ("Tantalum", "Ta", "Atomic.no: 73", "Mass.no: 180.95"),
        74: ("Tungsten", "W", "Atomic.no: 74", "Mass.no: 183.84"),
        75: ("Rhenium", "Re", "Atomic.no: 75", "Mass.no: 186.21"),
        76: ("Osmium", "Os", "Atomic.no: 76", "Mass.no: 190.23"),
        77: ("Iridium", "Ir", "Atomic.no: 77", "Mass.no: 192.22"),
        78: ("Platinum", "Pt", "Atomic.no: 78", "Mass.no: 195.08"),
        79: ("Gold", "Au", "Atomic.no: 79", "Mass.no: 196.97"),
        80: ("Mercury", "Hg", "Atomic.no: 80", "Mass.no: 200.59"),
        81: ("Thallium", "Tl", "Atomic.no: 81", "Mass.no: 204.38"),
        82: ("Lead", "Pb", "Atomic.no: 82", "Mass.no: 207.2"),
        83: ("Bismuth", "Bi", "Atomic.no: 83", "Mass.no: 208.98"),
        84: ("Polonium", "Po", "Atomic.no: 84", "Mass.no: [209]"),
        85: ("Astatine", "At", "Atomic.no: 85", "Mass.no: [210]"),
        86: ("Radon", "Rn", "Atomic.no: 86", "Mass.no: [222]"),
        87: ("Francium", "Fr", "Atomic.no: 87", "Mass.no: [223]"),
        88: ("Radium", "Ra", "Atomic.no: 88", "Mass.no: [226]"),
        89: ("Actinium", "Ac", "Atomic.no: 89", "Mass.no: [227]"),
        90: ("Thorium", "Th", "Atomic.no: 90", "Mass.no: 232.04"),
        91: ("Protactinium", "Pa", "Atomic.no: 91", "Mass.no: [231]"),
        92: ("Uranium", "U", "Atomic.no: 92", "Mass.no: 238.03"),
        93: ("Neptunium", "Np", "Atomic.no: 93", "Mass.no: [237]"),
        94: ("Plutonium", "Pu", "Atomic.no: 94", "Mass.no: [244]"),
        95: ("Americium", "Am", "Atomic.no: 95", "Mass.no: [243]"),
        96: ("Curium", "Cm", "Atomic.no: 96", "Mass.no: [247]"),
        97: ("Berkelium", "Bk", "Atomic.no: 97", "Mass.no: [247]"),
        98: ("Californium", "Cf", "Atomic.no: 98", "Mass.no: [251]"),
        99: ("Einsteinium", "Es", "Atomic.no: 99", "Mass.no: [252]"),
        100: ("Fermium", "Fm", "Atomic.no: 100", "Mass.no: [257]"),
        101: ("Mendelevium", "Md", "Atomic.no: 101", "Mass.no: [258]"),
        102: ("Nobelium", "No", "Atomic.no: 102", "Mass.no: [259]"),
        103: ("Lawrencium", "Lr", "Atomic.no: 103", "Mass.no: [266]"),
        104: ("Rutherfordium", "Rf", "Atomic.no: 104", "Mass.no: [267]"),
        105: ("Dubnium", "Db", "Atomic.no: 105", "Mass.no: [268]"),
        106: ("Seaborgium", "Sg", "Atomic.no: 106", "Mass.no: [269]"),
        107: ("Bohrium", "Bh", "Atomic.no: 107", "Mass.no: [270]"),
        108: ("Hassium", "Hs", "Atomic.no: 108", "Mass.no: [271]"),
        109: ("Meitnerium", "Mt", "Atomic.no: 109", "Mass.no: [278]"),
        110: ("Darmstadtium", "Ds", "Atomic.no: 110", "Mass.no: [281]"),
        111: ("Roentgenium", "Rg", "Atomic.no: 111", "Mass.no: [282]"),
        112: ("Copernicium", "Cn", "Atomic.no: 112", "Mass.no: [285]"),
        113: ("Nihonium", "Nh", "Atomic.no: 113", "Mass.no: [286]"),
        114: ("Flerovium", "Fl", "Atomic.no: 114", "Mass.no: [289]"),
        115: ("Moscovium", "Mc", "Atomic.no: 115", "Mass.no: [290]"),
        116: ("Livermorium", "Lv", "Atomic.no: 116", "Mass.no: [293]"),
        117: ("Tennessine", "Ts", "Atomic.no: 117", "Mass.no: [294]"),
        118: ("Oganesson", "Og", "Atomic.no: 118", "Mass.no: [294]"),
    }

    try:
        ask_as_float = float(ask)
    except ValueError:
        ask_as_float = None

    try:
        ask_as_int = int(ask)
    except ValueError:
        ask_as_int = None

    ask_lower = ask.lower()

    for key, value in elements.items():
        mass_no_string = value[3].split(": ")[1]

        if (
            ask_as_int == key
            or ask_lower == value[0].lower()
            or ask_lower == value[1].lower()
        ):
            found_elements.append((key, value))

        if mass_no_string == ask or mass_no_string == f"[{ask}]":
            found_elements.append((key, value))
        elif ask_as_float is not None:
            try:
                if float(mass_no_string) == ask_as_float:
                    found_elements.append((key, value))
            except ValueError:
                pass

    if found_elements:
        print("\n--- Found Element(s) ---")
        for key, value in found_elements:
            name, symbol, atomic_no, mass_no = value
            print(f"Name: {name}")
            print(f"Symbol: {symbol}")
            print(f"Atomic Number: {key}")
            print(f"Mass Number: {mass_no.split(': ')[1]}")
            print("-" * 25)
    else:
        print(
            "\nNo element found with that name, symbol, atomic number, or mass number."
        )


if __name__ == "__main__":
    main()

while True:
    ask = input("\nDo you wanna continue? {Y/n}:")

    if ask == "n":
        print("\nThanks for using my AI!!")
        break
    else:
        main()
