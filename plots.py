import plotly.graph_objects as go

from pua_tester import *

if __name__ == "__main__":
    suffixTrie = Trie()
    lst=(suffixTrie.sentiment('positive.txt','negative.txt','lemmatized.txt'))
    print(lst)
    sentiments=['positive','negative','neutral']
    fig=go.Figure([go.Bar(x=sentiments,y=lst)])
    fig.show()
    
    
    # data_canada = px.data.gapminder().query("country == 'Canada'")
    # fig = px.bar(data_canada, x='year', y='pop')
    # fig.show()

    

