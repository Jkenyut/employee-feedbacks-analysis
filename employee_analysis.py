from cgitb import text
import os
import cv2
import speech_recognition as sr
import pandas as pd
import numpy as np
import face_recognition
from datetime import datetime
import moviepy.editor as mp

r = sr.Recognizer()
# bert library
import transformers
import tensorflow as tf
from transformers import TFBertForSequenceClassification
from transformers import BertTokenizer

# inisialisasi persiapan bert
PRE_TRAINED_MODEL = "indobenchmark/indobert-base-p2"
bert_tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL)

# melakukan encoding gambar di folder untuk face recognition
path = "/content/drive/MyDrive/Orbit/PA/Karyawan"
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f"{path}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# data karyawan
data_karyawan = pd.read_csv(
    "/content/drive/MyDrive/Orbit/PA/Karyawan.csv"
)  # sesuaikan path
feedback = pd.read_csv("/content/drive/MyDrive/Orbit/PA/Feedback.csv")  # sesuaikan path


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError as e:
            print(e)
    return encodeList


encodeListKnown = findEncodings(images)


# fungsi merubah mp4 ke mp3/wav
def video_to_audio(path):
    # drop code untuk mengubah video ke audio
    clip = mp.VideoFileClip(path)
    clip.audio.write_audiofile(r"content" + ".wav")  # sesuaikan path
    return r"content" + ".wav"  # mengembalikan nilai path


# fungsi merubah audio ke teks
def audio_to_teks(path, lang="id-ID"):
    # drop code untuk mengubah audio ke teks
    with sr.AudioFile(path) as source:
        # print('Fetching File')
        audio_file = r.record(source)
    text = r.recognize_google(audio_file, language=lang)
    return text


# fungsi prediksi perasaan
def predict_feeling(path):
    # mp4 to wav/mp3
    vid2aud = video_to_audio(path)
    # audio to teks
    aud2text = audio_to_teks(vid2aud)
    # prediksi emosi teks
    # load pretrained
    bert_load_model = TFBertForSequenceClassification.from_pretrained(
        PRE_TRAINED_MODEL, num_labels=5
    )
    bert_load_model.load_weights(
        "/content/drive/MyDrive/Orbit/PA/bert-model.h5"
    )  # sesuaikan path
    # Encode input text
    input_text_tokenized = bert_tokenizer.encode(
        aud2text, truncation=True, padding="max_length", return_tensors="tf"
    )
    bert_predict = bert_load_model(input_text_tokenized)  # Lakukan prediksi
    bert_output = tf.nn.softmax(
        bert_predict[0], axis=-1
    )  # Softmax function untuk mendapatkan hasil klasifikasi
    emotion_label = ["anger", "happy", "sadness", "fear", "love"]
    label = tf.argmax(bert_output, axis=1)
    label = label.numpy()
    feel = emotion_label[label[0]]
    return aud2text, feel


# fungsi untuk identifikasi wajah karyawan
def faces_encode(img):
    facesCurFrame = face_recognition.face_locations(img)
    encodesCurFrame = face_recognition.face_encodings(img, facesCurFrame)
    zipped_faces_encode = zip(encodesCurFrame, facesCurFrame)
    return facesCurFrame, zipped_faces_encode


def employee_identity(path):
    # drop code untuk mengidentifikasi wajah karyawan
    cap = cv2.VideoCapture(path)
    run = True
    while run:
        success, frame = cap.read()
        img = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        facesCurFrame, zipped_faces_encode = faces_encode(img)
        if not facesCurFrame:
            img1 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            facesCurFrame, zipped_faces_encode = faces_encode(img1)
        if not facesCurFrame:
            img2 = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
            facesCurFrame, zipped_faces_encode = faces_encode(img2)
        for encodeFace, faceLoc in zipped_faces_encode:
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                id = classNames[matchIndex].lower()

                if id in list(str(data_karyawan["Id"])):
                    id_karyawan = int(id)
                    print(id_karyawan)
                    run = False
                else:
                    print("none")
    return id_karyawan  # mengembalikan id karyawan


# menambahkan data hasil analisis video dan teks
def add_to_list(id, komentar, perasaan):
    # mencari nilai id pada csv data karyawan
    profile_akun = data_karyawan[data_karyawan["Id"] == id]
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
    #
    # hasil identifikasi wajah
    id_karyawan = employee_identity(path)
    # hasil analisis komentar dan perasaan
    komentar, perasaan = predict_feeling(path)
    # hasil keseluruhan analisis
    data = add_to_list(id_karyawan, komentar, perasaan)
    # tambah ke dataframe
    data_series = pd.Series(data, index=feedback.columns)
    hasil_feedback = feedback.append(data_series, ignore_index=True)
    hasil_feedback.to_csv("/content/drive/MyDrive/Orbit/PA/Feedback.csv")
    return id_karyawan, komentar, perasaan
