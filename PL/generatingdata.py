import pandas as pd
import matplotlib.pyplot as plt

# Data growth chart
data = {
    "Umur (bulan)": list(range(25)),
    "-3 SD": [2.1, 2.9, 3.8, 4.4, 4.9, 5.3, 5.7, 5.9, 6.2, 6.4, 6.6, 6.8, 6.9, 7.1, 7.2, 7.4, 7.5, 7.7, 7.8, 8.0, 8.1, 8.2, 8.4, 8.5, 8.6],
    "-2 SD": [2.5, 3.4, 4.3, 5.0, 5.6, 6.0, 6.4, 6.7, 6.9, 7.1, 7.4, 7.6, 7.7, 7.9, 8.1, 8.3, 8.4, 8.6, 8.8, 8.9, 9.1, 9.2, 9.4, 9.5, 9.7],
    "-1 SD": [2.9, 3.9, 4.9, 5.7, 6.2, 6.7, 7.1, 7.4, 7.7, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10.0, 10.1, 10.3, 10.5, 10.7, 10.8],
    "Median": [3.3, 4.5, 5.6, 6.4, 7.0, 7.5, 7.9, 8.3, 8.6, 8.9, 9.2, 9.4, 9.6, 9.9, 10.1, 10.3, 10.5, 10.7, 10.9, 11.1, 11.3, 11.5, 11.8, 12.0, 12.2],
    "+1 SD": [3.9, 5.1, 6.3, 7.2, 7.8, 8.4, 8.8, 9.2, 9.6, 9.9, 10.2, 10.5, 10.8, 11.0, 11.3, 11.5, 11.7, 12.0, 12.2, 12.5, 12.7, 12.9, 13.2, 13.4, 13.6],
    "+2 SD": [4.4, 5.8, 7.1, 8.0, 8.7, 9.3, 9.8, 10.3, 10.7, 11.0, 11.4, 11.7, 12.0, 12.3, 12.6, 12.8, 13.1, 13.4, 13.7, 13.9, 14.2, 14.5, 14.7, 15.0, 15.3],
    "+3 SD": [5.0, 6.6, 8.0, 9.0, 9.7, 10.4, 10.9, 11.4, 11.9, 12.3, 12.7, 13.0, 13.3, 13.7, 14.0, 14.3, 14.6, 14.9, 15.3, 15.6, 15.9, 16.2, 16.5, 16.8, 17.1]
}

df = pd.DataFrame(data)

# Menambahkan kategori status gizi berdasarkan input berat badan
def kategori_status_gizi(berat_badan, umur):
    if umur > 24 or umur < 0:
        return "Umur tidak valid"
    
    median = df[df["Umur (bulan)"] == umur]["Median"].values[0]
    sd_neg2 = df[df["Umur (bulan)"] == umur]["-2 SD"].values[0]
    sd_neg1 = df[df["Umur (bulan)"] == umur]["-1 SD"].values[0]
    sd_pos1 = df[df["Umur (bulan)"] == umur]["+1 SD"].values[0]

    if berat_badan < sd_neg2:
        return 'Berat badan sangat kurang'
    elif berat_badan >= sd_neg2 and berat_badan < sd_neg1:
        return 'Berat badan kurang'
    elif berat_badan >= sd_neg1 and berat_badan <= sd_pos1:
        return 'Berat badan normal'
    else:
        return 'Risiko berat badan berlebih'

# Input umur dan berat badan dari user
umur_input = int(input("Masukkan umur (bulan): "))
berat_badan_input = float(input("Masukkan berat badan (kg): "))

# Tentukan status gizi dari input user
status_gizi = kategori_status_gizi(berat_badan_input, umur_input)
print(f"Status Gizi: {status_gizi}")

# Plotting the data with specified colors
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["Umur (bulan)"], df["-3 SD"], label="-3 SD", color="red")
ax.plot(df["Umur (bulan)"], df["-2 SD"], label="-2 SD", color="orange")
ax.plot(df["Umur (bulan)"], df["-1 SD"], label="-1 SD", color="yellow")
ax.plot(df["Umur (bulan)"], df["Median"], label="Median", color="green")
ax.plot(df["Umur (bulan)"], df["+1 SD"], label="+1 SD", color="yellow")
ax.plot(df["Umur (bulan)"], df["+2 SD"], label="+2 SD", color="orange")
ax.plot(df["Umur (bulan)"], df["+3 SD"], label="+3 SD", color="red")

# Plot the user's data point
ax.scatter(umur_input, berat_badan_input, color='blue', label=f'Input: {umur_input} bln, {berat_badan_input} kg')

# Add annotation pop-up
annot = ax.annotate("", xy=(0,0), xytext=(20,20),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(x, y, text):
    annot.xy = (x, y)
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor("lightblue")

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = ax.collections[-1].contains(event)
        if cont:
            update_annot(umur_input, berat_badan_input, f"Umur: {umur_input} bln\nBerat: {berat_badan_input} kg\nStatus: {status_gizi}")
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.xlabel("Umur (bulan)")
plt.ylabel("Berat Badan (Kg)")
plt.title("Grafik Berat Badan Berdasarkan Umur")
plt.legend()
plt.grid(True)
plt.show()
