from django.shortcuts import render
from .models import park
from datetime import datetime,timezone
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def parking(request):
    parking=park.objects.all()
    print(parking)
    if request.method=='POST':
        print("hy")
        car_number=request.POST.get('car_number','')
        book_slot=[]
        free_slot=[]
        
        print(car_number)
        for i in parking:
            book_slot.append(i.car_slot)
        for i in range(1,6):
            if(i in book_slot):
               print("")     
            else:
                free_slot.append(i)
        if(len(free_slot)!=0):
            print(free_slot[0])
            car_par=park(car_number=car_number,car_slot=free_slot[0])
            car_par.save()
            messages.success(request,'Successfuly Enter the Car in slot'+str(free_slot[0]))
        else:
            messages.error(request,'Sorry Parking Lot is Full')       
    return render(request,'parking.html')
def car_leave(request):
    if request.method=='POST':
        car_slot=request.POST.get('car_slot','')
        parking_car=park.objects.filter(car_slot=car_slot)
        for i in parking_car:
            time_in=i.time_in
        time=time_in-datetime.now(timezone.utc)
        messages.success(request," Your parking time is "+str(time.seconds)+"Seconds"+" Your amount is $"+str(time.seconds))
        parking_car.delete()
    return render(request,'car_leave.html')