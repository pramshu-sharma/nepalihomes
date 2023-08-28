from itemadapter import ItemAdapter


class ScrapperOnePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Remove spaces, clean price
        field_names = adapter.field_names()
        for fields in field_names:
            if fields == 'Price':
                price = adapter.get(fields)
                value = price.strip().replace('"', '')
                adapter['Price'] = value
            field = adapter.get(fields)
            value = field.strip()
            adapter[fields] = value

        # Replace Empty Seller Fields
        seller = adapter.get('Seller')
        value_0 = seller.replace('\xa0', 'NA')
        adapter['Seller'] = value_0

        # Clean Contact Number
        contact = adapter.get('Seller_Contact')
        value_1 = contact.replace('sms:', '').replace('+977 ', '').replace('+977', '')
        adapter['Seller_Contact'] = value_1

        # Clean Email
        email = adapter.get('Seller_Email')
        value_2 = email.replace('mailto:', '')
        adapter['Seller_Email'] = value_2

        # Clean Price Unit
        unit = adapter.get('Price_Unit')
        value_3 = unit.replace('/', '')
        adapter['Price_Unit'] = value_3

        # Clean Views
        views = adapter.get('Ad_Views')
        value_4 = views.replace(' views', '')
        adapter['Ad_Views'] = value_4

        return item
