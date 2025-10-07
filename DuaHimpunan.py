import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Definisi himpunan
A = {"Andi", "Budi", "Citra", "Dika"}
B = {"Budi", "Citra", "Eko", "Fanny"}

# Hitung elemen untuk setiap bagian
only_A = A - B  # Elemen hanya di A CT
only_B = B - A  # Elemen hanya di B
A_and_B = A & B  # Elemen di A dan B

# Buat diagram Venn
plt.figure(figsize=(5,5))
venn = venn2(subsets=(len(only_A), len(only_B), len(A_and_B)), set_labels=('A', 'B'))

# Mengisi angka-angka dari himpunan ke dalam diagram Venn
def set_labels(subset, values):
    if subset:  # Jika subset tidak kosong
        subset.set_text("\n".join(map(str, values)))  # Gabungkan angka-angka dalam satu area

set_labels(venn.get_label_by_id('10'), only_A)  # Hanya A
set_labels(venn.get_label_by_id('01'), only_B)  # Hanya B
set_labels(venn.get_label_by_id('11'), A_and_B)  # A ∩ B

plt.title("Diagram Venn untuk Dua Himpunan")
plt.show()
type(A)
