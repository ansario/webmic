from django.shortcuts import render
from microscope.models import Slide, Marker
import random
# Create your views here.
def home(request):
    slide = Slide.objects.get(pk=1)
    markers = Marker.objects.filter(slide=slide.pk)

    return render(request, 'microscope/detail.html', {"slide":slide, "markers":markers})

def slide(request, pk):
    return_dict = {}

    slide = Slide.objects.get(pk=pk)
    markers = Marker.objects.filter(slide=slide.pk)
    labels = request.GET.get('labels')
    magnification  = request.GET.get('magnification')
    quiz = request.GET.get('quiz')
    return_dict['slide'] = slide


    if labels:
        return_dict['markers'] = markers
    if quiz:



        quiz_markers = Marker.objects.order_by('?')[:3]

        return_dict['quiz_markers'] = quiz_markers
        pk_string = ""
        # random.shuffle(array)
        # return_dict['order'] = array
        # print return_dict['order']
        # print random.shuffle([1,2,3])
        array_of_titles = []
        for quiz in quiz_markers:
            pk_string = pk_string + str(quiz.pk)
            array_of_titles.append(quiz.text)

        return_dict['array_of_titles'] = array_of_titles

        return_dict['order'] = pk_string
    if magnification:
        return_dict['mag'] = True

    if request.method == "POST":


        a1 = request.POST.get('q1')
        a2 = request.POST.get('q2')
        a3 = request.POST.get('q3')
        answers = request.POST.get('pkstring')
        user_array = [a1, a2, a3]
        answer_array = []
        number_correct = 0
        for answer in answers:

            found = Marker.objects.get(pk=int(answer))
            answer_array.append(found.text)

        for i in xrange(len(user_array)):
            if user_array[i] == answer_array[i]:
                number_correct+=1

        return_dict['correct'] = number_correct
        print return_dict['correct']
        return render(request, 'microscope/detail.html', return_dict)
    return render(request, 'microscope/detail.html', return_dict)