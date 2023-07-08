import time

from chat.forms import ChatDataForm, LoginForm, SignupForm
from chat.models import (
    Channel,
    ChatData,
    Friend,
    FriendRequest,
    MessageTracker,
    UserData,
)
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render


def is_request_sent(name_and_request, name_and_relations):
    if name_and_request in name_and_relations:
        return True
    return False


def is_friend(name_and_friend, name_and_friends):
    if name_and_friend in name_and_friends:
        return True
    return False


def sent(user):

    name_and_relations = [
        {"name": relation.name, "Request": relation.Request}
        for relation in FriendRequest.objects.all()
    ]
    name_and_friends = [
        {"name": i.name, "friend": i.friend_name} for i in Friend.objects.all()
    ]

    request_sent_details_list = [
        {
            "name": rel.name,
            "image": rel.image,
            "sent": is_request_sent(
                {"name": rel.name, "Request": user}, name_and_relations
            ),
            "color": rel.color,
            "friend": is_friend({"name": user, "friend": rel.name}, name_and_friends),
        }
        for rel in UserData.objects.all()
    ]
    return request_sent_details_list


def request_data(request):
    current_usr = request.session["name"]
    delete_friend_requests(current_usr)
    all_requests_objects_for_curr_usr, unique_requests = [], []
    for relation_of_curr_usr in FriendRequest.objects.filter(name=current_usr):
        requested_person_info = UserData.objects.filter(
            name=relation_of_curr_usr.Request
        )
        info_obj = dict()
        for info in requested_person_info:
            info_obj = {
                "name": relation_of_curr_usr.Request,
                "image": info.image,
                "color": info.color,
            }
        if info_obj["name"] not in unique_requests:
            unique_requests.append(info_obj["name"])
            all_requests_objects_for_curr_usr.insert(0, info_obj)
    return all_requests_objects_for_curr_usr, len(unique_requests)


def requests(request):
    obj = request_data(request)[0]
    return render(request, "requests.html", {"obj": obj})


def accept_request(request, name):
    def make_friends(usr1, usr2):
        friend_ = Friend()
        friend_.name = usr1
        friend_.friend_name = usr2
        friend_.save()

    requesting_person = name
    curr_usr = request.session["name"]
    make_friends(curr_usr, requesting_person)
    make_friends(requesting_person, curr_usr)
    recieved_request = FriendRequest.objects.filter(Request=requesting_person)
    recieved_request.delete()
    create_channel(curr_usr, name)
    return redirect("/friends/")


def create_channel(name, friend):
    channel_usr = Channel()
    channel_usr.name = name
    channel_usr.friend_name = friend
    channel_created_at = (
        time.asctime(time.localtime(time.time())).replace(" ", "-").replace(":", "-")
    )
    channel_usr.channel_name = channel_created_at
    channel_usr.save()


def get_channel(name, friend):
    try:
        channel_obj = Channel.objects.get(name=name, friend_name=friend)
    except:
        channel_obj = Channel.objects.get(name=friend, friend_name=name)
    return channel_obj.channel_name


def video_call(request, name):
    channel = get_channel(request.session["name"], name)
    return render(request, "video_chat_room.html", {"channel": channel, "name": name})


def create_chats_order_trackers():
    try:
        try:
            MessageTracker.objects.get(name="track")
        except:
            track = MessageTracker(name="track")
            track.num = 0
            track.save()
    except Exception as e:
        raise ValueError(
            f"unable to start the app. track can't be initialised in records model : {e}"
        )


def start(request):
    create_chats_order_trackers()
    try:
        if request.session["name"]:
            return redirect("/all_users/")
    except:
        return render(request, "login.html")
    return render(request, "login.html")


def send_request(request, name):
    friend_request_reciever = name
    friend_request = FriendRequest()
    friend_request.name = friend_request_reciever
    current_usr_who_made_the_request = request.session["name"]
    friend_request.Request = current_usr_who_made_the_request
    friend_request.save()
    return render(
        request, "all_users.html", {"obj": sent(current_usr_who_made_the_request)}
    )


