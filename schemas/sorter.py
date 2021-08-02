def sorterEntity(item)->dict:
    return {
        "id":    str(item["_id"]),
        "name":  str(item["name"]),
        "data":  [str(item["data"])],
    }

def sortersEntity(entity)->list:
    return  [sorterEntity(item) for item in entity]