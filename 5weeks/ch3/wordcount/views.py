from django.shortcuts import render
import operator

# Create your views here.

def home(request) : 
    return render(request, 'home.html')


def about(request) : 
    return render(request, 'about.html')

def count(request) : # request안에 들어온 데이터도 포함됨
    
    full_text = request.POST['fulltext'] # full_text = 지금함수에서 사용할 변수 / 'fulltext' = text데이터가져오기
    num_word = full_text.split()

    word_dictionary = {}

    for word in num_word : 
        if word in word_dictionary :
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1
    
    # 가장많이 나온 글자 추출
    sort_dic = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True) # 키순내림차순 정렬
    
    '''
    max_count = sort_dic[0][1]
    max_word = []

    for i in range(len(sort_dic)) :
        if sort_dic[i][1] != max_count:
            break

        max_word.append(sort_dic[i][0])
    
    max_ratio = int((max_count*len(max_word) / len(num_word)) * 100)

    # return render(request, 'count.html', {'text' : full_text, 'word' : len(num_word), 'dic' : word_dictionary.items, 'max_word' : max_word, 'max_count' : max_count, 'max_ratio' : max_ratio}) # text = count페이지 안에서 사용할 변수
    '''
    # print(sort_dic)

    # max_word, second_word, third_word = [[]] * 3 // 이렇게 하니까 max_word, second_word, third_word 가 모두 같은 List로 주소값이 같아짐 즉, max_word = second_word = third_word = []
    change_index = []
    max_word = []
    second_word = []
    third_word = []
    max_count, second_count, third_count = [0] * 3
    count = 0

    # 최고개수부터 변경시 그 부분의 index를 append
    for i in range(len(sort_dic)) :
        if sort_dic[i][1] != count:
            count = sort_dic[i][1]
            change_index.append(i)
            # print('index: ', change_index)
    # 단어 append 
        if len(change_index) == 1 :
            max_word.append(sort_dic[i][0])
            max_count = count # 입력한 텍스트에서 가장 많이 나온 단어의 수 // max_word의 개수가 아님
            # print('len(1):', max_word)
        elif len(change_index) == 2 :
            second_word.append(sort_dic[i][0])
            second_count = count
            # print('len(2):', max_word)
        elif len(change_index) == 3 :
            third_word.append(sort_dic[i][0])
            third_count = count
        else : # 4위에서 멈춤
            break

    print(max_word, second_word, third_word)
        
    max_ratio = round((max_count*len(max_word) / len(num_word)) * 100, 2)
    second_ratio = round((second_count*len(second_word) / len(num_word)) * 100, 2)
    third_ratio = round((third_count*len(third_word) / len(num_word)) * 100, 2)
    
    return render(request, 'count.html', {'text' : full_text, 'word' : len(num_word), 'dic' : word_dictionary.items,
    'max_word' : max_word, 'max_count' : max_count, 'max_ratio' : max_ratio,
    'second_word' : second_word, 'second_count' : second_count, 'second_ratio' : second_ratio,
    'third_word' : third_word, 'third_count' : third_count, 'third_ratio' : third_ratio}) # text = count페이지 안에서 사용할 변수
    # 보내줄 데이터를 딕셔너리형으로 줘야함

