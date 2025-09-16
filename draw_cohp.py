import numpy as np
import matplotlib.pyplot as plt

# ======== Adjustable parameters ========
xlim = (-1, 2.5)                          # X-axis range
ylim = (-16, 6)                         # Y-axis (energy) range
fermi_energy = 0.0                     # Fermi level (usually 0 eV)
data_file = "COHPCAR.lobster"     # Input file name
fontsize_axis_labels = 16             # Font size for axis labels
fontsize_ticks = 14                   # Font size for tick labels
# ======================================

# Load COHP data (skip commented lines)
data = np.loadtxt(data_file, comments="#",skiprows=9)
energy = data[:, 0]
cohp = -data[:, 1]     # COHP is plotted as negative by convention
icohp = -data[:, 2]    # ICOHP also plotted as negative

# Start plotting
plt.figure(figsize=(4, 6))
plt.plot(cohp, energy, label="COHP", color="red", linewidth=1.5)
plt.plot(icohp, energy, label="ICOHP", color="black", linestyle="--", linewidth=2)

# Fill between COHP and zero line to indicate bonding (red) and antibonding (blue)
plt.fill_betweenx(energy, 0, cohp, where=(cohp < 0), color="blue", alpha=0.2)
plt.fill_betweenx(energy, 0, cohp, where=(cohp > 0), color="red", alpha=0.2)

# Add vertical zero line and horizontal Fermi level line
plt.axvline(x=0, color='black')
plt.axhline(y=fermi_energy, color='black', linestyle='--')
plt.text(xlim[1], fermi_energy + 0.2, r"$E_{\mathrm{F}}$", ha="right", va="bottom", fontsize=14)


# Axis labels and limits
plt.xlabel(r"$-$COHP", fontsize=fontsize_axis_labels)
plt.ylabel("Energy (eV)", fontsize=fontsize_axis_labels)
#plt.title("COHPCAR.lobster COHP")
plt.xlim(xlim)
plt.ylim(ylim)

# Tick font size
plt.tick_params(axis='both', which='major', labelsize=fontsize_ticks)

# Legend and output
plt.legend()
plt.tight_layout()
plt.savefig("cohp_plot_shaded.pdf", dpi=300)
