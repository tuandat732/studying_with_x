from pymongo import MongoClient

mongo_uri = 'mongodb+srv://admin1:admin1@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

dtb_tailieu = client.tailieu

# tailieu_collection_toan = dtb_tailieu['toan']
# tailieu_collection_li = dtb_tailieu['li']
# tailieu_collection_van =dtb_tailieu['van']
# collection_tai_lieu_hoa = dtb_tailieu['hoa']
# collection_tai_lieu_sinh =dtb_tailieu['sinh']
# collection_tai_lieu_anh = dtb_tailieu['anh']


# list_toan =[
  
#     {
#         'document':'33 file casio giải nhanh giải tích',
#         'anh':'../static/tailieu/toán/1.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/1.jpeg.jpg',
#         'link':'https://drive.google.com/drive/folders/1OL3720UNBAQQICrQe7HJCxOkf31Z2uLl?fbclid=IwAR34z0vuHO8JjDZAN5gFNgFp0nzk5c2w0xWbmgPUtf3JzHeyPzdXKDomSmI'
#     },
#     {
#         'document':'bộ đề 8 điểm môn toán',
#         'anh':'../static/tailieu/toán/2.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/2.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1OmMLzyC97NpwPSaHBZbBUSw2KVmWOTWa/view?fbclid=IwAR1-2a1eOmHzRfvLfs35lhIAr4HlCjt7i-jRwU88whXBF5qpz5ngowvKhwg'
#     },
#     {
#         'document':'giải nhanh hình không gian bằng casio',
#         'anh':'../static/tailieu/toán/3.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/3.jpeg.jpg',
#         'link':'https://drive.google.com/drive/folders/1-7n-rhSVN92BPawXt7O8twJl8JIQkSr4?fbclid=IwAR3BvdAh3VzoILUBhVscBxW_oFDCyOJBQyRvfBnXGQnaE-8R-ekfkcqIrcM'
#     },
#       {
#         'document':'110 bài toán ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số',
#         'anh':'../static/tailieu/toán/4.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/4.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/18WXeBLFD1ogMki1qBGxVZTShgX0cAufd/view'
#     },
#       {
#         'document':'vận dụng cao đạo hàm và ứng dụng của đạo hàm',
#         'anh':'../static/tailieu/toán/5.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/5.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/11FX5Zkz9J53jsBPLSITGAt2xfdIFnVoH/view'
#     },
#       {
#         'document':'57 ví dụ lúy thừa-mũ-logarit',
#         'anh':'../static/tailieu/toán/6.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/6.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1a7BWgB4iZk14aErKRPHYl8rF_XxHUI1H/view'
#     },
#       {
#         'document':'phân dạng và bài tập trắc nghiệm-mũ-logarit',
#         'anh':'../static/tailieu/toán/7.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/7.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1UHMf6zRDUsVA-VYb9R_Mk6NsOqwD4rhZ/view'
#     },
#       {
#         'document':'chuyên đề nguyên hàm, tích phân và ứng dụng',
#         'anh':'../static/tailieu/toán/8.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/8.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1XaGY5ZlHkVdexbW41x8rUJsRYrlByBFK/view'
#     },
#       {
#         'document':'áp dụng bất đẳng thức tích phân giải các bài toán tích phân nâng cao',
#         'anh':'../static/tailieu/toán/9.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/9.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1X7r-H8LDCNj1hHWFGfbiCnE0D4v1yQOd/view'
#     },
#       {
#         'document':'tổng ôn cực trị số phức',
#         'anh':'../static/tailieu/toán/10.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/10.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1IySJyX1ydXcRQHZTBN24nsLg4G822DCf/view'
#     },
#       {
#         'document':'bài tập trắc nghiệm số phức',
#         'anh':'../static/tailieu/toán/11.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/11.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1tHXLVR4x1MXzVeIduhXDbTngdlpugG5B/view'
#     },
#      {
#         'document':'kĩ thuật tư duy và giải nhanh hình học không gian',
#         'anh':'../static/tailieu/toán/12.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/12.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1XWI1yaa2LYL_1nJQGlwcbgxzNcNf2Xr7/view'
#     },
#      {
#         'document':'chuyên đề mặt nón-mặt trụ-mặt cầu',
#         'anh':'../static/tailieu/toán/13.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/13.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1mHU1u2AwWjkyErnLBErqtpqcFy1QkWG4/view'
#     },
#      {
#         'document':'phương pháp tọa độ hóa hình không gian',
#         'anh':'../static/tailieu/toán/14.jpeg.jpg',
#         'anh1':'/static/tailieu/toán/14.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1oSg5OdnL3irFF6RJ3-jInco2PCWC3QGh/view'
#     },

