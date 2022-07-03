# Vietnamese News Classification
Bài tập lớn môn Nhập môn Học máy và Khai phá dữ liệu

Đề tài: Phân loại tin tức tiếng Việt

Nguồn dữ liệu: https://github.com/duyvuleo/VNTC

Giáo viên hướng dẫn: ThS. Ngô Văn Linh

### Các model được sử dụng
- K Nearest Neighbors
- Multinomial Naive Bayes
- Logistic Regression
- Random Forest
- Support Vector Machine

### Cài đặt
Sử dụng một IDE bất kỳ để thực thi chương trình (ví dụ VS Code)
- Bước 1: Cài đặt các thư viện Python: 
```
pip install -r requirements.txt
```
- Bước 2: Chạy file preprocess_data.ipynb để tiền xử lý dữ liệu
- Bước 3: Chạy file data_analysing.ipynb để phân tích dữ liệu
- Bước 4: Chạy file model_selection.ipynb để lựa chọn tham số, mô hình, huấn luyện, đánh giá
- Bước 5: Chạy chương trình demo app.py:
```
streamlit run app.py
```

