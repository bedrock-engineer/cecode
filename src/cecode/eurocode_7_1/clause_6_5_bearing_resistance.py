import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # Constants for calculations
    # These are default values and can be adjusted by the user
    width = 2.0  # Width of the foundation (B) in meters
    length = 3.0  # Length of the foundation (L) in meters
    depth = 1.0  # Depth of the foundation (D) in meters
    unit_weight_soil = 18.0  # Unit weight of soil (γ) in kN/m³
    cohesion = 25.0  # Cohesion of soil (c) in kN/m²
    friction_angle = 30.0  # Angle of internal friction (φ) in degrees

    # Display the input parameters
    mo.md(r"""
    ## Inputs

    - **Width of the foundation (B):**
      - Default value: 2.0 m
      - Lower bound: 0.5 m
      - Upper bound: 10.0 m
      - Description: Width of the foundation in meters
      - LaTeX symbol: $B$
      - Unit: m

    - **Length of the foundation (L):**
      - Default value: 3.0 m
      - Lower bound: 0.5 m
      - Upper bound: 10.0 m
      - Description: Length of the foundation in meters
      - LaTeX symbol: $L$
      - Unit: m

    - **Depth of the foundation (D):**
      - Default value: 1.0 m
      - Lower bound: 0.5 m
      - Upper bound: 5.0 m
      - Description: Depth of the foundation in meters
      - LaTeX symbol: $D$
      - Unit: m

    - **Unit weight of soil (γ):**
      - Default value: 18.0 kN/m³
      - Lower bound: 10.0 kN/m³
      - Upper bound: 25.0 kN/m³
      - Description: Unit weight of the soil in kN/m³
      - LaTeX symbol: $\gamma$
      - Unit: kN/m³

    - **Cohesion of soil (c):**
      - Default value: 25.0 kN/m²
      - Lower bound: 0.0 kN/m²
      - Upper bound: 100.0 kN/m²
      - Description: Cohesion of the soil in kN/m²
      - LaTeX symbol: $c$
      - Unit: kN/m²

    - **Angle of internal friction (φ):**
      - Default value: 30.0 degrees
      - Lower bound: 0.0 degrees
      - Upper bound: 45.0 degrees
      - Description: Angle of internal friction in degrees
      - LaTeX symbol: $\phi$
      - Unit: degrees

    """)
    return (
        cohesion,
        depth,
        friction_angle,
        length,
        mo,
        np,
        pd,
        plt,
        unit_weight_soil,
        width,
    )


@app.cell
def _(mo):
    mo.md(
        r"""
        From marimo's kapa.ai: 

        >The error you're encountering is related to how LaTeX and f-strings interact in Marimo's markdown function. The issue is that you're using an r-string (raw string) with the .format() method, but your LaTeX expressions contain curly braces which are conflicting with Python's string formatting syntax.
        >
        >When you use curly braces in LaTeX (like in \pi \tan \phi), Python's .format() method interprets these as placeholders for formatting, causing the KeyError: '\\pi \\tan \\phi' error.
        >
        >To fix this issue, you need to escape the curly braces in your LaTeX expressions by doubling them. This tells Python to treat them as literal curly braces rather than format specifiers.
        >
        >Notice below how I've doubled the curly braces in the LaTeX expressions (e.g., e^{{\pi \tan \phi}} instead of e^{\pi \tan \phi}). This is a common requirement when mixing LaTeX with Python string formatting.
        >
        >[source](https://discord.com/channels/1059888774789730424/1362549495576924170/1362549585045750053)
        """
    )
    return


@app.cell
def _(friction_angle, mo, np):
    # Calculation of bearing capacity factors
    # Reference: Eurocode 7, Clause 6.5

    # Convert friction angle to radians for calculation
    phi_rad = np.radians(friction_angle)

    # Bearing capacity factors
    Nq = np.exp(np.pi * np.tan(phi_rad)) * (np.tan(np.radians(45) + phi_rad / 2)) ** 2
    Nc = (Nq - 1) / np.tan(phi_rad)
    Ngamma = 2 * (Nq + 1) * np.tan(phi_rad)

    mo.md(
        r"""
    ## Calculation

    ### Bearing Capacity Factors

    - **Clause 6.5**

    The bearing capacity factors are calculated as follows:

    - $N_q = e^{{\pi \tan \phi}} \tan^2(45^\circ + \frac{{\phi}}{{2}})$
    - $N_c = \frac{{N_q - 1}}{{\tan \phi}}$
    - $N_\gamma = 2 (N_q + 1) \tan \phi$

    Intermediate values:

    - $N_q = {:.2f}$
    - $N_c = {:.2f}$
    - $N_\gamma = {:.2f}$

    """.format(Nq, Nc, Ngamma)
    )
    return Nc, Ngamma, Nq, phi_rad


@app.cell
def _(Nc, Ngamma, Nq, cohesion, depth, mo, unit_weight_soil, width):
    # Calculation of ultimate bearing capacity
    # Reference: Eurocode 7, Clause 6.5

    # Shape factors (assuming strip footing for simplicity)
    sc = 1.0
    sq = 1.0
    sgamma = 1.0

    # Depth factors
    # Assuming depth factor is 1 for simplicity
    # More complex calculations can be added based on specific conditions

    # Ultimate bearing capacity
    qult = (
        (cohesion * Nc * sc)
        + (unit_weight_soil * depth * Nq * sq)
        + (0.5 * unit_weight_soil * width * Ngamma * sgamma)
    )

    mo.md(
        r"""
    ### Ultimate Bearing Capacity

    - **Clause 6.5**

    The ultimate bearing capacity is calculated using the formula:

    $$q_{ult} = c N_c s_c + \gamma D N_q s_q + 0.5 \gamma B N_\gamma s_\gamma$$

    Where:
    - $s_c$, $s_q$, $s_\gamma$ are shape factors (assumed to be 1 for strip footing)

    Intermediate and final results:

    - $q_{ult} = {:.2f}$ kN/m²

    """.format(qult)
    )
    return qult, sc, sgamma, sq


@app.cell
def _(mo, qult):
    # Results summary

    mo.md(
        r"""
    ## Results

    The final calculated ultimate bearing capacity of the shallow foundation is:

    - $q_{ult} = {:.2f}$ kN/m²

    This value represents the maximum pressure that the soil can support under the foundation without failure.

    """.format(qult)
    )
    return


if __name__ == "__main__":
    app.run()
