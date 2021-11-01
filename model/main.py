from os import name
import pickle
testset2 = {'cmt': '''
        Chiến thắng ngược 3-2 của Lào trước Mông Cổ chiều 31/10 giúp Thái Lan giành suất vào vòng chung kết U23 châu Á 2022.
        
    Loạt trận cuối bảng J vòng loại U23 châu Á diễn ra chiều 31/10 đem lại cảm xúc từ thất vọng đến hạnh phúc cho Thái Lan. Ở trận đấu sớm, Thái Lan bị Malaysia cầm hoà 0-0 và kết thúc vòng loại ở vị trí thứ hai bảng J, sau chính Malaysia.

    Điều đó có nghĩa Malaysia giành suất vào vòng chung kết, còn Thái Lan phải chờ Lào thắng Mông Cổ mới có hy vọng đi tiếp.
    '''}
def predict(text):
    with open('classifier_news.pkl', 'rb') as f:
        clf = pickle.load(f)

    with open('news_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    data = []
    # pre = preprocessing(testset['cmt'])
    data.append(text)
    newtest2 = vectorizer.transform(data)
    result = clf.predict(newtest2)
    return result
