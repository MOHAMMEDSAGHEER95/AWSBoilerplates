from main import DynamoDBModel


def get_item(key):
    model = DynamoDBModel()
    item = model.get_item({'PK': key, 'SK': key})
    print(item)


def set_item(key, value):
    model = DynamoDBModel()
    item = {
        'PK': key,
        'SK': key,
        'name': value
    }
    model.put_item(item)
    print("added")



get_item('name')
set_item('name', 'lewis')