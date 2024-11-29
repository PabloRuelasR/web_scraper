from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# Clase para almacenar los datos extraídos
class Sancion(Item):
    nombre_entidad = Field()
    nit_entidad = Field()
    nivel = Field()
    orden = Field()
    municipio = Field()
    numero_resolucion = Field()
    documento_contratista = Field()
    nombre_contratista = Field()
    numero_contrato = Field()
    valor_sancion = Field()
    fecha_publicacion = Field()
    fecha_firmeza = Field()
    fecha_cargue = Field()
    ruta_proceso = Field()

# Spider principal para extraer información
class MultasSpider(Spider):
    name = "MultasColombiaSpider"

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    # URL inicial
    start_urls = ['https://www.datos.gov.co/en/widgets/4n4q-k399']

    def parse(self, response):
        # Selector base de las filas de la tabla
        filas = response.xpath('//table/tbody/tr')

        for fila in filas:
            # Inicialización de ItemLoader con el selector de la fila actual
            item = ItemLoader(item=Sancion(), selector=fila)

            # Extracción de datos usando XPath para cada columna de la tabla
            item.add_xpath('nombre_entidad', './td[1]/text()')
            item.add_xpath('nit_entidad', './td[2]/text()')
            item.add_xpath('nivel', './td[3]/text()')
            item.add_xpath('orden', './td[4]/text()')
            item.add_xpath('municipio', './td[5]/text()')
            item.add_xpath('numero_resolucion', './td[6]/text()')
            item.add_xpath('documento_contratista', './td[7]/text()')
            item.add_xpath('nombre_contratista', './td[8]/text()')
            item.add_xpath('numero_contrato', './td[9]/text()')
            item.add_xpath('valor_sancion', './td[10]/text()')
            item.add_xpath('fecha_publicacion', './td[11]/text()')
            item.add_xpath('fecha_firmeza', './td[12]/text()')
            item.add_xpath('fecha_cargue', './td[13]/text()')
            item.add_xpath('ruta_proceso', './td[14]/a/@href')
            
            yield item.load_item()
