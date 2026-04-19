# Message Processor for Redis/Elasticsearch
import redis
from elasticsearch import Elasticsearch

redis_client = redis.Redis(host='localhost', port=6379, db=0)
elastic_client = Elasticsearch(['http://localhost:9200'])

def process_message(message):
    # Process and index the message
    redis_client.lpush('messages', message)
    elastic_client.index(index='telegram_messages', body={'message': message})