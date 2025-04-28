# Proyek Akhir: Menyelesaikan Permasalahan Atrisi Karyawan Pada Perusahaan IBM

## Business Understanding

IBM adalah perusahaan multinasional yang berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun telah tumbuh menjadi perusahaan berskala besar, IBM masih menghadapi tantangan dalam mengelola karyawan dengan efektif.

### Permasalahan Bisnis

1. Tingginya attrition rate yang mencapai lebih dari 10% menjadi perhatian utama perusahaan karena dapat berdampak negatif pada produktivitas, efisiensi operasional, serta biaya perekrutan karyawan baru.
2. Manager Departemen HR kesulitan dalam mengidentifikasi faktor-faktor penyebab attrition, baik dari aspek usia, departemen, kepuasan kerja, atau faktor demografis lainnya.
3. Kurangnya alat yang terstruktur dan terukur untuk memantau kinerja HR serta tingkat kepuasan karyawan.

### Cakupan Proyek

- Mengolah dan menganalisis dataset pada Perusahaan IBM
- Membuat visualisasi dashboard HR Analytics yang berfokus pada:
  - Employee count, attrition rate, dan profil demografis.
  - Analisis departemen dan bidang pendidikan terkait tingkat attrition.
  - Distribusi employee attrition berdasarkan gender dan umur.
  - Rating kepuasan karyawan berdasarkan peran pekerjaan.
- Memberikan rekomendasi untuk mengurangi tingkat attrition.

### Persiapan

Sumber data: [Employee Data](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

#### Setup environment

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install pandas numpy matplotlib seaborn
```

#### Run prediction.py

```
python prediction.py
```

## Business Dashboard

Link HR Analytics Tableau Public Dashboard : [HR Analytics Dashboard](https://public.tableau.com/views/WatsonsHRAnalyticsDashboard/IBMHRAnalyticsDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Dashboard ini menampilkan berbagai visualisasi terkait **HR Analytics** yang mencakup attrition rate, distribusi berdasarkan departemen,
usia, jenis kelamin (_gender_), pendidikan, dan _rating_ kepuasan karyawan. Dashboard berfungsi sebagai alat bagi manajemen untuk memahami lebih dalam kondisi
tenaga kerja mereka.

### Dashboard Preview

![HR Dashboard](sahrul57-dashboard.png)

## Conclusion

Berdasarkan analisis data dalam dashboard, ditemukan insight berikut:

1. **Departemen Sales** memiliki tingkat attrition tertinggi sebesar **59.78%**. Hal ini mengindikasikan tantangan besar dalam mempertahankan karyawan di departemen ini, yang bisa disebabkan oleh beban kerja tinggi, tekanan pencapaian target penjualan, atau peluang kerja di industri serupa.
2. Karyawan berusia **25-34 tahun** merupakan kelompok dengan tingkat attrition tertinggi, sebesar **28.49%**. Kelompok ini kemungkinan besar terdiri dari profesional muda yang mencari peluang karir atau keseimbangan kehidupan kerja yang lebih baik.
3. **Kepuasan kerja** berperan penting dalam retensi karyawan. Posisi **Sales Executive** dan **Research Scientist** menunjukkan kepuasan yang relatif tinggi, sementara departemen **Human Resources** memiliki tingkat kepuasan terendah. Hal ini menunjukkan perlunya perbaikan dalam sistem manajemen dan kesejahteraan tim HR itu sendiri.
4. Bidang pendidikan **Life Sciences** paling terdampak attrition, menunjukkan adanya keterbatasan dalam pengembangan karir atau kesesuaian peran pekerjaan dengan latar belakang pendidikan tersebut.

### Rekomendasi Action Items

Berikut adalah rekomendasi action items yang harus diperhatikan oleh perusahaan agar menyelesaikan permasalahan atau mencapai target:

1. Meningkatkan retensi di Departemen Sales dengan program kesejahteraan karyawan.
2. Fokus pada pengembangan program khusus untuk usia 25-34 guna mengurangi attrition.
3. Menjalankan survei kepuasan kerja lebih dalam terhadap peran pekerjaan yang memiliki kepuasan rendah.
4. Menyusun program pelatihan ulang (reskilling) karyawan untuk bidang Life Sciences.
