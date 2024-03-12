#-*- coding:utf-8 -*-
import os
from app.common.ip2Region import Ip2Region
#定义一个IP转化为地址的函数
def ip2addr(ip):
    ip_db_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        'static/ip2region/ip2region.db'
    )
    #实例化
    ip_to_addr = Ip2Region(ip_db_path)
    #地址信息
    addr_info = ip_to_addr.memorySearch(ip)
    return addr_info

if __name__ == '__main__':
    addr1 = ip2addr('39.156.66.18')
    print(addr1)  #查看ip地址
    print("城市ID：{},地址信息：{}".format
        (
        addr1['city_id'],
        addr1['region'].decode('utf-8')         #输出城市id地址信息
         )
    )

print("--------------------------")
addr2 = ip2addr('111.30.185.60')
print(addr2)
print("城市ID：{},地址信息：{}".format
    (
    addr2['city_id'],
    addr2['region'].decode('utf-8')
)
)