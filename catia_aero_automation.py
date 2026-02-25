import win32com.client
import numpy as np

# ==============================
# CONNECT TO CATIA
# ==============================

try:
    catia = win32com.client.Dispatch("CATIA.Application")
    catia.Visible = True
    print(" Connected to CATIA successfully.")
except:
    print(" Make sure CATIA is running.")
    exit()

# ==============================
# ACCESS ACTIVE PART
# ==============================

try:
    document = catia.ActiveDocument
    part = document.Part
    parameters = part.Parameters
except:
    print(" Open your aircraft CATPart file first.")
    exit()

# ==============================
# READ CURRENT WING SPAN
# ==============================

try:
    wing_span = parameters.Item("Wing_Span").Value
    print(f" Current Wing Span: {wing_span:.2f} m")
except:
    print(" Parameter 'Wing_Span' not found.")
    exit()

# ==============================
# USER INPUT - NEW SPAN
# ==============================

new_span = float(input("\nEnter new Wing Span (meters): "))

parameters.Item("Wing_Span").Value = new_span
part.Update()

print(f"\n Wing span updated to {new_span:.2f} meters in CATIA.")

# ==============================
# AERODYNAMIC PARAMETERS
# ==============================

rho = 1.225        # Air density (kg/m^3)
V = 70             # Cruise velocity (m/s)
CL = 0.5           # Lift coefficient
CD0 = 0.02         # Zero-lift drag coefficient
e = 0.8            # Oswald efficiency factor
chord = 3          # Assumed constant chord length (m)

# ==============================
# GEOMETRIC CALCULATIONS
# ==============================

S = new_span * chord              # Wing area
AR = new_span**2 / S              # Aspect Ratio

# ==============================
# AERODYNAMIC CALCULATIONS
# ==============================

# Induced drag coefficient
CDi = (CL**2) / (np.pi * AR * e)

# Total drag coefficient
CD = CD0 + CDi

# Forces
Lift = 0.5 * rho * V**2 * S * CL
Drag = 0.5 * rho * V**2 * S * CD

LD_ratio = Lift / Drag

# ==============================
# RESULTS
# ==============================

print("\n==============================")
print("      AERODYNAMIC RESULTS")
print("==============================")

print(f"Wing Area (S): {S:.2f} m^2")
print(f"Aspect Ratio (AR): {AR:.2f}")
print(f"Total Drag Coefficient (CD): {CD:.4f}")
print(f"Lift: {Lift:.2f} N")
print(f"Drag: {Drag:.2f} N")
print(f"Lift-to-Drag Ratio (L/D): {LD_ratio:.2f}")

# ==============================
# VELOCITY SWEEP ANALYSIS
# ==============================

print("\n--- Velocity Sweep (Lift vs Velocity) ---")

for velocity in range(30, 121, 10):
    lift = 0.5 * rho * velocity**2 * S * CL
    print(f"Velocity: {velocity} m/s -> Lift: {lift:.2f} N")
