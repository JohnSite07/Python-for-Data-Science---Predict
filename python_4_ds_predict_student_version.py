### Function 1: Metric Dictionary

def dictionary_of_metrics(items):
    # your code here
    dic = {'mean': round(np.mean(items),2), 'median': round(np.median(items),2),
           'var': round(np.var(items,ddof=1),2), 'std': round(np.std(items,ddof=1),2),
           'min': round(np.min(items),2), 'max': round(np.max(items),2)}
    return dic


### Function 2: Five Number Summary

def five_num_summary(items):
    # your code here
    dic = {'max': round(np.max(items),2), 
           'median': round(np.median(items),2),
           'min': round(np.min(items),2),
           'q1': round(np.quantile(items, 1/4),2),
           'q3': round(np.quantile(items, 3/4),2)
           }
    return dic


### Function 3: Date Parser

def date_parser(dates):
    # your code here
    li = []
    for time in range(0,len(dates),3):
        for date in dates:
            li.append(date[:10])
    return li


### Function 4: Municipality & Hashtag Detector

def extract_municipality_hashtags(df):
    # your code here
    
    def get_municipality(df):
        
        def municipality(df):
            tw_list = df['Tweets']

            sub_lists = []
            for sentence in tw_list:
                sub_lists.append(sentence.split(" "))

            vide = []
            diks = mun_dict.keys()
            for sublist in sub_lists:
                vide2 = []
                for word in sublist:
                    for val in diks:
                        if word == val :
                            word = mun_dict[val]
                            vide2.append(word)
                vide.append(vide2)

            df['municipality'] = pd.DataFrame(vide)
    
            return df

        Tweets_df = municipality(df)

        def to_nan(x):
            if x == None:
                x = np.nan
            return x
    
        Tweets_df['municipality'] = Tweets_df['municipality'].agg(to_nan)

        return Tweets_df
    
    return get_municipality(df)


### Function 5: Number of Tweets per Day

 def number_of_tweets_per_day(df):
    # your code here
    def get_date(Date):
        date = Date[0:10]
        return date

    df['Date'] = df['Date'].agg(get_date)
    
    tw_grouped = df.groupby('Date')['Tweets']
    tw_group_date = pd.DataFrame(tw_grouped, columns = ['Date', 'Tweets'])
    
    def get_tweets_lenght(tweets):
        tweets_lenght = len(tweets)
        return tweets_lenght
    
    tw_group_date['Tweets'] = tw_group_date['Tweets'].agg(get_tweets_lenght)
    
    return tw_group_date.set_index('Date')


### Function 6: Word Splitter

def word_splitter(df):
    # your code here
    def splitting (tweet):
        tweet_low = tweet.lower()
        splet_tweet = tweet_low.split(" ")
        return splet_tweet
    
    df['Split Tweets'] = df['Tweets'].agg(splitting)
    
    return df

### Function 7: Stop Words

def stop_words_remover(df):
    # your code here
    def splitting (tweet):
        splet_tweet = tweet.lower().split(" ")
        return splet_tweet
    
    df['Without Stop Words'] = df['Tweets'].agg(splitting)
    
    def remove_stop_words(Tweets):
        stop_word_removed = []
        for word in Tweets:
            if stop_words_dict['stopwords'].count(word) == 0:
                stop_word_removed.append(word)
        return stop_word_removed
    
    df['Without Stop Words']  = df['Without Stop Words'].agg(remove_stop_words)
    
    return df
