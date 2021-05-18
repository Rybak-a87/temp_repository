# -----
# Вычисление цены с учетом налогов и маржы
# -----

data = {
    "products": [
        {
            "id": 1,
            "title": "Product 1",
            "net_cost": 100
        },
        {
            "id": 2,
            "title": "Product 2",
            "net_cost": 200
        }
    ],
    "tax": 0.1,
    "margin": 0.2
}


def create_new_price(data: dict) -> dict:
    new_price = {"products": []}
    for i in data["products"]:
        new_price["products"].append({
            "id": i["id"],
            "title": i["title"],
            # расчет новой стоимости продуктов с учетом налогов (в процентах) и желаемого маржи (в процентах)
            "price": round(
                ((i["net_cost"] / (1 - data["margin"])) * (1 + data["tax"])),
                2
            )
        })

    # расчет общей стоимости всего списка продуктов
    new_price["total_price"] = sum([v["price"] for v in new_price["products"]])
    return new_price


