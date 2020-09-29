from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import resolve
from random import choice, shuffle, randint, seed
from urllib import parse
from .models import Question


default_kwargs = {
    "nav_styling": "background-color: #FFF;",
    "nav_text_styling": "color: #000;"
}

kwargs = {}

def get_qn(path_name, qn_seed, n=1):
    # Set seed
    seed(qn_seed)
    # Pick a random question
    qns = Question.objects.filter(page=path_name)
    for _ in range(n):
        qn = choice(qns)
    return qn

def shuffle_opt(qn, opt_seed):
    # Set seed
    seed(opt_seed)
    # shuffle options
    opt_l = [qn.opt1, qn.opt2, qn.opt3, qn.opt4]
    shuffle(opt_l)
    return opt_l

def preprocess(func):
    def process(request):
        # Get name by path, refer to .urls.py for more infomation
        path_name = resolve(request.path_info).url_name

        if request.method == "POST":
            # Get data in dict
            data = dict(parse.parse_qsl(request.body))

            if int(data[b'load_next']):
                kwargs.clear()
                kwargs["page"] = int(data[b'page']) + 1
                qn = get_qn(path_name, int(data[b'qn_seed']), kwargs["page"])
                kwargs["question"] = qn

                # Get a random seed (for opt)
                opt_seed = randint(1, 100000)
                kwargs['opt_seed'] = opt_seed
                opt_l = shuffle_opt(qn, opt_seed)
                qn.opt1, qn.opt2, qn.opt3, qn.opt4 = opt_l
                kwargs["qn_seed"] = int(data[b'qn_seed'])
            else:
                # Get question that is anwering now
                qn = Question.objects.filter(qn_id=data[b'qn_id'].decode(), page=path_name).first()
                # Get answer in text
                qn_ans = qn.__getattribute__(qn.answer)
                # Get index of answer after shuffling
                qn_ans_idx = shuffle_opt(qn, int(data[b'opt_seed'])).index(qn_ans)

                # Get index of user's answer
                mapping = ["opt1", "opt2", "opt3", "opt4"]
                user_ans_idx = mapping.index(data[b'user_opt'].decode())

                # Show message
                if qn_ans_idx == user_ans_idx:
                    messages.success(request, "Tahniah! Jawapan anda adalah betul!")
                else:
                    hint_ans = ["A", "B", "C", "D"]
                    messages.error(request, "Maaf, jawpan betul ialah {}.".format(hint_ans[qn_ans_idx]))

                # Disable buttons
                kwargs['{}_selected'.format(data[b'user_opt'].decode())] = 'checked'
                kwargs['status'] = 'disabled'
            kwargs["page_total"] = Question.objects.filter(page=path_name).count()
            return render(request, 'quiz/base.html', {**kwargs, **default_kwargs})
        else:
            kwargs.clear()
            # Get a random seed (for qn)
            qn_seed = randint(1, 100000)
            kwargs['qn_seed'] = qn_seed
            qn = get_qn(path_name, qn_seed)
            kwargs["question"] = qn

            # Get a random seed (for opt)
            opt_seed = randint(1, 100000)
            kwargs['opt_seed'] = opt_seed
            opt_l = shuffle_opt(qn, opt_seed)
            qn.opt1, qn.opt2, qn.opt3, qn.opt4 = opt_l

            kwargs["page"] = 1
            kwargs["page_total"] = Question.objects.filter(page=path_name).count()
            return func(request)
    return process

@preprocess
def comp_t(request):
    default_kwargs["quiz_name"] = "Pemikiran Komputasional"
    return render(request, 'quiz/base.html', {**kwargs, **default_kwargs})

@preprocess
def data_r(request):
    default_kwargs["quiz_name"] = "Perwakilan Data"
    return render(request, 'quiz/base.html', {**kwargs, **default_kwargs})

@preprocess
def algo(request):
    default_kwargs["quiz_name"] = "Algoritma"
    return render(request, 'quiz/base.html', {**kwargs, **default_kwargs})

@preprocess
def code(request):
    default_kwargs["quiz_name"] = "Kod Arahan"
    return render(request, 'quiz/base.html', {**kwargs, **default_kwargs})
