from transformers import VitsModel, AutoTokenizer
import torch
import numpy as np
import scipy.io.wavfile
import simpleaudio as sa
import os
model = VitsModel.from_pretrained("facebook/mms-tts-vie")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-vie")

text = "Mai Huy Hoạt là một sinh viên có đam mê mãnh liệt với công nghệ thông tin. Sinh ra ở Nam Định, anh gặp nhiều khó khăn trong việc tiếp cận công nghệ khi còn nhỏ. Ban đầu, Hoạt dự định du học Nhật Bản để theo đuổi ngành CNTT, nhưng kế hoạch này bị gián đoạn do dịch Covid-19. Sau đó, anh đã tham gia và giành học bổng 50% từ cuộc thi Tài Năng Trẻ IT do FPT Aptech tổ chức, mở ra một hành trình mới trong việc học lập trình tại Việt Nam."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs).waveform

    # Chuyển đổi từ torch.Tensor sang numpy.ndarray
    output_numpy = output.squeeze().cpu().numpy()

    # Chuyển đổi dữ liệu float sang 16-bit PCM
    output_int16 = np.int16(output_numpy / np.max(np.abs(output_numpy)) * 32767)

    # Ghi dữ liệu vào file .wav
    scipy.io.wavfile.write("techno.wav", rate=model.config.sampling_rate, data=output_int16)

    # Phát âm thanh
    wave_obj = sa.WaveObject.from_wave_file("techno.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    os.remove("techno.wav")
