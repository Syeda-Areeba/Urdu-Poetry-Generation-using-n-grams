import scrapy

class I210307urdupoemsspiderSpider(scrapy.Spider):
    name = 'I210307urdupoemsspider'
    allowed_domains = ['www.rekhta.org']
    
    start_urls = [
        'https://www.rekhta.org/poets/faiz-ahmad-faiz/ghazals?lang=ur',
        'https://www.rekhta.org/poets/aamir-azher-1/ghazals?lang=ur',
        'https://www.rekhta.org/poets/aanis-moin/ghazals?lang=ur',
        'https://www.rekhta.org/poets/erum-zehra/ghazals?lang=ur',
        'https://www.rekhta.org/poets/ashu-mishra/ghazals?lang=ur',
        'https://www.rekhta.org/poets/fazil-jamili/ghazals?lang=ur',
        'https://www.rekhta.org/poets/aabid-adeeb/ghazals?lang=ur',
        'https://www.rekhta.org/poets/khursheed-akbar/ghazals?lang=ur',
        'https://www.rekhta.org/poets/kaif-ahmed-siddiqui/ghazals?lang=ur',
        'https://www.rekhta.org/poets/zehra-alvi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/faheem-shanas-kazmi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/faisal-azeem/ghazals?lang=ur',
        'https://www.rekhta.org/poets/faisal-malik/ghazals?lang=ur',
        'https://www.rekhta.org/poets/vikram/ghazals?lang=ur',
        'https://www.rekhta.org/poets/nabeel-ahmad-nabeel/ghazals?lang=ur',
        'https://www.rekhta.org/poets/aabid-jafri/ghazals?lang=ur',
        'https://www.rekhta.org/poets/habab-hashmi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/m-i-zaahir/ghazals?lang=ur',
        'https://www.rekhta.org/poets/m-kothiyavi-rahi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/anwar-dehlvi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/taufeeq-hyderabadi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/hasrat-azimabadi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/shah-aasim/ghazals?lang=ur',
        'https://www.rekhta.org/poets/syed-nazeer-hasan-sakha-dehlavi/ghazals?lang=ur',
        'https://www.rekhta.org/poets/obaidullah-khan-mubtala/ghazals?lang=ur'
        ]
    
    def parse(self, response):
        # Extracting URLs of all poems written by the poet
        poem_links = response.css('div.contentListItems.nwPoetListBody a::attr(href)').extract()

        # Go to each poem link to extract it
        for poem_link in poem_links:
            yield scrapy.Request(response.urljoin(poem_link), callback=self.parse_poem)

    def parse_poem(self, response):

        poet_name = response.css('div.authorAddFavorite h2 a.ghazalAuthor::text').get()
        poem_name = response.xpath('//h1/text()').get()

        # Selecting all <p> elements within <div class="c">
        paragraph_elements = response.css('div.c > p')

        urdu_text_lines = []

        for paragraph in paragraph_elements:
            # Selecting all <span> elements within the <p> element containing urdu words of poem
            span_elements = paragraph.css('span[data-m]::text').extract()

            # Joining urdu text of all <span> elements
            paragraph_text = ''.join(span_elements).strip()

            urdu_text_lines.append(paragraph_text) # 1 verse is appended at a time

        # Saving data as JSON
        poem_data = {
            'poet_name': poet_name,
            'poem_name': poem_name,
            'poem_lines': urdu_text_lines[2:] # first 2 lines contain garbage (i.e. English text) so discarding them
        }

        yield poem_data