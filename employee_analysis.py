# fungsi merubah mp4 ke mp3/wav
def video_to_audio(path):
	# drop code untuk mengubah video ke audio
	# ...
	# ...
	path = # isi dengan path ke audio disimpan
	return path # mengembalikan nilai path

# fungsi merubah audio ke teks
def audio_to_teks(path):
	#drop code untuk mengubah audio ke teks
	# ...
	# ...
	teks = # isi dengan teks hasil dari audio
	return teks # mengembalikan nilai teks

# fungsi prediksi perasaan
def predict_feeling(path):
	# mp4 to wav/mp3
	vid2aud = video_to_audio(path)
	# audio to teks
	aud2text = audio_to_teks(vid2aud)
	# prediksi
	feel = # hasil prediksi perasaan
	return aud2text, feel
	
# fungsi untuk identifikasi wajah karyawan
def employee_identity(path):
	# drop code untuk mengidentifikasi wajah karyawan
	# ...
	# ...
	return id_karyawan # mengembalikan id karyawan

# menambahkan data hasil analisis video dan teks
def add_to_list(id, komentar, perasaan):
  # mencari nilai id pada csv data karyawan
  profile_akun = profile[profile['nama'] == id]
  # ubah ke list
  data = profile_akun.values.tolist()[0]
  # datetime
  now = datetime.now()
  # tambahkkan data komentar dan perasaan ke list
  data.append(komentar)
  data.append(perasaan)
  data.append(now.strftime("%m-%d-%Y, %H:%M:%S"))
  return data
	
# fungsi utama
def analysis(path):
	# hasil identifikasi wajah
	id_karyawan = employee_identity(path)
	# hasil analisis komentar dan perasaan
	komentar, perasaan = predict_feeling(path)
	# hasil keseluruhan analisis
	data = add_to_list(id, komentar, perasaan)
	# tambah ke dataframe
	data = pd.DataFrame([a], columns=data_classify_col)
	data_klasifikasi = data_klasifikasi.append(data)
	
