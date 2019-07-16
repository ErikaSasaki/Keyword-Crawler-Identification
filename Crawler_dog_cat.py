from icrawler.builtin import GoogleImageCrawler
from tqdm import tqdm

crawler_dog = GoogleImageCrawler(storage = {'root_dir': '/Users/erika.sasaki/Keyword-Crawler/dog_images'})
crawler_dog.crawl(keyword='dog', max_num=5000) 

crawler_cat = GoogleImageCrawler(storage = {'root_dir': '/Users/erika.sasaki/Keyword-Crawler/cat_images'})
crawler_cat.crawl(keyword='cat', max_num=5000) 

