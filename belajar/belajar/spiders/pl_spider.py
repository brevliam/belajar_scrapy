import scrapy

class PLSpider(scrapy.Spider):
    name = 'premierleagueteamstadium'
    allowed_domains = ['premierleague.com']
    start_urls = ['https://www.premierleague.com/clubs']

    def parse(self, response):
        rows = response.css('li.club-card-wrapper')

        for row in rows:
            yield {
                'team' : row.css('h2.club-card__name::text').get(),
                'stadium' : row.css('span.club-card__stadium::text').get()
            }