#%%
import pandas as pd
import os
# import tensorflow
dataset_dir = '../../data/wechat_algo_data1'
feed_info_file_path = os.path.join(dataset_dir, 'feed_info.csv')
feed_embeddings_file_path = os.path.join(dataset_dir, 'feed_embeddings.csv')
user_action_file_path = os.path.join(dataset_dir, 'user_action.csv')
test_a_file_path = os.path.join(dataset_dir, 'test_a.csv')

#%%
if __name__ == "__main__":
    #%%
    feed_info_data = pd.read_csv(feed_info_file_path)
    feed_embeddings_data = pd.read_csv(feed_embeddings_file_path)
    user_action_data = pd.read_csv(user_action_file_path)
    test_a_data = pd.read_csv(test_a_file_path)
    #%%
    '''
    feed_info_data
    .__len__()        ->   106444
    .columns
        Index(['feedid', 'authorid', 'videoplayseconds', 'description', 'ocr', 'asr',
               'bgm_song_id', 'bgm_singer_id', 'manual_keyword_list',
               'machine_keyword_list', 'manual_tag_list', 'machine_tag_list',
               'description_char', 'ocr_char', 'asr_char'],
              dtype='object')
    
    feed_embeddings_data
    .__len__()  ->   106444
    .columns
        Index(['feedid', 'feed_embedding'], dtype='object')
        
    user_action_data
    .__len__()      ->  7317882
    .columns
        Index(['userid', 'feedid', 'date_', 'device', 'read_comment', 'comment',
               'like', 'play', 'stay', 'click_avatar', 'forward', 'follow',
               'favorite'],
              dtype='object')
    
    test_a_data.__len__()           ->   421985
    
    '''
    pd.set_option('display.max_columns', None)
    feed_info_data.describe()
    #%%
    feed_info_data.columns
    #%%
    feed_info_data.head()
    #%%
    user_action_columns = user_action_data.columns
    user_action_data.loc[user_action_data['userid'] == 8].__len__()






