def new(lbwiader=256):
    aMap=[]
    for i in range(0,lbwiader):
        aMap.append([])
    return aMap
    
def hash_key(aMap, key):
    return hash(key) % len(aMap)
    
def get_bucket(aMap, key):
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
    
def get_slot(aMap, key, default=None):
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k ,v
            
    return -1, key, default
    
    
