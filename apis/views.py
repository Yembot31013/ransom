from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, How_To_Pay
import random

def get_random_code():
  num = 0
  count = 8
  rand = ""
  while num < count:
    ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    rand += str(ran)
    num += 1
  
  return rand

def view(request):
  return render(request, "index.html")

def how(request):
  content = How_To_Pay.objects.all()
  context = {
    "content": content
  }
  return render(request, "indexs.html", context)

@api_view(["POST"])
def insert_into_db(request, *arg, **kwarg):
    token = request.query_params.get("token")
    hname = request.query_params.get("host_name")
    oname = request.query_params.get("os_name")
    oversion = request.query_params.get("os_version")
    omanufac = request.query_params.get("os_manufacturer")
    ocon = request.query_params.get("os_configuration")
    obt = request.query_params.get("os_build_type")
    regowner = request.query_params.get("registered_owner")
    regorg = request.query_params.get("registered_organization")
    productId = request.query_params.get("product_iD")
    oid = request.query_params.get("original_Install_Date")
    sbt = request.query_params.get("system_Boot_Time")
    sm = request.query_params.get("system_Manufacturer")
    sysm = request.query_params.get("system_Model")
    syst = request.query_params.get("system_Type")
    process = request.query_params.get("processor")
    biosv = request.query_params.get("bios_Version")
    wd = request.query_params.get("windows_Directory")
    sd = request.query_params.get("system_Directory")
    sl = request.query_params.get("system_Locale")
    il = request.query_params.get("input_Locale")
    tz = request.query_params.get("time_Zone")
    tpm = request.query_params.get("total_Physical_Memory")
    apm = request.query_params.get("available_Physical_Memory")
    
    result = Profile()
    result.token = token
    result.host_name = hname
    result.os_name = oname
    result.os_version = oversion
    result.os_manufacturer = omanufac
    result.os_configuration = ocon
    result.os_build_type = obt
    result.registered_owner = regowner
    result.registered_organization = regorg
    result.product_iD = productId
    result.original_Install_Date = oid
    result.system_Boot_Time = sbt
    result.system_Manufacturer = sm
    result.system_Model = sysm
    result.system_Type = syst
    result.processor = process
    result.bios_Version = biosv
    result.windows_Directory = wd
    result.system_Directory = sd
    result.system_Locale = sl
    result.input_Locale = il
    result.time_Zone = tz
    result.total_Physical_Memory = tpm
    result.available_Physical_Memory = apm
    ex = False
    to_slug = str(get_random_code())
    ex = Profile.objects.filter(token_id=to_slug).exists()
    while ex:
      to_slug = str(get_random_code())
      ex = Profile.objects.filter(token_id=to_slug).exists()
      print("stuck")
    result.token_id = to_slug
    result.save()

    return Response({"status": "success"}, status=200)

@api_view(["POST"])
def confirm_payment(request, *arg, **kwarg):
  token = request.query_params.get("token")
  result = Profile.objects.filter(token = token).order_by("?").first()
  res = result.is_verified
  pen = result.decrypted
  tok = result.token_id
  return Response({"status": res, "token": tok, "pending": pen}, status=200)

@api_view(["GET"])
def check(request, *arg, **kwarg):
  token = request.query_params.get("token")
  print(token)
  result = Profile.objects.filter(token_id = token).first()
  print(result)
  if result:
    res = {
      "res": "success",
      "host_name": result.host_name,
      "registered_owner": result.registered_owner,
      "os_name": result.os_name,
      "os_version": result.os_version,
      "system_Boot_Time": result.system_Boot_Time,
      "system_Manufacturer": result.system_Manufacturer,
      "system_Model": result.system_Model,
      "system_Type": result.system_Type,
      "total_Physical_Memory": result.total_Physical_Memory,
    }
    return Response(res, status=200)
  else:
    return Response({"res": "wrong"}, status=200)

@api_view(["GET"])
def send(request, *arg, **kwarg):
  token = request.query_params.get("token")
  print(token)
  sender_id = request.query_params.get("sender_id")
  result = Profile.objects.filter(token_id = token).first()
  if result:
    result.sender_id = sender_id
    result.decrypted = True
    result.save()

  return Response({"status": "success"}, status=200)