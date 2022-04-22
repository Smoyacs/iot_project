# django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


# modelos
from iot_devices.models import Device
from iot_devices.forms import DeviceForm




# otros
import pandas as pd


class Dashboard(View):
    def get(self, request):
        
        # obtenemos el usuario de la sesion
        
        # user = User
        devicess= Device.objects.all()

        context = {
            # 'user': user,
            'all_devicess':devicess
        }
        
        return render(request, 'iot_devices/dashboard.html', context)



####################################################################

class AddNewDev(View):
    
    
    
    def get(self, request):

        form = DeviceForm()
        context = {
            'form': form,
  
        }
        return render(request, 'iot_devices/create.html', context)

    def post(self, request):
        print(request.POST)
        print(request.FILES)
        
        User = request.user
        
        form = DeviceForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.added_by = User
            print(User)
            form.save()
            return redirect(reverse('iot_devices:dashboard'))
        else:
            context = {
                'form': form,
            }
            return render(request,'iot_devices/create.html', context)


def ViewDev(request, id): # GET /wall/<id>
    
    
    

    # Obtenemos la instancia del objeto que queremos utilizar 
    device = Device.objects.get(id=id)
    
    # Obtenemos el archivo csv y ocupamos el nombre para buscar el archivo cvs
    device_name = device.device_id
    file_path = f'iot_devices/static/iot_devices/devices/{device_name}.cvs'
    data = pd.read_csv(file_path, names=["Device_id", "Temperature", "humidity", "Date", "time"], encoding='utf-8')# Escribimos los headers para indentificar cada columna de nuestro archivo cvs
    
    
    
    fecha = data['Date']
    last_data = fecha.iloc[-1]
    
    # limpiamos los datos utilizando pandas
    datetime = data['time'].tail(15)
    list_of_datetime = datetime.tolist() # convertimos los datos a una lista para graficar (EJE X)
    

    temp_1 = data['Temperature'].tail(15)
    list_of_temperature = temp_1.to_list()  # obtenemos temperatura  en lista para graficar (EJE Y)
    
    hum_1 = data['humidity'].tail(15) # obtenemos humedad en lista para graficar (EJE Y)
    list_of_humidity = hum_1.to_list()
    
    
    # ultima temperatura
    last_temp = temp_1.iloc[-1]
    #print(last_temp[0])
    
    # ultima humedad
    last_hum = hum_1.iloc[-1]
    #print(last_hum[0])
    
    #ultimo tiempo
    last_date = datetime.iloc[-1]
    
    #file_path = f'iot_devices/devices/{device_name}.cvs' # para utilizar en static al llamar chart.js
    # img_path = f'iot_devices/images/{device.imageDevice}'
    context = {
        # variables para realizar grafico
        'datetime': list_of_datetime,
        'temp': list_of_temperature,
        'hum': list_of_humidity,
        
        'last_temp': last_temp,
        'last_hum': last_hum,
        'last_date': last_date,
        'last_data': last_data,
        # 'img_path': img_path,
        
        
        'device': device,
        'data': data,
    }
    return render(request, 'iot_devices/DevShow.html', context)


class EditDev(View):
    def get(self, request, id):
        user = request.user
        device = Device.objects.get(id=id)
        form = DeviceForm(instance=device)
        # img_path = f'media/{device.imageDevice}'
        context = {
            # 'img_path': img_path,
            'form': form,
            'user': user,
            'device': device,
        }
        return render(request, 'iot_devices/EditDev.html', context)

    def post(self, request, id):
        device = Device.objects.get(id=id)
        form = DeviceForm(request.POST, request.FILES , instance=device)
        if form.is_valid():
            print(form)
            form.save()
            return redirect(reverse('iot_devices:dashboard'))
        else:
            context = {
                'form': form,
                'device': device,
            }
            return render(request, 'iot_devices/EditDev.html', context)
# *********************************************

# 7 POST Device/<id>/destroy
def DeleteDev(request, id):
    device = Device.objects.get(id=id)
    device.delete()
    return redirect('/dashboard')
# *********************************************

def Logout(request):
    request.session.clear()
    print("Logged Out")
    return redirect('/')

#************************************************



