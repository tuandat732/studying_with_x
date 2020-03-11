from pymongo import MongoClient

mongo_uri = 'mongodb+srv://admin1:admin1@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

dtb = client.luyende

# dtb_tintuc = client.trangchu

# tintuc_collection = dtb_tintuc['tintuc2']




# hoa_collection = dtb['hoa']

# ls_hoa=[
#     '1D',
# '2D',
# '3B',
# '4C',
# '5A',
# '6C',
# '7A',
# '8B',
# '9B',
# '10C',
# '11D',
# '12D',
# '13C',
# '14D',
# '15C',
# '16C',
# '17D',
# '18B',
# '19C',
# '20C',
# '21D',
# '22B',
# '23B',
# '24D',
# '25D',
# '26D',
# '27B',
# '28D',
# '29D',
# '30A',
# '31D',
# '32A',
# '33D',
# '34D',
# '35C',
# '36B',
# '37D',
# '38A',
# '39B',
# '40B']

# for i in range(len(ls_hoa)) :
#     k=len(ls_hoa[i])
#     link_hoa = {
#         'link':'../static/luyende/hoa/'+ ls_hoa[i] +'.jpeg',
#         'link1':'/static/luyende/hoa/'+ ls_hoa[i] +'.jpeg',
#         'cau': str(i + 1),
#         'dap_an': ls_hoa[i][len(ls_hoa[i])-1:len(ls_hoa[i])]
#     }
#     hoa_collection.insert_one(link_hoa)
#     print(link_hoa)


# # ///////////////////////////////////////////////////////////////////////////
# toan_collection = dtb['toan']

# ls_toan = [
    
# '1A',
# '2A',
# '3C',
# '4A',
# '5A',
# '6A',
# '7C',
# '8D',
# '9A',
# '10A',
# '11B',
# '12C',
# '13C',
# '14A',
# '15A',
# '16A',
# '17C',
# '18A',
# '19D',
# '20A',
# '21D',
# '22B',
# '23C',
# '24A',
# '25D',
# '26A',
# '27D',
# '28A',
# '29A',
# '30C',
# '31A',
# '32A',
# '33D',
# '34A',
# '35B',
# '36D',
# '37B',
# '38D',
# '39C',
# '40B',
# '41D',
# '42B',
# '43B',
# '44C',
# '45B',
# '46C',
# '47B',
# '48C',
# '49D',
# '50A'
# ]

# for i in range(len(ls_toan)) :
    
#     link_toan = {
#         'link':'../static/luyende/toan/'+ ls_toan[i] +'.jpeg',
#         'link1':'/static/luyende/toan/'+ ls_toan[i] +'.jpeg',
#         'cau': str(i + 1),
#         'dap_an': ls_toan[i][len(ls_toan[i])-1:len(ls_toan[i])]
#     }
#     toan_collection.insert_one(link_toan)
#     print(link_toan)

# //////////////////////////////////////////////////////////////////


# li_collection = dtb['li']
# ls_li = [
#     '1C',
#     '2D',
#     '3D',
#     '4B',
#     '5B',
#     '6C',
#     '7B',
#     '8D',
#     '9B',
#     '10C',
#     '11A',
#     '12A',
#     '13C',
#     '14A',
#     '15B',
#     '16B',
#     '17C',
#     '18D',
#     '19A',
#     '20D',
#     '21B',
#     '22A',
#     '23C',
#     '24C',
#     '25D',
#     '26C',
#     '27D',
#     '28D',
#     '29B',
#     '30A',
#     '31B',
#     '32C',
#     '33D',
#     '34C',
#     '35D',
#     '36B',
#     '37D',
#     '38D',
#     '39C',
#     '40B'
# ]

# for i in range(len(ls_li)) :
    
#     link_li = {
#         'link':'../static/luyende/li/'+ ls_li[i] +'.jpeg',
#         'link1':'/static/luyende/li/'+ ls_li[i] +'.jpeg',
#         'cau': str(i + 1),
#         'dap_an': ls_li[i][len(ls_li[i])-1:len(ls_li[i])]
#     }
#     li_collection.insert_one(link_li)
#     print(link_li)
# ////////////////////////////////////////////////////////////////////////////////
# anh_collection = dtb['anh']

# ls_anh = [
#     '1B',
#     '2C',
#     '3D',
#     '4B',
#     '5C',
#     '6A',
#     '7A',
#     '8D',
#     '9D',
#     '10C',
#     '11D',
#     '12C',
#     '13A',
#     '14B',
#     '15C',
#     '16C',
#     '17A',
#     '18A',
#     '19D',
#     '20A',
#     '21B',
#     '22C',
#     '23A',
#     '24D',
#     '25C',
#     '26D',
#     '27A',
#     '28D',
#     '28D',
#     '29C',
#     '30B',
#     '31B',
#     '32C',
#     '33C',
#     '34D',
#     '35C',
#     '36A',
#     '37C',
#     '38A',
#     '39B',
#     '40A',
#     '41D',
#     '42D',
#     '43D',
#     '44B',
#     '45B',
#     '46D',
#     '47B',
#     '48D',
#     '49A',
#     '50C'

# ]

# for i in range(len(ls_anh)) :
    
#     link_anh = {
#         'link':'../static/luyende/anh/'+ ls_anh[i] +'.jpeg',
#         'link1':'/static/luyende/anh/'+ ls_anh[i] +'.jpeg',
#         'cau': str(i + 1),
#         'dap_an': ls_anh[i][len(ls_anh[i])-1:len(ls_anh[i])]
#     }
#     anh_collection.insert_one(link_anh)
#     print(link_anh)

# //////////////////////////////////////////////////////////////////////////////

# sinh_collection = dtb['sinh']

# ls_sinh =[
#     '1A',
#     '2B',
#     '3C',
#     '4A',
#     '5C',
#     '6B',
#     '7C',
#     '8B',
#     '9B',
#     '10C',
#     '11D',
#     '12A',
#     '13D',
#     '14A',
#     '15B',
#     '16A',
#     '17B',
#     '18C',
#     '19A',
#     '20D',
#     '21D',
#     '22C',
#     '23B',
#     '24A',
#     '25B',
#     '26C',
#     '27D',
#     '28A',
#     '29C',
#     '30D',
#     '31A',
#     '32B',
#     '33A',
#     '34C',
#     '35A',
#     '36C',
#     '37B',
#     '38A',
#     '39B',
#     '40B'
#     ]

# for i in range(len(ls_sinh)) :
    
#     link_sinh = {
#         'link':'../static/luyende/sinh/'+ ls_sinh[i] +'.jpeg',
#         'link1':'/static/luyende/sinh/'+ ls_sinh[i] +'.jpeg',
#         'cau': str(i + 1),
        # 'dap_an': ls_sinh[i][len(ls_sinh[i])-1:len(ls_sinh[i])]
#     }
#     sinh_collection.insert_one(link_sinh)
#     print(link_sinh)


