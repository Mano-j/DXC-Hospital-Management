from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import PatientDetails, DoctorDetails
from .forms import postForm
import operator
import schedule
import time
import threading



def start_BG_process():
    
    t = threading.Thread(target=reduceTime, args=(), kwargs={})
    t.setDaemon(True)
    t1 = threading.Thread(target=assign, args=(), kwargs={})
    t1.start()
    t.start()

    return True


def reduceTime():
    while True:
        time.sleep(60)
        
        busyDoctors = DoctorDetails.objects.all().filter(doctor_availability=False, is_Doctor_servicing=True)
        print("BusyDocList ", busyDoctors)

        if len(busyDoctors) > 0:
            for doctor in busyDoctors:
                
                if doctor.remaining_time > 0 :
                    doctor.remaining_time -= 1
                    doctor.save()
                else:
                    doctor.doctor_availability = True
                    doctor.remaining_time = 0
                    doctor.save()


def assign():
    while True:
        time.sleep(10)
        patientList = PatientDetails.objects.all().filter(doctorDetails=None)
        

        if len(patientList) > 0:
            print("patientList Queue = ", patientList) 

            eList = patientList.filter(criticality='E')
            uList = patientList.filter(criticality='U')
            nList = patientList.filter(criticality='N')
            
            """++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ NOTE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
            # These are the time periods alloted for patients depending upon their health status.
            # eTime - Time for emmergency case patients
            # uTime - Time for urgent case patients
            # nTime - Time for normal case patients

            # For demonstration the time period is kept low. kindly change as needed. ( time is in minutes)
            """++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ END OF NOTE +++++++++++++++++++++++++++++++++++++++++++++++++++"""

            eTime = 3 + 2 
            uTime = 2 + 2
            nTime = 1 + 2

            if len(eList) > 0:
                # print("inside Emmergency list")
                for patient in eList:
                    availableDoctors = DoctorDetails.objects.all().filter(doctor_availability=True, is_Doctor_servicing=True)
                    fixDoctor(patient, availableDoctors, eTime)

            elif len(uList) > 0:
                # print("inside urgent list")
                for patient in uList: 
                    availableDoctors = DoctorDetails.objects.all().filter(doctor_availability=True, is_Doctor_servicing=True)
                    fixDoctor(patient, availableDoctors, uTime)

            elif len(nList) > 0:
                # print("inside normal list")
                for patient in nList: 
                    availableDoctors = DoctorDetails.objects.all().filter(doctor_availability=True, is_Doctor_servicing=True)
                    fixDoctor(patient, availableDoctors, nTime)
            
assignmentDetails = []
def fixDoctor(patient, availableDoctors, Time):

    if len(availableDoctors) > 0:
        print(patient)
        patient.doctorDetails = availableDoctors[0]
        availableDoctors[0].doctor_availability = False
        availableDoctors[0].remaining_time = Time 
        patient.save()
        availableDoctors[0].save()

        temp = "Patient " + str(patient) + " is assigned to Dr." + str(availableDoctors[0])
        print(temp)
        global assignmentDetails
        assignmentDetails.append(temp)
        print("Current Patient: -->", assignmentDetails)
   
    else:
        print("No Doctor available now for patient, ", patient)
        time.sleep(2)


def index(request):
    doctor_list = DoctorDetails.objects.order_by('-doctor_availability')

    form = postForm(request.POST or None)
    if form.is_valid():
        pk_form = form.save()
        return HttpResponseRedirect("/")

        
    global assignmentDetails

    context= {
        'doctor_list' : doctor_list,
        'form' : form,
        'assignmentDetails' : assignmentDetails
    }
    return render(request, 'newHome.html', context)




def doctorDetails(request, id):

    doctor = DoctorDetails.objects.get(id=id)

    form = postForm(request.POST or None)
    
    if form.is_valid():
        form.save()
    context = {'doctor': doctor, 'form': form}
    
    return render(request, 'Doctor/bookAppointment.html', context)



def doctor_page_view(request):

    doctor = DoctorDetails.objects.all().get(doctor_name=request.user),

    checkValue = doctor[0].is_Doctor_servicing
    
    if request.method == "POST":
        isServing = request.POST.get('isServing', None)
        if isServing != "on":
            # print("Turning False")
            doctor[0].is_Doctor_servicing = False
            doctor[0].remaining_time = 0
            doctor[0].save()

        else:
            # print("Turning True")
            doctor[0].is_Doctor_servicing = True
            doctor[0].remaining_time = 0
            doctor[0].save()
        
    checkValue = doctor[0].is_Doctor_servicing

    context = {                
        'patientList' : doctor[0].patientdetails_set.all(), 
        'checkValue' : checkValue,
    }
    
    return render(request, 'Doctor/yourPage.html', context)



