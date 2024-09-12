# resistor_tools.py

def parallel_resistance(R1, R2):
    """
    Beregner den samlede modstand af to modstande i parallel.
    """
    return 1 / ((1 / R1) + (1 / R2))

def parallel_resistance_multi(*resistors):
    """
    Beregner den samlede modstand af et vilkårligt antal modstande i parallel.
    """
    total_inverse = sum(1 / R for R in resistors)
    return 1 / total_inverse

def voltage_divider(Vin, R1, R2):
    """
    Beregner spændingen (Vout) for en spændingsdeler.
    """
    return Vin * (R2 / (R1 + R2))
