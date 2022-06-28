import streamlit as st
import numpy as np
import pickle
import import_ipynb
import preprocess
import time
import os
import io

# chuyển nhãn sang tiếng việt
name_result = {
    'Am nhac': 'Âm nhạc',
    'Am thuc': 'Ẩm thực',
    'Bat dong san': 'Bất động sản',
    'Bong da': 'Bóng đá',
    'Chung khoan': 'Chứng khoán',
    'Cum ga': 'Cúm gà',
    'Cuoc song do day': 'Cuộc sống đó đây',
    'Du hoc': 'Du học',
    'Du lich': 'Du lịch',
    'Duong vao WTO': 'Đường vào WTO',
    'Gia dinh': 'Gia đình',
    'Giai tri tin hoc': 'Giải trí tin học',
    'Giao duc': 'Giáo dục',
    'Gioi tinh': 'Giới tính',
    'Hackers va Virus': 'Hackers và Virus',
    'Hinh su': 'Hình sự',
    'Khong gian song': 'Không gian sống',
    'Kinh doanh quoc te': 'Kinh doanh quốc tế',
    'Lam dep': 'Làm đẹp',
    'Loi song': 'Lối sống',
    'Mua sam': 'Mua sắm',
    'My thuat': 'Mỹ thuật',
    'San khau dien anh': 'Sân khấu điện ảnh',
    'San pham tin hoc moi': 'Sản phẩm tin học mới',
    'Tennis': 'Tennis',
    'The gioi tre': 'Thế giới trẻ',
    'Thoi trang': 'Thời trang'
}

st.title('Vietnamese News Classification')

# load model
model = pickle.load(open('Data/saved/best_model.sav', 'rb'))

# load feature extractor
feature_extractor = pickle.load(open('Data/saved/feature_extractor.sav', 'rb'))

news = st.text_area('News input')
if news:

    # Tiền xử lý và loại bỏ stopwords
    start = time.time()
    data = preprocess.text_preprocessing(news)
    data = preprocess.remove_stopwords(data)
    preprocess_time = time.time() - start

    # Dự đoán
    start = time.time()
    np_data = np.array([data])
    feature = feature_extractor.transform(np_data)
    pred = model.predict(feature)
    result = name_result[pred[0]]
    predict_time = time.time() - start

    total = round(predict_time + preprocess_time, 2)

    # Hiện kết quả
    st.text('Kết quả: ' + result)
    st.text('Time: ' + str(total) + 's')
    #st.text('Data preprocessed: ' + data)
