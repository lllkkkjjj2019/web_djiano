from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    """homepage of learning log"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    content = {'topics':topics}
    return render(request,'learning_logs/topics.html',content)

def topic(request,topic_id):
    """detail page special topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    content = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',content)
def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        # data not submitted:create a new form
        form = TopicForm()
    else:
        # post submit data:process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_Logs:topics')

    # Display a new form or indicate that the form data is invalid
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
def new_entry(request,topic_id):
    """add new entry"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # data not submitted:create a new form
        form = EntryForm()
    else:
        # post submit data:process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic =topic
            form.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    # Display a new form or indicate that the form data is invalid
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    """edit entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # data not submitted:create a new form
        form = EntryForm(instance=entry)
    else:
        # post submit data:process data
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)

    # Display a new form or indicate that the form data is invalid
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)