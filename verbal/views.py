from django.shortcuts import render
from django.views import View
import json
from django.http import HttpResponseNotFound
# Create your views here.


class VerbalView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('./static/data3000.json') as f:
            self.data = json.load(f)

    def get(self, request, *args, **kwargs):
        if 'lid' in request.GET:
            lid = request.GET['lid']
            if 'uid' in request.GET:
                uid = request.GET['uid']
                word_list = self.data[lid][uid]
            else:
                word_list = []
                for unit in self.data[lid]:
                    word_list.extend(self.data[lid][unit])
            render_list = []
            cnt = 0
            for word_data in word_list:
                for word in word_data:
                    usages = word_data[word]
                    for usage in usages:
                        if 'eg' in usage and 'paraphrase' in usage:
                            flat_eg = ''
                            for eg in usage['eg']:
                                flat_eg += eg['eng'] +'\t' + eg['cn'] + '\n'
                            flat_eg = flat_eg.replace(word, '[____]')
                            flat_eg = flat_eg.replace(word.capitalize(), '[____]')
                            render_list.append({
                                'eg': flat_eg,
                                'word': word,
                                'paraphrase': usage['paraphrase'],
                                'hash':word + str(cnt)
                            })
                            cnt += 1
            list_id = lid
            unit_id = request.GET['uid'] if 'uid' in request.GET else 'all'
            return render(request, 'verbal.html', {'verbal_list':render_list, 'list_id':list_id, 'unit_id':unit_id})
        else:
            return HttpResponseNotFound()