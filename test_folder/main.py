from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['amazon-wish-list']
import datetime

wishing_list = [
    {
        "url": "https://www.amazon.co.uk/Svavo-Dispenser-Automatic-Sanitizer-Container/dp/B07QXS5N3C/?_encoding=UTF8&pd_rd_w=b9FuN&pf_rd_p=f08a84cd-720c-4620-9087-109830bbc621&pf_rd_r=XV0XXV5GNZ1R3N02HEXT&pd_rd_r=ab51388f-3ef8-4203-adfc-b744cc9b05f2&pd_rd_wg=znPiX&ref_=pd_gw_bmx_gp_ub4a7h0n&th=1",
        "to_buy_price": 9.99
    },
    {
        "url": "https://www.amazon.co.uk/AmazonBasics-Ironing-Board-H-Shaped-Large/dp/B0825K1JR9/ref=sr_1_1_sspa?c=ts&keywords=Ironing%2BAccessories&qid=1651342552&s=kitchen-appliances&sr=1-1-spons&ts_id=3576368031&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTSzMwRFMxTzFKRDAmZW5jcnlwdGVkSWQ9QTA5NzUyNDMxWVgxNDFKMjJNUVBJJmVuY3J5cHRlZEFkSWQ9QTA3MjMzMjMxQ1kwMVozQTI5NTJDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1",
        "to_buy_price":46
    }
]
#Add dict to a collection
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
#Add dict to database.
# for item in wishing_list:
#     items = db.items
#     item_id = items.insert_one(item).inserted_id

print(db.items.find_one({"url":"https://www.amazon.co.uk/Svavo-Dispenser-Automatic-Sanitizer-Container/dp/B07QXS5N3C/?_encoding=UTF8&pd_rd_w=b9FuN&pf_rd_p=f08a84cd-720c-4620-9087-109830bbc621&pf_rd_r=XV0XXV5GNZ1R3N02HEXT&pd_rd_r=ab51388f-3ef8-4203-adfc-b744cc9b05f2&pd_rd_wg=znPiX&ref_=pd_gw_bmx_gp_ub4a7h0n&th=1"}))
my_query = {"url":"https://www.amazon.co.uk/Svavo-Dispenser-Automatic-Sanitizer-Container/dp/B07QXS5N3C/?_encoding=UTF8&pd_rd_w=b9FuN&pf_rd_p=f08a84cd-720c-4620-9087-109830bbc621&pf_rd_r=XV0XXV5GNZ1R3N02HEXT&pd_rd_r=ab51388f-3ef8-4203-adfc-b744cc9b05f2&pd_rd_wg=znPiX&ref_=pd_gw_bmx_gp_ub4a7h0n&th=1"}
newvalues = {"$set":{"dear_price":515165}}

#Update database.
# db.items.update_one(my_query,newvalues)
