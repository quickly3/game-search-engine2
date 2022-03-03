scrapy crawl juejin_tag


python juejin_author_output.py

scrapy juejin_authors_crawl

nohup python3 -m juejin_tag_crawl >> juejin_tag_crawl.log 2>&1 &
nohup python3 -m juejin_post_crawl_by_author >> juejin_post_crawl_by_author.log 2>&1 &
nohup python3 -m juejin_authors_crawl >> juejin_authors_crawl.log 2>&1 &

tail -f juejin_tag_crawl.log
tail -f juejin_authors_crawl.log
tail -f juejin_post_crawl_by_author.log


nohup python3 -m follow_tag_list >> follow_tag_list.log 2>&1 &
tail -f follow_tag_list.log

nohup python3 -m followees >> followees.log 2>&1 &
tail -f followees.log


nohup python3 -m followers >> followers.log 2>&1 &
tail -f followers.log


nohup python3 -m tags >> tags.log 2>&1 &
tail -f tags.log
