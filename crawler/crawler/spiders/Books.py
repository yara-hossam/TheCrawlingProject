import scrapy

class BooksSpider(scrapy.Spider):
    #this is the class responsible for the books website spider; setting the rules by which data will be retrieved.
    #the spider's name:
    name = 'books'
    #the required website:
    start_urls = ['https://edugeneral.org/blog/general-knowledge/famous-books-titles-and-authors-names/']

    def parse(self, response):
        #getting the table part in the body by using xpath
        for book in response.xpath('//tbody/tr'):
          #extracting the data in each row
          book_no=book.xpath('td[1]//text()').extract_first()
          book_title=book.xpath('td[2]//text()').extract_first()
          book_author=book.xpath('td[3]//text()').extract_first()
          #skipping the first row which has null elements
          if book_no and book_title and book_author:
            yield {
                'Book Number': book_no,
                'Book Title': book_title,
                'Book Author': book_author,
            }

