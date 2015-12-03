from elasticsearch import Elasticsearch

if __name__ == "__main__":
    ES = Elasticsearch(["{}:{}".format('192.168.99.100', 9200)])
    ad_mapping = {
        'ad': {"_timestamp": {
            "enabled": True
        },
            "date_detection": False,
            "properties": {
                "id": {
                    "type": "integer"
                },
                "subject": {
                    "type": "string"
                },
                "body": {
                    "type": "string"
                },
                "image": {
                    "type": "string",
                    "index": "not_analyzed"
                },
            }
        }
    }
    settings = {
        'settings': {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    }

    ES.indices.create(index='tags', body=settings)
    ES.indices.put_mapping(index='tags', doc_type='ad', body=ad_mapping)

    doc = {
        'subject': 'Vendo volvo v70',
        'body': 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/5/57/Volvo_V40_2012_ID42221_280212.jpg',
        'id': 1
    }

    res = ES.index('tags', 'ad', doc)
    print(res['created'])

    doc = {
        'subject': 'Vendo volvo v60',
        'body': 'Turbos nuevos, cartuchos, baratos, citroen, peugeot, fiat, nissan, volvo, renault, kia, seat, ford, mercedes, bmw, hyundai, mazda, saab, skoda, toyota, volkswagen, audi, alfa romeo, mitsubishi, opel, chevrolet, tdi, tdci, dci, cdi, jtd, hdi, tds. gtc, 1. 4, 1. 5, 1. 6, 1. 7, 1. 8, 1. 9, 2. 0, 2. 2, 2. 5, 3. 0. 70, 75, 80, 90, 105, 110, , 115, 120, 130, 140, 150, 220, 320, 325, 330, 525, 530, x3, x5, astra, c3, c4, c5, 206, 207, 307, 406, 407, picasso, xsara, partner, berlingo, passat, leon, ibiza, golf, polo, clio, megane, laguna, space, focus, a3, a4, a6, e36, e46, e39. envio gratuito. ',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/5/57/Volvo_V40_2012_ID42221_280212.jpg',
        'id': 2
    }

    res = ES.index('tags', 'ad', doc)
    print(res['created'])