# ]

# list_li = [
#      {
#         'document':'500 bài tập trắc nghiệm vật lý',
#         'anh':'../static/tailieu/lí/1.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/1.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1MpIFjkd_FF0Cx55YTTQ7lEHOlqjFlbuK/view'
#      },
#       {
#         'document':'công phá vật lý',
#         'anh':'../static/tailieu/lí/2.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/2.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1rv76gEKH0em05Hb8gE8xHGPom4_AleOq/view'
#      },
#      {
#         'document':'20 đề thi thử vật lý 2017',
#         'anh':'../static/tailieu/lí/3.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/3.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1csaXl6mqlVMxCjJE0poGodK2JtRhpc2d/view'
#      },
#      {
#         'document':'Công phá đề thi THPT quốc gia 2018 vật lý',
#         'anh':'../static/tailieu/lí/4.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/4.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1n3rfxBV85wMy5Nrp7vrFwxlEfOr3xbvc/view'
#      },
#      {
#         'document':'Mega luyện đề THPT quốc gia 2018 vật lý',
#         'anh':'../static/tailieu/lí/5.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/5.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1jwkE8g_LuaHBnWHsBB1LpBv-AXlf9x80/view'
#      },
#      {
#         'document':'Hướng giải nhanh bộ đề luyện thi THPT quốc gia vật lý',
#         'anh':'../static/tailieu/lí/6.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/6.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/161hkWNnNtI1T6RPwTUkLaCDiNKuueCKQ/view'
#      },
#      {
#         'document':'Kiến thức vật lý đầy đủ',
#         'anh':'../static/tailieu/lí/7.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/7.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1QaR2Po9WLrpk9aw7p8P3ilnmYR2TDDE4/view'
#      },
#       {
#         'document':'Bộ 10 đề thi thử vật lý từ các trường 2018',
#         'anh':'../static/tailieu/lí/8.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/8.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1CZ3coYHznxHY1NUuIxg7QvPUzJ1mWLaN/view'
#      },
#       {
#         'document':'casio giải toán vật lý',
#         'anh':'../static/tailieu/lí/9.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/9.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/181JPZ6h4n3aWzOYxCuX5u0B18AjZFti2/view'
#      },
#       {
#         'document':'tài liệu lí thuyết và công thức giải nhanh vật lý',
#         'anh':'../static/tailieu/lí/10.jpeg.jpg',
#         'anh1':'/static/tailieu/lí/10.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/0B9GvBjf6V7-MTlVWRlBuZHpPZnc/view'
#       }
# ]

# list_van =[
#     {
#         'document':'Kiến thức trọng tâm ngữ văn 12',
#         'anh':'../static/tailieu/văn/1.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/1.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1JxGj16ZsDL7WjXeo0bHY8HUtJ18SPLBJ/edit?fbclid=IwAR3ts2i6y864UTkKBbDza9p_Q_g2F2Gss_My1B-nLZ9E_UNg_obXhgOT2BA'
#     },
#      {
#         'document':'Tuyển tập 101 đề đọc hiểu ngữ văn có đáp án',
#         'anh':'../static/tailieu/văn/2.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/2.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1cKOgKyosQQocoGxGHqZZq9BPRlNXTRXn/view?fbclid=IwAR21xAjWX4UbTGlqGRrrSkx5ECAZ1PiWzrMS8jChTFSV57uDi4tFb5HdK_Q'
#     },
#      {
#         'document':'tổng hợp 20 đề và đáp án chi tiết môn ngữ văn',
#         'anh':'../static/tailieu/văn/3.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/3.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1QT9fOYxZ_eOQxnZWXUiUiDQHbJD5h_sd/view'
#     },
#      {
#         'document':'tài liệu ôn thi cơ bản môn ngữ văn',
#         'anh':'../static/tailieu/văn/4.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/4.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1_oe3CHGLzj84n-kGyN_SoWv_D5ovpwyF/view'
#     },
#      {
#         'document':'Kiến thức trọng tâm ngữ văn 12 THPT',
#         'anh':'../static/tailieu/văn/5.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/5.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1vW4YyI4NqAL2sOT3gtt_7WgF35dqJf_g/view'
#     },
#      {
#         'document':'Sơ đồ tư duy ngữ văn 12',
#         'anh':'../static/tailieu/văn/6.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/6.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/0B9GvBjf6V7-MRjczai1lanFtT2s/view'
#     },
#      {
#         'document':'7 phương pháp viết hay nghị luận xã hội',
#         'anh':'../static/tailieu/văn/7.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/7.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/0B9GvBjf6V7-Mc2xubTVaRDVXZTQ/view'
#     },
#      {
#         'document':'tài liệu chuyên đề thơ',
#         'anh':'../static/tailieu/văn/8.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/8.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1kV9ndFMA88xxGCwev5gYGSuyJ2xbb6My/view'
#     },
#      {
#         'document':'Chinh phục năng lực đọc hiểu và làm văn',
#         'anh':'../static/tailieu/văn/9.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/9.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1ITpVr_6tTScLRuNnkvOWjZ51aGTO3J4r/view'
#     },
#      {
#         'document':'Phân tích tác phẩm văn học 12',
#         'anh':'../static/tailieu/văn/10.jpeg.jpg',
#         'anh1':'/static/tailieu/văn/10.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/0B9GvBjf6V7-MWEZmQnFuclQ4WFk/view'
#     },


