from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from student.models import Student
from .models import Course, Lesson, Sentence, UserProgress
import pandas as pd
from django.core.files.storage import FileSystemStorage


def english_course(request):
    course = get_object_or_404(Course, id=1)
    lessons = course.lessons.all()

    if request.method == 'POST':
        lesson_number = request.POST.get('lesson_number')
        title = request.POST.get('title')

        content_file = request.FILES.get('content_file')
        if content_file:
            fs = FileSystemStorage()
            filename = fs.save(content_file.name, content_file)
            content = content_file.name
        else:
            content = ''

        Lesson.objects.create(
            course=course,
            lesson_number=lesson_number,
            title=title,
            content=content
        )

        return redirect('english_course')

    return render(request, 'english_course.html', {'course': course, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    return render(request, 'lesson_detail.html', {"lesson_id": lesson_id})



def save_progress(request, lesson_id):
    if request.method == 'POST':
        lesson = Lesson.objects.get(id=lesson_id)
        
        # Получаем или создаем прогресс пользователя для данного урока
        user_progress, created = UserProgress.objects.get_or_create(
            user=request.user, 
            lesson=lesson
        )

        progress_tasks = request.POST.get('progress_tasks', '').split(',')
        progress_indicators = request.POST.get('progress_indicators', '').split(',')

        df = pd.read_excel(lesson.content)
        df.columns = ['English', 'Ukrainian']
        assignments = df.to_dict(orient='records')

        i = 0
        for task, indicator in zip(progress_tasks, progress_indicators):
            is_correct = (indicator == '1')
            
            df = pd.read_excel(lesson.content)
            df.columns = ['English', 'Ukrainian']
            assignments = df.to_dict(orient='records') 
            correct_sentence = assignments[i]['English']
            
            # print(task)
            if task != "":
                
                sentence, created = Sentence.objects.update_or_create(
                    lesson=lesson,
                    assignment_id=i,
                    user=request.user,
                    defaults={
                        'sentence': task,
                        'correct_sentence': correct_sentence,
                        'is_correct': is_correct
                    }
                )
            i += 1
            user_progress.sentences.add(sentence)

        user_progress.completed = all(indicator == '1' for indicator in progress_indicators)
        user_progress.save()

        return JsonResponse({'success': True})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_assignments(request, lesson_id):

    lesson = get_object_or_404(Lesson, id=lesson_id)
    sentences = Sentence.objects.filter(lesson=lesson, user=request.user)
    
    tasks = []
    
    for sentence in sentences: 
        tasks.append({
            'sentence': sentence.sentence,
            'is_correct': 1 if sentence.is_correct else 0,
            'assignment_id': sentence.assignment_id,
        })

    df = pd.read_excel(lesson.content)

    df.columns = ['English', 'Ukrainian']
    
    assignments = df.to_dict(orient='records') # assignments = {'English': 'English', 'Ukrainian': 'Ukrainian'}
    # task = {
    #     'type': 'task',
    #     'content': 'Translate the following sentences to Ukrainian:',  
    # }
    print(tasks)
    return JsonResponse({
        'assignments': assignments,
        'tasks': tasks
    })





def course_main(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def load_lessons(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all().values('id', 'lesson_number', 'title', 'content')
    return JsonResponse(list(lessons), safe=False)

def load_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    lesson_data = {
        'id': lesson.id,
        'lesson_number': lesson.lesson_number,
        'title': lesson.title,
        'content': lesson.content,
    }
    return JsonResponse(lesson_data)

def add_lesson(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        lesson_number = request.POST.get('lesson_number')
        title = request.POST.get('title')
        content = request.POST.get('content')
        course = get_object_or_404(Course, id=course_id)
        lesson = Lesson.objects.create(course=course, lesson_number=lesson_number, title=title, content=content)
        return JsonResponse({'success': True})

def update_lesson(request):
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')      
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson.lesson_number = request.POST.get('lesson_number')
        lesson.title = request.POST.get('title')
        lesson.content = request.POST.get('content')
        lesson.save()
        return JsonResponse({'success': True})






# def get_assignments(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     df = pd.read_excel(lesson.content)
#     df.columns = ['English', 'Ukrainian']
    
#     student = request.user  
#     assignments = df.to_dict(orient='records')

#     student_assignments = Assignment.objects.filter(lesson=lesson, student=student)
#     assignments_with_answers = []

#     for i, assignment in enumerate(assignments):

#         student_assignment = student_assignments[i] if i < len(student_assignments) else None
        
#         assignments_with_answers.append({
#             'English': assignment['English'],
#             'Ukrainian': assignment['Ukrainian'],
#             'user_answer': student_assignment.user_answer if student_assignment else '',
#         })

#     return JsonResponse({'assignments': assignments_with_answers})
