
# CATIA Aircraft Geometry Automation & Aerodynamic Analysis
## Project Overview
This project demonstrates a parametric automation workflow integrating **CATIA V5** and **Python** to modify aircraft geometry and evaluate aerodynamic performance. The objective is to create a simplified **design–analysis loop** where a geometric parameter directly influences aerodynamic calculations. Using Python’s COM interface (`win32com`), the script connects to CATIA V5, modifies a wing geometry parameter, updates the 3D model, and computes aerodynamic performance metrics automatically.

## Key Features
- Connection to CATIA V5 via COM automation
- Reading and modifying a custom design parameter (`Wing_Span`)
- Automatic 3D geometry update
- Wing area computation
- Aspect Ratio (AR) calculation
- Induced drag estimation using finite wing theory
- Total drag coefficient calculation (CD₀ + CDᵢ)
- Lift and Drag force computation
- Lift-to-Drag ratio (L/D) evaluation
- Velocity sweep analysis (Lift vs Velocity)

## Aerodynamic Model
The script implements simplified preliminary aircraft design relations.

**Wing Area**  
`S = b × c` (assuming constant chord)

**Aspect Ratio**  
`AR = b² / S`

**Induced Drag Coefficient**  
`CDi = CL² / (π ARe)`  
Where:  
- `CL` = Lift coefficient  
- `AR` = Aspect ratio  
- `e` = Oswald efficiency factor

**Total Drag Coefficient**  
`CD = CD₀ + CDi`

**Aerodynamic Forces**  
`Lift = ½ ρ V² S CL`  
`Drag = ½ ρ V² S CD`

This allows evaluation of how wing span variations influence aerodynamic efficiency and performance.

## Technologies Used
- CATIA V5
- Python
- win32com (COM automation)
- NumPy

## How It Works
1. Open **CATIA V5** and load the aircraft `CATPart` file.  
2. Ensure a custom parameter named `Wing_Span` exists in the model.  
3. Run the Python script.  
4. Enter a new wing span value when prompted.  

The script will:  
- Update the geometry in CATIA  
- Recompute aerodynamic parameters  
- Display results in the terminal

## Example Output
The script outputs:  
- Updated Wing Area  
- Aspect Ratio  
- Drag Coefficient  
- Lift Force  
- Drag Force  
- Lift-to-Drag Ratio  
- Lift variation across a velocity range

## Engineering Objective
This project demonstrates how **parametric CAD modeling** can be integrated with **performance analysis through automation**. It represents a simplified preliminary aircraft design workflow combining geometry control and aerodynamic evaluation.

## Future Improvements
- Drag polar plotting  
- Performance optimization loop  
- Exporting results to CSV  
- Integration with CFD simulations  
- Variable chord or tapered wing modeling

## Author
**Elaa Hamdani**  
Engineering Student at INSAT – Instrumentation & Industrial Maintenance Engineering  
Specialized in AI & Aerodynamics
