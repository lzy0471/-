from pymongo import MongoClient

# MongoDB配置
mongodb_configs = {
    'db_host': '127.0.0.1',
    'db_port': 27017
}

# 连接MongoDB
client = MongoClient(host=mongodb_configs['db_host'], port=mongodb_configs['db_port'])

# 列出所有数据库的名称
dbs = client.list_database_names()
print(dbs)
