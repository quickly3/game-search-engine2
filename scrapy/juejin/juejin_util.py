import datetime

def getJuejinDocByJsonItem(item):
    postUrl = "https://juejin.cn/post/"
    userUrl = "https://juejin.cn/user/"


    article_info = item['article_info']
    author_user_info = item['author_user_info']
    tags = item['tags']
    doc = {}
    doc['title'] = article_info['title']
    doc['url'] = postUrl+article_info['article_id']
    doc['summary'] = article_info['brief_content']
    doc['created_at'] = datetime.datetime.fromtimestamp(int(article_info['ctime']),None)
    doc['created_year'] = doc['created_at'].strftime("%Y")

    tagsArr = list(map(lambda x: x['tag_name'] , tags))

    doc['tag'] = tagsArr
    doc['source'] = 'juejin'
    doc['source_id'] = item['article_id']
    doc['stars'] = 0

    doc['author'] = author_user_info['user_name']
    doc['author_url'] = userUrl + author_user_info['user_id']
    
    doc['collect_count'] = article_info['collect_count']
    doc['comment_count'] = article_info['comment_count']
    doc['digg_count']    = article_info['digg_count']
    doc['view_count']    = article_info['view_count']
    doc['hot_index']     = article_info['hot_index']
    doc['user_index']    = article_info['user_index']
    
    doc['user_id']       = article_info['user_id']
    doc['user_index']    = article_info['user_index']
    doc['user_index']    = article_info['user_index']
    
    category = item['category']['category_name']
    doc['category'] = category

    return doc;
