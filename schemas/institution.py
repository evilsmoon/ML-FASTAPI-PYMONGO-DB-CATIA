
def institutionEntity(item)->dict:
    return {
        "id": str(item["_id"]),
        "cod": item["cod"],
        "name": item["name"]
    }

def institutionsEntity(entity)->list:
    return  [institutionEntity(item) for item in entity]