def process(request):
    log = True
    return render(request, "sinup.html", locals())


def process_recieved(request):
    return HttpResponse(request.session["name"])


def all_users(request):
    if request.session["name"]:
        request_sent_info = sent(request.session["name"])
        friend_requests_count = (
            "" if request_data(request)[1] == 0 else request_data(request)[1]
        )
        return render(
            request,
            "all_users.html",
            {"obj": request_sent_info, "count": friend_requests_count},
        )
    return render(request, "login.html")


def logout(request):
    try:
        curr_usr = UserData.objects.get(name=request.session["name"])
        curr_usr.color = "white"
        curr_usr.save()
        del request.session["name"]
        return redirect("/")
    except Exception as e:
        raise ValueError(f"Unable to logout : {e}")


def get_usr_pass_from_request(request):
    user, password = "", ""
    if request.method == "POST":
        MyLoginForm = SignupForm(request.POST, request.FILES)
        if MyLoginForm.is_valid():
            user = MyLoginForm.cleaned_data["username"]
            password = MyLoginForm.cleaned_data["password"]
    return user, password


def login_process(request):
    user, password = get_usr_pass_from_request(request)
    for usr_obj in UserData.objects.filter(user=user):
        if password == usr_obj.password:
            request.session["name"] = usr_obj.name
            user = request.session["name"]
            online(user)
            return redirect("/all_users/")
    return render(request, "login.html", {"checking": "invalid user"})


def save_usr_info(MyLoginForm):
    obj = UserData()
    obj.password = MyLoginForm.cleaned_data["password"]
    obj.age = MyLoginForm.cleaned_data["age"]
    obj.user = MyLoginForm.cleaned_data["username"]
    obj.name = MyLoginForm.cleaned_data["name"]
    obj.image = MyLoginForm.cleaned_data["image"]
    obj.save()


def validate_user_input(request, MyLoginForm):
    username = MyLoginForm.cleaned_data["username"]
    name = MyLoginForm.cleaned_data["name"]

    if username in [i.user for i in UserData.objects.all()]:
        return False, render(request, "sinup.html", {"checking": "username exists"})
    if " " in username:
        return False, render(
            request,
            "sinup.html",
            {"checking": "Don't use space in username"},
        )
    if name in [i.name for i in UserData.objects.all()]:
        return False, render(request, "sinup.html", {"checking": "name exists"})
    if " " in name:
        return False, render(
            request, "sinup.html", {"checking": "Don't use space in name"}
        )
    return True, ""


def validate_user_form(request, MyLoginForm):
    if request.method == "POST":
        if MyLoginForm.is_valid():
            is_valid, error_msg = validate_user_input(request, MyLoginForm)
            if not is_valid:
                return False, error_msg
            save_usr_info(MyLoginForm)
        return True, ""
    return False, render(request, "sinup.html", {"checking": "Http method not allowed"})


def sinup_process(request):
    MyLoginForm = LoginForm(request.POST, request.FILES)
    is_valid, error_msg = validate_user_form(request, MyLoginForm)
    if not is_valid:
        return error_msg
    request.session["name"] = MyLoginForm.cleaned_data["name"]
    online(MyLoginForm.cleaned_data["name"])
    return render(request, "all_users.html", {"obj": UserData.objects.all()})


def friends(request):
    obj = []
    for friend_obj in Friend.objects.filter(name=request.session["name"]):
        friend_name = friend_obj.friend_name
        for friend_info in UserData.objects.filter(name=friend_name):
            d = {
                "name": friend_name,
                "image": friend_info.image,
                "color": friend_info.color,
            }
            obj.insert(0, d)
    return render(request, "friends.html", {"obj": obj})


def extract_chats_info_in_asc(chats, usr):
    chats_list = []
    for chat in chats:
        chats_list.insert(0, {"num": chat.num, "msg": chat.msg, "name": usr})
    return chats_list