# ]

# list_hoa =[
#     {
#         'document':'Hóa hữu cơ 12',
#         'anh':'../static/tailieu/hóa/1.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/1.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1EjePMnSAXKDz16nll4cOx7mEMlHqf4rP/view'
#     },
#     {
#         'document':'Hóa vô cơ 12',
#         'anh':'../static/tailieu/hóa/2.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/2.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1EjePMnSAXKDz16nll4cOx7mEMlHqf4rP/view'
#     },
#     {
#         'document':'Hóa hữu cơ 11',
#         'anh':'../static/tailieu/hóa/3.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/3.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/18S18bnfBsAicN0hScNsSmdN_ngvZdFWY/view'
#     },
#     {
#         'document':'Tổng hợp chuyên đề hóa học 11 ',
#         'anh':'../static/tailieu/hóa/4.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/4.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/19uQSvJV0M_PVeDjrhwkvu8HKF1Dm3GN6/view'
#     },
#     {
#         'document':'Các chuyên đề hóa học 10',
#         'anh':'../static/tailieu/hóa/5.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/5.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1O4ZpOLp4KkHA6-9YzHLUNIZF37WwESl3/view'
#     },
#     {
#         'document':'Sách nhớ kiến thức cơ bản hóa 10',
#         'anh':'../static/tailieu/hóa/6.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/6.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1agBQC9tCe2GwT08qulmFfOb9foctTk7Z/view'
#     },
#     {
#         'document':'30 ngày làm chủ hóa hữu cơ',
#         'anh':'../static/tailieu/hóa/7.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/7.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1qH6s4IY_04MvJy_oHhckGQ_puxIu_zu-/view'
#     },
#     {
#         'document':'30 ngày làm chủ hóa vô cơ',
#         'anh':'../static/tailieu/hóa/8.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/8.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1-kpetKzQDsaeIsM0GiZaLoECiBTMTcQ7/view'
#     },
#     {
#         'document':'sách hóa 12',
#         'anh':'../static/tailieu/hóa/9.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/9.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1VADIaxRAjnXVMaezDWDBDlFsOHFe6at5/view'
#     },
#     {
#         'document':'Tuyển tập 50 đề học sinh giỏi hóa',
#         'anh':'../static/tailieu/hóa/10.jpeg.jpg',
#         'anh1':'/static/tailieu/hóa/10.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/124UDjNxOd5bchOR55uFY03iKEiMKHV_X/view'
#     }
# ]

# list_sinh =[
#     {
#         'document':'Mega luyện đề thi thpt sinh',
#         'anh':'../static/tailieu/sinh/1.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/1.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1joQJIrBw6OJbOzKq-cuZ8LaEJyyErA7t/view'
#     },
#     {
#         'document':'Sách công phá sinh 1',
#         'anh':'../static/tailieu/sinh/2.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/2.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1Y4HQ4BqtlU4d0vjPziyNi3MDYbj0NJIN/view'
#     },
#     {
#         'document':'Sách công phá sinh 2',
#         'anh':'../static/tailieu/sinh/3.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/3.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1I-UugDaSPfcHFRfywpTfvE7xi-y8LxrK/view'
#     },
#     {
#         'document':'Bộ đề tinh túy sinh học thpt 2017',
#         'anh':'../static/tailieu/sinh/4.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/4.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1QnbNjVSuq0awx9Y0zkMF5zLH7JiDe3Zv/view'
#     },
#     {
#         'document':'BẢO BỐI CHINH PHỤC ĐỀ THI THPT QG SINH 2018 THẦY THỊNH NAM',
#         'anh':'../static/tailieu/sinh/5.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/5.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1aDq-hjrCt-czb_cVkARDTzVqO4SI0Gf0/view'
#     },
#     {
#         'document':'GIẢI TOÁN SINH HỌC TRÊN MÁY TÍNH CASIO VÀ VINACAL',
#         'anh':'../static/tailieu/sinh/6.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/6.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/13GICHu985xlFDgDquiAgMTmCKb1B26rq/view'
#     },
#     {
#         'document':'GIẢI TOÁN SINH HỌC TRÊN MÁY TÍNH CASIO VÀ VINACAL',
#         'anh':'../static/tailieu/sinh/7.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/7.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1tbgPAppqnDz8TX9wbtHMYL4LqSKJbpHo/view'
#     },
#     {
#         'document':'Tóm tắt công thức sinh 12',
#         'anh':'../static/tailieu/sinh/8.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/8.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1DFvvxYUI0GK1TnxllUvFupHVsILasEKt/view'
#     },
#     {
#         'document':'Tổng hợp lí thuyết sinh 11',
#         'anh':'../static/tailieu/sinh/9.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/9.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/0B9GvBjf6V7-McWxCM012S0M5Z28/view'
#     },
#     {
#         'document':'NHỮNG CÂU HỎI LÝ THUYẾT MÔN SINH XUẤT HIỆN TRONG ĐỀ THI ĐẠI HỌC VÀ ĐÁP ÁN',
#         'anh':'../static/tailieu/sinh/10.jpeg.jpg',
#         'anh1':'/static/tailieu/sinh/10.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1XXWTZhg4oxLjZwaJUtCMGnjHDB19SVn3/view'
#     }
# ]



