# test_resistor_tools.py

import resistor_tools

# Test af parallel modstandsberegner (to modstande)
print("Parallel Modstandsberegner (to modstande)")
R1 = float(input("Indtast værdi for R1 i Ohm: "))
R2 = float(input("Indtast værdi for R2 i Ohm: "))
total_resistance = resistor_tools.parallel_resistance(R1, R2)
print(f"Samlede modstand for R1={R1} og R2={R2} er {total_resistance:.2f} Ohm\n")

# Test af parallel modstandsberegner (flere modstande)
print("Parallel Modstandsberegner (flere modstande)")
num_resistors = int(input("Hvor mange modstande vil du beregne i parallel? "))
resistors = []
for i in range(num_resistors):
    resistor = float(input(f"Indtast værdi for modstand {i+1} i Ohm: "))
    resistors.append(resistor)

total_resistance_multi = resistor_tools.parallel_resistance_multi(*resistors)
print(f"Samlede modstand for {resistors} er {total_resistance_multi:.2f} Ohm\n")

# Test af spændingsdeler
print("Spændingsdeler beregning")
Vin = float(input("Indtast værdi for Vin (indgangsspænding) i Volt: "))
R1 = float(input("Indtast værdi for R1 i Ohm: "))
R2 = float(input("Indtast værdi for R2 i Ohm: "))
Vout = resistor_tools.voltage_divider(Vin, R1, R2)
print(f"Udgangsspænding (Vout) for Vin={Vin}V, R1={R1}Ohm og R2={R2}Ohm er {Vout:.2f}V")