def chatting(request, name):
    """chats routing logic"""
    friend_name = name
    curr_usr = request.session["name"]
    chats_curr_usr_and_friend = ChatData.objects.filter(
        name=curr_usr, friend_name=friend_name
    )
    chats_friend_and_curr_usr = ChatData.objects.filter(
        name=friend_name, friend_name=curr_usr
    )
    all_chats = extract_chats_info_in_asc(
        chats_curr_usr_and_friend, curr_usr
    ) + extract_chats_info_in_asc(chats_friend_and_curr_usr, friend_name)

    for chat in UserData.objects.filter(name=friend_name):
        return render(
            request,
            "public_profile.html",
            {
                "obj": sorted(all_chats, key=lambda s: s["num"]),
                "f_img": chat.image.url,
                "f_name": chat.name,
            },
        )
    raise ValueError("chats routing failed")


def get_field(field, MyLoginForm):
    try:
        return MyLoginForm.cleaned_data[f"{field}"]
    except:
        return ""


def validate_and_clean_chats(MyLoginForm):
    msg, image = "", ""
    if MyLoginForm.is_valid():
        msg = MyLoginForm.cleaned_data["msg"]
        image = MyLoginForm.cleaned_data["image"]
    if not MyLoginForm.is_valid():
        msg = get_field("msg", MyLoginForm)
        image = get_field("image", MyLoginForm)
    return msg, image


def get_chatid():
    rec = MessageTracker.objects.get(name="track")
    rec.num = rec.num + 1
    rec.save()
    return rec.num


def chatting_process(request, name):
    """logic to process the chats"""
    msg, image = "", ""
    if request.method == "POST":
        msg, image = validate_and_clean_chats(ChatDataForm(request.POST, request.FILES))
    if image != "" or msg != "":
        chat = ChatData(
            name=request.session["name"],
            friend_name=name,
            msg=msg,
            image=image,
            num=get_chatid(),
        )
        chat.save()
    return redirect("/chatting/" + name)


def usr_to_friend_chats(curr_usr, friend_name):
    chats = []
    for chat in ChatData.objects.filter(name=curr_usr, friend_name=friend_name):
        try:
            image = chat.image.url
        except:
            image = ""
        chats.insert(
            0, {"num": chat.num, "msg": chat.msg, "name": curr_usr, "image": image}
        )
    return chats


def json(request, name):
    friend_name = name
    curr_usr = request.session["name"]

    chats = usr_to_friend_chats(curr_usr, friend_name) + usr_to_friend_chats(
        friend_name, curr_usr
    )

    data = dict()
    for i in UserData.objects.filter(name=friend_name):
        data = {
            "obj": sorted(chats, key=lambda s: s["num"]),
            "f_name": i.name,
            "f_img": i.image.url,
            "user": curr_usr,
        }
    return JsonResponse(data)


def delete_friend_requests(name):
    for friend_obj in Friend.objects.filter(name=name):
        usr_to_friend_request = FriendRequest.objects.filter(
            name=name, Request=friend_obj.friend_name
        )
        usr_to_friend_request.delete()


def get_usr_to_friend_chats(curr_usr, friend_name):
    chats = []
    for chat_obj in ChatData.objects.filter(name=curr_usr, friend_name=friend_name):
        chats.insert(0, {"num": chat_obj.num, "msg": chat_obj.msg, "name": curr_usr})
    return chats


def chat_size(request, name):
    curr_usr = request.session["name"]
    chats = get_usr_to_friend_chats(curr_usr, name) + get_usr_to_friend_chats(
        name, curr_usr
    )
    return JsonResponse({"size": len(sorted(chats, key=lambda s: s["num"]))})


def online(user):
    temp = UserData.objects.get(name=user)
    temp.color = "green"
    temp.save()


def decline_request(request, name):
    temp = FriendRequest.objects.get(name=request.session["name"], Request=name)
    temp.delete()
    return redirect("/all_users/")