# list_anh =[
#     {
#         'document':'Bộ tinh túy đề thi anh thpt 2017',
#         'anh':'../static/tailieu/anh/1.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/1.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1PewREGBPbUUHniFcwt-jmFeJjEhDSxPr/view'
#     },
#     {
#         'document':'100 câu thi thpt tiếng anh 2019',
#         'anh':'../static/tailieu/anh/2.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/2.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1yYrfehVWqQGPPpZu9dPPvfPihah8uDsm/view'
#     },
#     {
#         'document':'Tự đột phá phát âm và trọng âm',
#         'anh':'../static/tailieu/anh/3.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/3.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1WLNQ8ujC9uyxb7UNd0skqWiJaH3uxKxQ/view'
#     },
#     {
#         'document':'Sách luyện siêu trí nhớ T.A',
#         'anh':'../static/tailieu/anh/4.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/4.jpeg.jpg',
#         'link':'https://drive.google.com/drive/folders/1RqVaoJfIZS13DjaDADkUdMWAXdNmqxQ0'
#     },
#     {
#         'document':'Bí kíp nhớ từ vựng siêu tốc',
#         'anh':'../static/tailieu/anh/5.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/5.jpeg.jpg',
#         'link':'https://drive.google.com/drive/folders/1m6gqHmY6v_DfU5xGHlAiS3de0oz8twn1'
#     },
#     {
#         'document':'Luyện nói tiếng anh như người bản xứ',
#         'anh':'../static/tailieu/anh/6.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/6.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/10SiTpTOwuemfY5pqFkLIczovGqjr0YIn/view'
#     },
#     {
#         'document':'Rèn luyện kĩ năng đọc hiểu',
#         'anh':'../static/tailieu/anh/7.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/7.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1H39Tp6n5QAYLlwdXLIR7P8Jx3ZmAS7bk/view'
#     },
#     {
#         'document':'Ngữ pháp tiếng anh cơ bản',
#         'anh':'../static/tailieu/anh/8.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/8.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1GGJfT6SxzeicCdHoUZsWck_uZtWwpQMT/view'
#     },
#     {
#         'document':'Tự đột phá ngữ pháp tiếng anh',
#         'anh':'../static/tailieu/anh/9.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/9.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1uXQc_uuZxvk4g6MjdrZoHz-I2_JNkKCm/view'
#     },
#     {
#         'document':'100% trọng tâm ôn tiếng anh',
#         'anh':'../static/tailieu/anh/10.jpeg.jpg',
#         'anh1':'/static/tailieu/anh/10.jpeg.jpg',
#         'link':'https://drive.google.com/file/d/1TSX0HwHuj3tLlhigie6nYLBSCDPniPWn/view'
#     },
# ]



# for a in list_hoa :
#     collection_tai_lieu_hoa.insert_one(a)

# for b in list_sinh:
#     collection_tai_lieu_sinh.insert_one(b)

# for c in list_anh :
#     collection_tai_lieu_anh.insert_one(c)


# for i in list_toan:
#     tailieu_collection_toan.insert_one(i)
#     print(i)

# for j in list_li:
#     tailieu_collection_li.insert_one(j)
#     print(j)

# for k in list_van:
#     tailieu_collection_van.insert_one(k)
#     print(k)